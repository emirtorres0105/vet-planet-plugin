---
description: Genera un informe de control en PDF para el propietario (tono accesible, 1-2 paginas) con la identidad Vet Planet.
argument-hint: [nombre del paciente y datos del caso]
---

Generá un **informe de control para el propietario** de la Clínica Veterinaria
Vet Planet usando la skill `vetplanet-pdf-reports`.

Datos del caso: $ARGUMENTS

Pasos:
1. Leé `SKILL.md` de la skill `vetplanet-pdf-reports` antes de escribir código.
2. Reuní la reseña, hallazgos y plan. Si falta el peso u otro dato clave para
   dosificar o concluir, señalalo.
3. Verificá vía búsqueda web cualquier cifra o referencia antes de incluirla.
4. Redactá con **tono de usted, formal pero accesible**, lenguaje natural
   costarricense, sin jerga innecesaria (explicaciones entre paréntesis cuando
   haga falta). No infantilizar ni aterrorizar; usar analogías de nivel de
   preocupación ("luz amarilla / luz roja") cuando ayude.
5. Generá el PDF (1–2 páginas), verificá la paginación y los datos de contacto,
   y entregá el archivo con `present_files`.
6. **No incluir firma del médico** salvo que se pida explícitamente.
