---
name: vetplanet-dosificacion
description: >-
  Resuelve consultas de dosificacion de farmacos y planes de manejo para
  pacientes de la Clinica Veterinaria Vet Planet. Usar SIEMPRE que se pregunte
  por una dosis (mg/kg, mL, dias de tratamiento), por que farmaco o producto
  usar, o por el manejo integral de una condicion (que mas mandar). Calcula la
  dosis por peso y la traduce a la presentacion comercial disponible, respeta
  umbrales y contraindicaciones por especie y edad, y entrega advertencias
  criticas. NO genera PDF: responde de forma conversacional y estructurada.
  Cubre antiparasitarios (giardia, coccidios, helmintos), antibioticos,
  antiemeticos, analgesia, gastroproteccion, probioticos y soporte.
---

# Vet Planet · Dosificación y Manejo Clínico

Esta skill responde consultas de dosis y de manejo para los pacientes de la
clínica. **No produce PDF**: entrega una respuesta clara, de colega a colega,
con la dosis calculada, la traducción a la presentación disponible, los días de
tratamiento, las advertencias críticas y el manejo integral ("qué más mandar").

## Regla de oro: verificar antes de dosificar

**Antes de dar cualquier cifra de dosis, verificarla con búsqueda web** (fuente
veterinaria fiable: Plumb's, MSD/Merck Vet Manual, monografías del producto,
guías de especialidad). No dar dosis de memoria. El estándar de la clínica es
"sin errores": una dosis equivocada puede dañar al paciente.

## Flujo de trabajo

1. **Confirmar los datos mínimos:** especie, **peso** (imprescindible), edad
   (clave para contraindicaciones), y el cuadro/diagnóstico.
2. **Verificar la dosis** del fármaco vía búsqueda web (mg/kg, frecuencia, días,
   dosis máxima).
3. **Calcular por peso** y **traducir a la presentación comercial** que tenga la
   clínica (suspensión mg/mL → mL; tabletas mg → fracción/unidades).
4. **Revisar contraindicaciones** por especie y edad (ver más abajo).
5. **Entregar:** dosis + volumen + días + advertencias + "qué más mandar"
   (manejo integral).

## Cómo calcular y traducir a la presentación

- **Suspensión:** `mL por toma = (mg/kg × peso_kg) ÷ concentración_mg/mL`.
  Ej.: metronidazol 25 mg/kg en un perro de 5.6 kg = 140 mg; con suspensión de
  25 mg/mL → 5.6 mL por toma (con esa concentración el cálculo cae en 1 mL/kg).
- **Tabletas:** si la fracción resultante es incómoda (p. ej. menos de ¼ de
  tableta), preferir la suspensión; decirlo explícitamente.
- **Productos combinados** (p. ej. antiparasitarios con varios principios):
  usar la dosis del producto (mL/kg) y notar qué cubre cada componente.

## Umbrales y contraindicaciones por especie/edad (memoria de la clínica)

- **Metronidazol:** dosis de giardiasis ~25 mg/kg cada 12 h × 5 días; **no
  exceder 50 mg/kg/día** (neurotoxicidad). **Evitar en neonatos / cachorros y
  gatitos menores de ~6 semanas** (metabolismo hepático inmaduro + barrera
  hematoencefálica permeable → riesgo neurológico/hepatorrenal). En pacientes muy
  pequeños o frágiles, usar el extremo conservador (15–20 mg/kg q12h) y cursos
  cortos; vigilar signos neurológicos (ataxia, temblor, nistagmo).
- **Fenbendazol:** primera línea para giardia (50 mg/kg/día × 3–5 días); seguro
  en jóvenes; es el principio activo de varios antiparasitarios combinados.
- **AINEs:** **no usar** en pacientes deshidratados, geriátricos con función
  renal incierta, con sospecha de cardiopatía o con sangrado digestivo; preferir
  un opioide para el dolor.
- **Furosemida:** solo con evidencia de insuficiencia cardíaca; a ciegas empeora
  una disnea no cardíaca o una deshidratación.
- **Enemas de fosfato:** **nunca en gatos** (hiperfosfatemia/hipocalcemia
  graves); usar agua tibia/lactulosa.
- **Lipidosis hepática felina:** en un gato anoréxico (más si tiene sobrepeso),
  no prolongar el ayuno; soporte nutricional temprano.
- **Interpretación por especie:** respetar umbrales de la especie correcta
  (p. ej. densidad urinaria felina adecuada > 1.035; canina > 1.030).

## Plantilla de respuesta (manejo integral)

Estructurar la respuesta así:

1. **Dosis del/los fármaco(s):** por kg → volumen en la presentación disponible
   → frecuencia y días. Incluir alternativa conservadora si aplica.
2. **Qué más mandar (manejo integral):** soporte y medidas no farmacológicas
   propias de la condición (ej. en giardia: baño/limpieza con clorhexidina,
   higiene ambiental, dieta blanda, probiótico, control coprológico de
   seguimiento a las 2–4 semanas).
3. **Advertencias críticas:** contraindicaciones específicas de *ese* paciente
   (especie, edad, peso, comorbilidades).
4. **Cierre:** recordar que el ajuste final es a criterio del médico tratante.

## Esquemas de referencia frecuentes (verificar siempre antes de aplicar)

- **Giardiasis (perro/gato):** fenbendazol 50 mg/kg/día × 3–5 d (primera línea)
  ± metronidazol 25 mg/kg q12h × 5 d (no en muy jóvenes). Productos combinados
  fenbendazol + toltrazuril se dosifican ~1 mL/kg q24h × 3 d (cubren además
  coccidios). Complementar con baño/limpieza perianal con clorhexidina (inicio y
  cierre), higiene ambiental, probiótico, dieta blanda y control coprológico a
  las 2–4 semanas. En gatitos pequeños: no baño de inmersión (hipotermia), solo
  limpieza perianal localizada; probiótico a media dosis por el tamaño.
- **Probiótico (FortiFlora / E. faecium):** 1 sobre/día sobre la comida (por UFC,
  no por kg); en pacientes muy pequeños, media dosis. Continuar 1–2 semanas
  después del antibiótico.

## Importante

- Esta skill es **soporte a la decisión clínica**; el médico veterinario
  tratante valida y ajusta toda dosis y plan.
- Si la consulta deriva en un documento formal (informe/epicrisis), usar la
  skill `vetplanet-pdf-reports`.
