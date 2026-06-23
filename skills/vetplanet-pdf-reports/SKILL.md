---
name: vetplanet-pdf-reports
description: >-
  Genera informes y reportes clinicos en PDF con la identidad visual de la
  Clinica Veterinaria Vet Planet (logo, marca de agua, paleta teal/dorado/vino,
  tablas con encabezado teal, pie con datos de contacto). Usar SIEMPRE que se
  pida crear un informe de control, informe clinico, reporte de consulta,
  epicrisis, resumen para propietario o cualquier documento PDF de la clinica
  Vet Planet. Cubre estructura, tono por audiencia (medico vs propietario) y
  el motor reutilizable de generacion de PDF.
---

# Vet Planet · Informes y Reportes Clínicos en PDF

Esta skill produce documentos PDF profesionales con la marca Vet Planet. Úsala
cuando el usuario pida un informe, reporte, epicrisis o resumen clínico de la
Clínica Veterinaria Vet Planet.

## Flujo de trabajo

1. **Identificar el tipo de documento** y su audiencia:
   - *Informe de control / resumen para propietario* → tono formal pero accesible, de usted, lenguaje natural costarricense, sin jerga innecesaria. 1–2 páginas.
   - *Informe clínico de discusión (médico-a-médico)* → terminología técnica, tablas comparativas de laboratorio, 3 diferenciales, 3 opciones de manejo, referencias.
   - *Epicrisis* → formal, médico-legal, secciones en numeración romana, aviso de confidencialidad.
2. **Reunir los datos** del caso (reseña, exámenes, hallazgos, plan).
3. **Generar el PDF** con el motor `scripts/vetplanet_report.py`.
4. **Verificar** el resultado: páginas que cierran bien (sin secciones cortadas), datos de contacto correctos, resaltados de tabla coherentes.
5. **Entregar** el archivo al usuario.

## Cómo generar el PDF

El motor está en `scripts/vetplanet_report.py`. Copia ese script y la carpeta
`assets/` (logo.png y watermark.png) al directorio de trabajo, o referencia la
carpeta de assets con `assets_dir=`. Patrón mínimo:

```python
import sys
sys.path.insert(0, "ruta/a/scripts")   # carpeta donde está vetplanet_report.py
from vetplanet_report import VetPlanetReport

r = VetPlanetReport(
    titulo="Informe de Control",
    subtitulo="Seguimiento de condicion urinaria geriatrica",
    fecha="06 de junio de 2026",
    expediente="603",
    output_path="/mnt/user-data/outputs/Informe_Control.pdf",
    assets_dir="ruta/a/assets",          # opcional si assets/ está junto al script
)

r.ficha_paciente([
    ("PACIENTE", "Ghio", "PROPIETARIA", "Melissa Castro S."),
    ("ESPECIE", "Felino (gato)", "EXPEDIENTE", "603"),
    ("EDAD / SEXO", "12 anos / macho castrado", "RAZA", "SRD"),
])

r.seccion("Motivo de la consulta")
r.parrafo("El paciente se presenta a control programado para el seguimiento ...")

r.seccion("Hallazgos de la valoracion")
r.tabla(
    ["EXAMEN", "RESULTADO", "LECTURA"],
    [
        ["Orina - cristales", "Negativo (todos en 0)", "Bien - sin cristales"],
        ["Orina - densidad", "1.030", "A vigilar (ideal en gato > 1.035)"],
        ["SDMA (prueba de rinon)", "12.0 ug/dL (normal <14)", "Normal - tranquilizador"],
    ],
    col_widths=[5, 5, None],             # cm; None = ancho restante
    resaltar={1: "vigilar", 2: "favorable"},
)

r.seccion("Interpretacion clinica")
r.parrafo("Un dato que aporta tranquilidad es que el SDMA se mantiene ...")

r.plan([
    "Repetir control en un plazo de 4 meses (creatinina, SDMA y densidad urinaria, en ayuno).",
    "Completar la evaluacion renal: relacion proteina/creatinina urinaria y presion arterial.",
    "Priorizar la hidratacion: presentacion humeda del alimento y varias fuentes de agua.",
])

r.conclusion(
    "la condicion urinaria del paciente se mantiene controlada. El hallazgo no reviste "
    "gravedad ni urgencia; se mantendra seguimiento con un control en 4 meses.",
    tipo="favorable",                    # favorable | alerta | critico | info
)

r.nota_cierre()
# r.firma("Maria Daniela Gonzalez")      # opcional, solo si se requiere firma

r.cerrar()
```

## API del motor (resumen)

- `VetPlanetReport(titulo, output_path, subtitulo, fecha, expediente, assets_dir, watermark)` — crea el documento con encabezado (logo) y configura la marca de agua.
- `.ficha_paciente(rows)` — tabla de identificación; `rows` = lista de tuplas `(label, valor, label, valor)`.
- `.seccion(titulo)` — encabezado de sección.
- `.parrafo(texto)` — párrafo justificado. Admite `<b>negrita</b>`.
- `.tabla(headers, rows, col_widths, resaltar, keep)` — tabla con encabezado teal. `col_widths` en cm (usar `None` en una columna para el ancho restante). `resaltar` = `{indice_fila: "favorable"|"alerta"|"vigilar"|"critico"}` (índice 0 = primera fila de datos).
- `.plan(items, titulo)` — lista numerada que se mantiene unida (no se corta entre páginas).
- `.conclusion(texto, etiqueta, tipo)` — caja destacada. `tipo` = `favorable|alerta|critico|info`.
- `.nota_cierre(texto)` — nota de uso clínico (texto por defecto si se omite).
- `.firma(nombre, rol)` — bloque de firma (opcional).
- `.espacio(n)` — espaciador vertical.
- `.cerrar()` — escribe el PDF y devuelve la ruta.

## Reglas de estilo (obligatorias)

- **Datos de contacto**: el correo oficial es `clinicaveterinaria@vetplanetcr.com`. Está fijado en el motor (`CLINICA` en el script); no inventar otro.
- **Tono propietario**: tratar de *usted*; lenguaje claro; cuando un término requiera explicación, ponerla entre paréntesis en la misma línea; usar analogías ("luz amarilla / luz roja") para el nivel de preocupación sin alarmismo; no infantilizar ni aterrorizar.
- **Resaltado de tablas**: dorado (`vigilar`/`alerta`) para el dato a observar; verde (`favorable`) para el hallazgo tranquilizador; rojo (`critico`) para lo urgente.
- **Interpretación por especie**: respetar umbrales de la especie correcta (p. ej. densidad urinaria felina adecuada > 1.035; canina > 1.030).
- **Disclaimers**: incluir nota de cierre de uso clínico; en documentos médicos agregar que el diagnóstico definitivo requiere confirmación y que las lecturas de imagen tienen limitaciones.
- **Verificar paginación**: usar `.plan()` y `keep=True` en tablas que no deban cortarse; revisar que el documento cierre limpio.

## Recursos de la skill

- `scripts/vetplanet_report.py` — motor de generación de PDF (importable).
- `assets/logo.png` — logo Vet Planet (fondo transparente) para el encabezado.
- `assets/watermark.png` — versión atenuada para la marca de agua de fondo.
- `reference/metodologia.md` — metodología clínica completa (estructura, frameworks, fuentes) para el contenido de los informes.

## Dependencias

Requiere `reportlab`. Instalar si no está disponible:
`pip install reportlab --break-system-packages`
