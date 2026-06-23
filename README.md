# Plugin Vet Planet — Asistente Clínico

Convierte a Claude (en **Cowork**, Desktop y la web) en el asistente clínico de
la **Clínica Veterinaria Vet Planet** (Cartago, Costa Rica): genera informes
clínicos en PDF con la identidad de la clínica y resuelve consultas de
dosificación y manejo con dosis verificadas.

---

## Qué incluye

**Skills (2)**

- `vetplanet-pdf-reports` — genera documentos PDF con la marca Vet Planet (logo,
  marca de agua, paleta teal/dorado/vino, tablas con encabezado teal, pie con
  datos de contacto). Tipos: informe de control para propietario, informe
  médico-a-médico, epicrisis. Incluye el motor de PDF (`scripts/`), los assets
  (`assets/`) y la metodología clínica completa (`reference/metodologia.md`).
- `vetplanet-dosificacion` — resuelve consultas de dosis y manejo (cálculo por
  peso, traducción a la presentación comercial, días, advertencias por
  especie/edad, manejo integral). No genera PDF.

**Comandos rápidos (slash commands)**

- `/informe-control` — informe de control para el propietario (1–2 páginas).
- `/informe-medico` — informe médico-a-médico (tendencia, 3 diferenciales, 3
  opciones, referencias).
- `/epicrisis` — epicrisis médico-legal (secciones romanas, confidencialidad).
- `/dosis` — consulta de dosificación y manejo (sin PDF).

---

## Cómo se usa

Una vez instalado, podés:

- Escribir naturalmente: *"informe de control para Ghio"*, *"analicemos este
  caso, te paso los exámenes"*, *"¿qué dosis de metronidazol para 5.6 kg?"* — las
  skills se activan solas cuando son relevantes.
- O usar los comandos rápidos: `/informe-medico`, `/dosis`, etc.

> **Nota importante:** las skills dan **formato, estructura y metodología**; la
> consulta de evidencia en tiempo real (journals, dosis) la hace Claude con la
> **búsqueda web**. Asegurate de tener la búsqueda web y la **ejecución de
> código** habilitadas (Settings → Capabilities), ya que el motor de PDF corre en
> Python.

## Dependencias

El motor de PDF requiere `reportlab`. Si no está disponible en el entorno:
`pip install reportlab --break-system-packages`

---

## Instalación en Cowork

1. Abrí **Customize** (barra lateral) → pestaña **Plugins**.
2. En *Personal plugins*, tocá **"+"** → **Add marketplace**, y apuntá a la
   carpeta de este plugin (o subí el `.zip`).
3. Instalá el plugin **vet-planet** y dejalo habilitado.
4. Verificá que **code execution** esté activo (Settings → Capabilities).

> También se puede instalar solo una skill suelta desde Customize → Skills → "+"
> si preferís no usar el plugin completo.

## Estructura del plugin

```
vet-planet/
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── commands/
│   ├── informe-control.md
│   ├── informe-medico.md
│   ├── epicrisis.md
│   └── dosis.md
├── skills/
│   ├── vetplanet-pdf-reports/
│   │   ├── SKILL.md
│   │   ├── scripts/vetplanet_report.py
│   │   ├── assets/ (logo.png, watermark.png)
│   │   └── reference/metodologia.md
│   └── vetplanet-dosificacion/
│       └── SKILL.md
└── README.md
```

---

*Clínica Veterinaria Vet Planet · Cartago, Costa Rica · clinicaveterinaria@vetplanetcr.com · @clinicavetplanet*
