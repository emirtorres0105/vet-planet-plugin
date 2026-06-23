---
description: Genera una epicrisis clinica en PDF (formal, medico-legal, secciones en numeracion romana, aviso de confidencialidad).
argument-hint: [paciente, cronologia, intervenciones y desenlace]
---

Generá una **epicrisis clínica** (documento médico-legal de cierre de caso) de
la Clínica Veterinaria Vet Planet usando la skill `vetplanet-pdf-reports`.

Datos del caso: $ARGUMENTS

Pasos:
1. Leé `SKILL.md` y `reference/metodologia.md` de la skill `vetplanet-pdf-reports`.
2. Estructurá en **secciones con numeración romana**: I. Resumen ejecutivo ·
   II. Identificación del paciente y propietario · III. Cronología clínica ·
   IV. Motivo de consulta · V. Evaluación diagnóstica al ingreso · VI. Primera
   intervención · VII. Segunda intervención · VIII. Evento adverso (si aplica) ·
   IX. Maniobras de reanimación (si aplica) · X. Causa de muerte (si aplica) ·
   XI. Evolución y desenlace · XII. Validación.
3. Tono **formal y documental**. Cerrá con **aviso de confidencialidad médica** y
   la conservación mínima del expediente (5 años, conforme al Colegio de
   Profesionales en Medicina Veterinaria de Costa Rica).
4. Generá el PDF, verificá la paginación y entregá con `present_files`.
5. **No incluir firma del médico** salvo que se pida explícitamente.
