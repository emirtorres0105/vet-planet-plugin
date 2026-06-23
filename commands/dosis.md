---
description: Resuelve una consulta de dosificacion y manejo (dosis por peso, presentacion disponible, dias, advertencias, que mas mandar). Sin PDF.
argument-hint: [especie, peso, edad, cuadro y farmacos/productos disponibles]
---

Resolvé una **consulta de dosificación y manejo** usando la skill
`vetplanet-dosificacion`. Respondé de forma conversacional (sin PDF).

Consulta: $ARGUMENTS

Pasos:
1. Confirmá los datos mínimos: especie, **peso**, edad y cuadro. Si falta el
   peso, pedilo (es imprescindible para dosificar).
2. **Verificá la dosis vía búsqueda web** antes de darla (mg/kg, frecuencia,
   días, dosis máxima) en fuente veterinaria fiable.
3. Calculá por peso y **traducí a la presentación comercial disponible**
   (suspensión mg/mL → mL; tabletas → fracción/unidades).
4. Revisá contraindicaciones por **especie y edad** (p. ej. metronidazol no en
   menores de ~6 semanas; no AINE en geriátrico/cardiópata/deshidratado).
5. Entregá: dosis + volumen + días + **qué más mandar** (manejo integral) +
   **advertencias críticas** del paciente, y recordá que el ajuste final es del
   médico tratante.
