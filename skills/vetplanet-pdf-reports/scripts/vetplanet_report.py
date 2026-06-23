#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor de informes PDF - Clinica Veterinaria Vet Planet
=======================================================
Modulo reutilizable para generar informes y reportes clinicos con la
identidad visual de Vet Planet (logo, marca de agua, paleta, tablas).

USO BASICO
----------
    from vetplanet_report import VetPlanetReport, COLORS

    r = VetPlanetReport(
        titulo="Informe de Control",
        subtitulo="Seguimiento de condicion urinaria geriatrica",
        fecha="06 de junio de 2026",
        output_path="/mnt/user-data/outputs/Informe.pdf",
    )
    r.ficha_paciente([
        ("PACIENTE", "Ghio", "PROPIETARIA", "Melissa Castro S."),
        ("ESPECIE", "Felino (gato)", "EXPEDIENTE", "603"),
        ("EDAD / SEXO", "12 anos / macho castrado", "RAZA", "SRD"),
    ])
    r.seccion("Motivo de la consulta")
    r.parrafo("El paciente se presenta a control ...")
    r.seccion("Hallazgos de la valoracion")
    r.tabla(
        ["EXAMEN", "RESULTADO", "LECTURA"],
        [["Orina - cristales", "Negativo", "Bien"], ...],
        col_widths=[5, 5, None],          # cm; None = resto del ancho
        resaltar={1: "favorable"},        # fila: favorable|alerta|critico|vigilar
    )
    r.plan(["Repetir control en 4 meses ...", "Completar UPC ...", ...])
    r.conclusion("La condicion urinaria del paciente se mantiene controlada ...")
    r.cerrar()                            # escribe el PDF

NOTAS
-----
- Coloque logo.png y watermark.png en la subcarpeta assets/ junto al script,
  o pase rutas explicitas via VetPlanetReport(assets_dir=...).
- Los anchos de columna se expresan en centimetros. Use None en UNA columna
  para que tome el ancho restante.
- Para un informe tecnico (medico-a-medico) use el mismo motor; agregue mas
  secciones, tablas comparativas y una seccion de referencias al final.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, HRFlowable, Image, KeepTogether)
from reportlab.lib.utils import ImageReader

# ── PALETA OFICIAL VET PLANET ─────────────────────────────────────────────────
COLORS = {
    'teal':      colors.HexColor('#1F6B6B'),
    'dark_teal': colors.HexColor('#14524F'),
    'head_teal': colors.HexColor('#2E7D7A'),
    'light':     colors.HexColor('#E8F1F0'),
    'gold':      colors.HexColor('#A98B3D'),
    'light_gold':colors.HexColor('#F7F1E1'),
    'wine':      colors.HexColor('#7A1F1F'),
    'green':     colors.HexColor('#1E6B3A'),
    'light_green':colors.HexColor('#EAF4EC'),
    'row_alt':   colors.HexColor('#F2F7F6'),
    'dark_gray': colors.HexColor('#333333'),
    'mid_gray':  colors.HexColor('#7A7A7A'),
    'line':      colors.HexColor('#C9D9D7'),
    'white':     colors.white,
}

# Datos de contacto oficiales (editar aqui si cambian)
CLINICA = {
    'nombre':  'CLINICA VETERINARIA VET PLANET',
    'ciudad':  'Cartago, Costa Rica',
    'tel':     '7143 3060',
    'correo':  'clinicaveterinaria@vetplanetcr.com',
    'redes':   '@clinicavetplanet',
    'expediente_label': 'Documento Medico-Veterinario Confidencial',
}

# Mapas de resaltado de filas/celdas
_HIGHLIGHT = {
    'favorable': COLORS['light_green'],
    'alerta':    COLORS['light_gold'],
    'vigilar':   COLORS['light_gold'],
    'critico':   colors.HexColor('#F7ECEC'),
}

W, H = A4


