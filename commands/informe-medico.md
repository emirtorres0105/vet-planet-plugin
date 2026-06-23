---
description: Genera un informe clinico de discusion medico-a-medico en PDF (analisis por tendencia, 3 diferenciales, 3 opciones, referencias).
argument-hint: [paciente, examenes, imagenes y senal de analisis]
---

Generá un **informe clínico de discusión (médico-a-médico)** de la Clínica
Veterinaria Vet Planet usando la skill `vetplanet-pdf-reports`.

Datos del caso: $ARGUMENTS

Pasos:
1. Leé `SKILL.md` y `reference/metodologia.md` de la skill `vetplanet-pdf-reports`.
2. Seguí la **secuencia obligatoria**: urgencias → hilo clínico → cronología →
   laboratorio comparativo (analizar **tendencia**, no solo el valor puntual) →
   imagenología (con disclaimer de lectura digital) → **3 diferenciales**
   jerarquizados (incluir uno benigno) → **3 opciones de manejo** (con cifras y
   advertencias) → próximos pasos priorizados → referencias.
3. Respetá los **umbrales por especie**.
4. **Verificá vía búsqueda web** toda cifra de pronóstico y toda referencia
   (tipo de estudio, n, hallazgo) antes de incluirla. No inventar referencias.
5. Si se aportan imágenes (US/Rx), leelas con criterio "compatible con /
   sugestivo de" y declarando limitaciones.
6. Generá el PDF, blindá los saltos de página (que ninguna tabla ni caja se
   corte), verificá rasterizando, y entregá con `present_files`.
7. **No incluir firma del médico** salvo que se pida explícitamente.