class VetPlanetReport:
    def __init__(self, titulo, output_path, subtitulo='', fecha='',
                 expediente='', assets_dir=None, watermark=True):
        self.titulo = titulo
        self.subtitulo = subtitulo
        self.fecha = fecha
        self.expediente = expediente or '---'
        self.output_path = output_path
        self.watermark_on = watermark
        self.story = []
        self.CW = W - 4 * cm

        if assets_dir is None:
            assets_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')
        self.logo_path = os.path.join(assets_dir, 'logo.png')
        self.wm_path = os.path.join(assets_dir, 'watermark.png')
        self._wm_reader = ImageReader(self.wm_path) if (watermark and os.path.exists(self.wm_path)) else None

        self._build_styles()
        self._build_header()

    # ── ESTILOS ───────────────────────────────────────────────────────────────
    def _build_styles(self):
        ss = getSampleStyleSheet()
        def mk(n, **k): return ParagraphStyle(n, parent=ss['Normal'], **k)
        c = COLORS
        self.S = {
            'doctitle': mk('dt', fontName='Helvetica-Bold', fontSize=15, textColor=c['dark_teal'], leading=18, spaceAfter=1),
            'docsub':   mk('ds', fontName='Helvetica', fontSize=8.5, textColor=c['mid_gray']),
            'subhdr':   mk('sh', fontName='Helvetica-Bold', fontSize=10, textColor=c['teal'], spaceBefore=8, spaceAfter=4),
            'body':     mk('body', fontName='Helvetica', fontSize=9.5, textColor=c['dark_gray'], leading=14, spaceAfter=6, alignment=TA_JUSTIFY),
            'tlabel':   mk('tl', fontName='Helvetica-Bold', fontSize=8, textColor=c['gold'], leading=11),
            'tl':       mk('tlc', fontName='Helvetica', fontSize=8.5, textColor=c['dark_gray'], leading=12),
            'tlb':      mk('tlb', fontName='Helvetica-Bold', fontSize=8.5, textColor=c['dark_gray'], leading=12),
            'tc':       mk('tc', fontName='Helvetica', fontSize=8.5, textColor=c['dark_gray'], alignment=TA_CENTER, leading=12),
            'th':       mk('th', fontName='Helvetica-Bold', fontSize=8, textColor=c['white'], alignment=TA_LEFT),
            'thc':      mk('thc', fontName='Helvetica-Bold', fontSize=8, textColor=c['white'], alignment=TA_CENTER),
            'conf':     mk('conf', fontName='Helvetica-Oblique', fontSize=6.5, textColor=c['mid_gray'], alignment=TA_CENTER, leading=9),
        }

    def P(self, txt, st='body'):
        return Paragraph(txt, self.S[st])

    # ── ENCABEZADO CON LOGO ─────────────────────────────────────────────────────
    def _build_header(self):
        rows = [[self.P(self.titulo, 'doctitle')]]
        if self.subtitulo:
            rows.append([self.P(self.subtitulo, 'docsub')])
        if self.fecha:
            rows.append([self.P(f'Fecha: {self.fecha}', 'docsub')])
        title_cell = Table(rows, colWidths=[self.CW - 3.4 * cm])
        title_cell.setStyle(TableStyle([
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 1), ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        if os.path.exists(self.logo_path):
            logo = Image(self.logo_path, width=3.0 * cm, height=3.0 * cm * (704 / 900))
            head = Table([[logo, title_cell]], colWidths=[3.4 * cm, self.CW - 3.4 * cm])
        else:
            head = Table([[title_cell]], colWidths=[self.CW])
        head.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (0, 0), 0), ('RIGHTPADDING', (0, 0), (0, 0), 6),
        ]))
        self.story.append(head)
        self.story.append(HRFlowable(width='100%', thickness=2, color=COLORS['teal'], spaceBefore=4, spaceAfter=10))

    # ── FICHA DEL PACIENTE ──────────────────────────────────────────────────────
    def ficha_paciente(self, rows):
        """rows: lista de tuplas (label1, val1, label2, val2)."""
        data = []
        for r in rows:
            data.append([self.P(r[0], 'tlabel'), self.P(r[1], 'tl'),
                         self.P(r[2], 'tlabel'), self.P(r[3], 'tl')])
        t = Table(data, colWidths=[2.6 * cm, self.CW / 2 - 2.6 * cm, 2.6 * cm, self.CW / 2 - 2.6 * cm])
        t.setStyle(TableStyle([
            ('ROWBACKGROUNDS', (0, 0), (-1, -1), [COLORS['light'], COLORS['white']]),
            ('GRID', (0, 0), (-1, -1), 0.4, COLORS['line']),
            ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('LEFTPADDING', (0, 0), (-1, -1), 7), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        self.story.append(t)
        self.story.append(Spacer(1, 8))

    # ── SECCIONES Y PARRAFOS ────────────────────────────────────────────────────
    def seccion(self, titulo):
        self.story.append(self.P(titulo, 'subhdr'))

    def parrafo(self, texto):
        self.story.append(self.P(texto))

    def espacio(self, n=6):
        self.story.append(Spacer(1, n))

    # ── TABLAS ──────────────────────────────────────────────────────────────────
    def tabla(self, headers, rows, col_widths=None, resaltar=None, keep=False):
        """
        headers: lista de encabezados.
        rows: lista de filas (cada fila es lista de celdas).
        col_widths: lista en cm; usar None en UNA columna para el ancho restante.
        resaltar: dict {indice_fila_de_datos: 'favorable'|'alerta'|'vigilar'|'critico'}
                  (el indice 0 es la primera fila de datos, no el encabezado).
        keep: si True, mantiene la tabla unida en una pagina.
        """
        resaltar = resaltar or {}
        # encabezado: primera col a la izquierda, resto centrado
        head = [self.P(h, 'th' if i == 0 else 'thc') for i, h in enumerate(headers)]
        data = [head]
        for r in rows:
            data.append([self.P(str(c), 'tlb' if i == 0 else 'tc') for i, c in enumerate(r)])

        # anchos
        if col_widths is None:
            widths = [self.CW / len(headers)] * len(headers)
        else:
            fixed = sum(w for w in col_widths if w is not None) * cm
            widths = []
            for w in col_widths:
                widths.append((self.CW - fixed) if w is None else w * cm)

        t = Table(data, colWidths=widths)
        style = [
            ('BACKGROUND', (0, 0), (-1, 0), COLORS['head_teal']),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [COLORS['white'], COLORS['row_alt']]),
            ('GRID', (0, 1), (-1, -1), 0.4, COLORS['line']),
            ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('LEFTPADDING', (0, 0), (-1, -1), 7), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]
        for fila, tipo in resaltar.items():
            color = _HIGHLIGHT.get(tipo, COLORS['light_gold'])
            style.append(('BACKGROUND', (0, fila + 1), (-1, fila + 1), color))
        t.setStyle(TableStyle(style))
        self.story.append(KeepTogether([t]) if keep else t)
        self.story.append(Spacer(1, 8))

    # ── PLAN NUMERADO ───────────────────────────────────────────────────────────
    def plan(self, items, titulo='Plan de manejo recomendado'):
        data = [[self.P(f'<b>{i+1}.</b>', 'tc'), self.P(t, 'tl')] for i, t in enumerate(items)]
        t = Table(data, colWidths=[0.9 * cm, self.CW - 0.9 * cm])
        t.setStyle(TableStyle([
            ('ROWBACKGROUNDS', (0, 0), (-1, -1), [COLORS['white'], COLORS['row_alt']]),
            ('LINEBELOW', (0, 0), (-1, -2), 0.3, COLORS['line']),
            ('BOX', (0, 0), (-1, -1), 0.5, COLORS['line']),
            ('TOPPADDING', (0, 0), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('LEFTPADDING', (0, 0), (-1, -1), 7), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        # Mantener titulo + tabla juntos para que no se corten entre paginas
        self.story.append(KeepTogether([self.P(titulo, 'subhdr'), t]))
        self.story.append(Spacer(1, 8))

    # ── CAJA DE CONCLUSION / CALLOUT ────────────────────────────────────────────
    def conclusion(self, texto, etiqueta='Conclusion', tipo='favorable'):
        borde = {'favorable': COLORS['green'], 'alerta': COLORS['gold'],
                 'critico': COLORS['wine'], 'info': COLORS['teal']}.get(tipo, COLORS['green'])
        fondo = {'favorable': COLORS['light_green'], 'alerta': COLORS['light_gold'],
                 'critico': colors.HexColor('#F7ECEC'), 'info': COLORS['light']}.get(tipo, COLORS['light_green'])
        cell = self.P(f'<b>{etiqueta}:</b> {texto}')
        t = Table([[cell]], colWidths=[self.CW])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), fondo),
            ('LINEBEFORE', (0, 0), (0, -1), 3, borde),
            ('BOX', (0, 0), (-1, -1), 0.5, borde),
            ('TOPPADDING', (0, 0), (-1, -1), 8), ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 12), ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ]))
        self.story.append(t)
        self.story.append(Spacer(1, 14))

    def nota_cierre(self, texto=None):
        if texto is None:
            texto = ('Documento de uso clinico de la Clinica Veterinaria Vet Planet. '
                     'La informacion de este reporte corresponde a una visita de control '
                     'y debe interpretarse junto con el seguimiento del paciente.')
        self.story.append(self.P(texto, 'conf'))

    # ── FIRMA (opcional) ────────────────────────────────────────────────────────
    def firma(self, nombre, rol='Regente Veterinario'):
        ss = getSampleStyleSheet()
        sg = ParagraphStyle('sg', parent=ss['Normal'], fontName='Helvetica-Bold',
                            fontSize=9, textColor=COLORS['dark_gray'], alignment=TA_CENTER, spaceAfter=1)
        sr = ParagraphStyle('sr', parent=ss['Normal'], fontName='Helvetica',
                            fontSize=8, textColor=COLORS['mid_gray'], alignment=TA_CENTER)
        self.story.append(Spacer(1, 20))
        sign = Table([[Paragraph(nombre, sg)],
                      [Paragraph(f'{rol}  -  Clinica Veterinaria Vet Planet', sr)]], colWidths=[8 * cm])
        sign.setStyle(TableStyle([('LINEABOVE', (0, 0), (0, 0), 0.6, COLORS['dark_gray']),
                                  ('TOPPADDING', (0, 0), (0, 0), 5), ('ALIGN', (0, 0), (-1, -1), 'CENTER')]))
        wrap = Table([[sign]], colWidths=[self.CW])
        wrap.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER')]))
        self.story.append(wrap)

    # ── DECORACION DE PAGINA (marca de agua + pie) ──────────────────────────────
    def _on_page(self, canvas, doc):
        canvas.saveState()
        if self._wm_reader is not None:
            wmw = 13 * cm
            wmh = wmw * (938 / 1200)
            canvas.drawImage(self._wm_reader, (W - wmw) / 2, (H - wmh) / 2,
                             width=wmw, height=wmh, mask='auto')
        canvas.setStrokeColor(COLORS['line']); canvas.setLineWidth(0.5)
        canvas.line(2 * cm, 1.6 * cm, W - 2 * cm, 1.6 * cm)
        canvas.setFont('Helvetica-Bold', 7); canvas.setFillColor(COLORS['teal'])
        canvas.drawCentredString(W / 2, 1.35 * cm, CLINICA['nombre'])
        canvas.setFont('Helvetica', 6.5); canvas.setFillColor(COLORS['mid_gray'])
        canvas.drawCentredString(W / 2, 1.13 * cm,
            f"{CLINICA['ciudad']}   |   Tel. {CLINICA['tel']}   |   {CLINICA['correo']}   |   {CLINICA['redes']}")
        canvas.setFont('Helvetica', 6)
        canvas.drawRightString(W - 2 * cm, 0.9 * cm, f'Pag. {canvas.getPageNumber()}')
        canvas.restoreState()

    # ── ESCRIBIR PDF ────────────────────────────────────────────────────────────
    def cerrar(self):
        doc = SimpleDocTemplate(self.output_path, pagesize=A4,
                                leftMargin=2 * cm, rightMargin=2 * cm,
                                topMargin=1.6 * cm, bottomMargin=1.9 * cm,
                                title=self.titulo, author=CLINICA['nombre'])
        doc.build(self.story, onFirstPage=self._on_page, onLaterPages=self._on_page)
        return self.output_path
