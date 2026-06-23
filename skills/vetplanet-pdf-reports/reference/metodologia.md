# Metodología para la Elaboración de Informes y Reportes Clínicos
## Clínica Veterinaria Vet Planet · Modelo de Trabajo Asistido

> **Propósito de este documento.** Este archivo define el modelo de trabajo que se utiliza para producir los informes clínicos, reportes de consulta y documentos de la clínica de forma profesional, estructurada y respaldada en evidencia. Sirve como guía de referencia (playbook) para replicar el mismo nivel de análisis y presentación en cualquier caso, tanto en documentos médico-a-médico como en informes dirigidos al propietario. Es complementario al prompt maestro del módulo **DR IA** del proyecto Nex Vet.

---

## 1. Tipos de documentos que produce este modelo

El modelo genera cuatro grandes tipos de entregables. Cada uno tiene una audiencia, un tono y una estructura distinta.

| Documento | Audiencia | Tono | Uso |
|---|---|---|---|
| **Informe clínico de discusión** | Médico tratante / especialistas | Técnico, médico-a-médico | Debate diagnóstico de alto nivel, casos complejos |
| **Epicrisis clínica** | Expediente / médico-legal | Formal, documental | Cierre de caso, desenlace, documento médico-legal |
| **Informe de control** | Propietario (revisado con el médico) | Formal pero accesible | Seguimiento, controles de rutina, comunicación al cliente |
| **Especificación de módulo / prompt** | Equipo de desarrollo | Técnico-funcional | Documentación del sistema DR IA / Nex Vet |

La regla central: **el médico y el propietario necesitan documentos distintos**. No se entrega el mismo informe a ambos. El técnico lleva terminología, tablas de laboratorio y referencias; el del propietario lleva lenguaje claro, foco en calidad de vida y decisiones concretas.

---

## 2. Flujo de trabajo (metodología de análisis)

Este es el corazón del modelo. El orden no es opcional: cada paso alimenta al siguiente.

### 2.1 Ingestión por fases

La información de los casos llega en fases, no toda de golpe. El modelo acumula contexto y **no produce un análisis diagnóstico hasta recibir la señal de inicio** (explícita: "ya puedes analizar"; o implícita: una pregunta diagnóstica directa tras la última carga de datos).

- **Fase 0 — Contexto inicial:** reseña del paciente (especie, edad, sexo, peso, raza, propietario) y motivo de consulta.
- **Fase 1 — Exámenes basales:** hemograma, bioquímica, urianálisis, historia clínica, sintomatología.
- **Fase 2 — Seguimiento / nuevos datos:** exámenes comparativos, evolución, tratamientos administrados y respuesta.
- **Fase 3 — Imagenología:** ecografía (Modo B / Doppler), radiografía simple o con contraste.
- **Fase adicional — Post-diagnóstico:** biopsia/histopatología, nuevos controles, respuesta a tratamiento.

### 2.2 Secuencia de análisis (orden obligatorio)

1. **Urgencias primero.** Antes de cualquier discusión diagnóstica, identificar hallazgos que requieran acción inmediata (obstrucción total, azoemia crítica, deterioro multiorgánico). Si existen, se destacan al inicio del informe.
2. **Hilo clínico (síntesis).** La narrativa que une todos los datos en una historia coherente. Es el párrafo más importante.
3. **Cronología.** Tabla con fechas, eventos y hallazgos clave en orden temporal.
4. **Laboratorio comparativo.** Siempre en tabla si hay más de una fecha. Se analiza la **tendencia**, no solo el valor puntual.
5. **Imagenología.** Se lee en el contexto del cuadro clínico, nunca de forma aislada.
6. **Diagnósticos diferenciales.** Exactamente 3, jerarquizados.
7. **Opciones de manejo.** Exactamente 3.
8. **Próximos pasos.** Acciones priorizadas por urgencia.

---

## 3. Principios clínicos del modelo

Estos principios distinguen un análisis profesional de uno superficial.

- **Paciencia diagnóstica.** No se diagnostica de forma prematura. Se espera a tener el conjunto de datos.
- **Análisis comparativo en el tiempo.** Un valor dentro de rango que cambia rápidamente (ej. creatinina 1.46 → 1.88 → 2.25 en semanas) puede ser tan importante como un valor fuera de rango estable.
- **Interpretación por especie.** El mismo número puede significar lo opuesto según la especie. Ejemplo clave de esta sesión: una **densidad urinaria de 1.030** indica capacidad concentradora *preservada* en el perro, pero *inadecuada* en el gato (umbral felino: 1.035). Nunca aplicar umbrales caninos a felinos ni viceversa.
- **La imagen al servicio del clínico.** Los hallazgos imagenológicos se expresan como "compatible con" / "sugestivo de", nunca como certeza diagnóstica. Se declaran las limitaciones de la lectura digital.
- **Correlacionar entre paneles.** Hemograma, bioquímica y urianálisis se leen juntos. Buscar el patrón que los une y alertar sobre discordancias (ej. glucosuria con normoglucemia = disfunción tubular; bilirrubina elevada en muestra lipémica = probable artefacto).
- **Siempre un diferencial benigno.** Aunque sea el menos probable, incluir siempre una posibilidad benigna/tratable para evitar el sesgo de confirmación hacia el diagnóstico más grave.
- **Urgencia escalada.** Lo que pone en riesgo la vida se comunica primero.
- **Considerar el artefacto de laboratorio.** Las muestras lipémicas, hemolizadas o no en ayuno alteran valores. Identificar la interferencia antes de sobre-interpretar (ej. bilirrubina o colesterol en muestra lipémica).

---

## 4. Framework de diagnósticos diferenciales

**Regla: exactamente 3, ordenados por probabilidad descendente.**

Cada diferencial debe contener:

1. **Descripción** — qué es la entidad y su comportamiento típico.
2. **Argumentos a favor en este paciente** — los datos concretos del caso que lo sostienen.
3. **Argumentos en contra** — lo que habla en su contra (reduce el sesgo de confirmación).
4. **Implicación terapéutica** — cómo cambia el manejo si este es el diagnóstico real.

Codificación visual por prioridad en los PDF: rojo (máxima prioridad), naranja (alta), teal/verde (alternativa o benigno).

---

## 5. Framework de opciones de manejo

**Regla: exactamente 3 opciones, no mutuamente excluyentes.**

- **Opción 1 — siempre estabilización + diagnóstico definitivo + estadificación.** Antes de tratar, confirmar. Incluye derivación/estabilización del paciente, pruebas diagnósticas definitivas (biopsia sin sembrar, tests moleculares), y estadificación.
- **Opción 2 — manejo médico / conservador.** El protocolo médico de elección basado en evidencia si se confirma el diagnóstico más probable.
- **Opción 3 — intervencionista / quirúrgico.** Cuándo y por qué intervenir, técnicas, riesgos y beneficios.

Cada opción debe incluir:
- **Cifras de pronóstico reales** (supervivencia mediana, tasa de respuesta, % de complicación) para que el médico pueda conversar con el propietario.
- **Advertencias críticas en negrita** específicas para *ese* paciente (ej. "no iniciar AINE con azoemia activa").

---

## 6. Modos de especialista

El modelo activa el nivel de detalle técnico según el tipo de información recibida.

| Modo | Se activa con | Enfoque |
|---|---|---|
| **Internista (base)** | Siempre activo | Interpretación de hemograma y bioquímica, narrativa clínica, razonamiento bayesiano |
| **Radiólogo** | Imágenes (eco, Rx contraste) | Lectura por modalidad y órgano; prioriza Doppler color en masas; integra con clínica |
| **Oncólogo** | Sospecha neoplásica en el top 3 | Estadificación, tests moleculares, supervivencia, advertencias (ej. no FNA percutáneo en TCC) |
| **Nefrólogo / Urólogo** | Azoemia, hallazgos urinarios, obstrucción | Urianálisis completo, estadiaje IRIS, componente pre/renal/post-renal, fármacos nefrotóxicos |

---

## 7. Contenido a consultar (estándares y fuentes)

### 7.1 Journals de referencia

| Journal | Área principal |
|---|---|
| Journal of Veterinary Internal Medicine (JVIM) | Medicina interna, nefrología, urología, oncología |
| Journal of the American Veterinary Medical Association (JAVMA) | Medicina general, procedimientos, outcomes |
| Journal of Feline Medicine and Surgery (JFMS) | Medicina felina específica |
| Journal of Veterinary Emergency and Critical Care (JVECC) | Urgencias y cuidados intensivos |
| American Journal of Veterinary Research (AJVR) | Investigación clínica y diagnóstico |
| Veterinary Clinics of North America: Small Animal Practice | Revisiones por especialidad, guías |
| Veterinary Radiology & Ultrasound | Imagenología, protocolos de contraste |
| Frontiers in Veterinary Science | Revisiones sistemáticas, poblaciones grandes |

### 7.2 Guías y referencias de estadiaje

- **IRIS (International Renal Interest Society)** — estadiaje de enfermedad renal crónica:
  - Estadio 1: creatinina < 1.6 mg/dL (felino)
  - Estadio 2: creatinina 1.6 – 2.8 mg/dL
  - Estadio 3: creatinina 2.9 – 5.0 mg/dL
  - Estadio 4: creatinina > 5.0 mg/dL
  - Requiere **dos mediciones estables, en ayuno, paciente hidratado**, y exclusión de causas no renales.
  - Subestadiaje: UPC (proteinuria) y presión arterial.
- **SDMA** — marcador de función renal temprano. Se eleva con ~25% de pérdida de TFG (vs. ~75% de la creatinina). Umbral: ≤ 14 µg/dL normal; 14–19.9 sospechoso; ≥ 20 compatible con falla renal.
- **Umbrales de densidad urinaria por especie** — felino: concentración adecuada > 1.035; canino: > 1.030.

### 7.3 Estándar de citación de evidencia

- Cada cifra (supervivencia, tasa de respuesta, frecuencia de complicación) debe estar respaldada por una fuente.
- Citar con: tipo de estudio, tamaño de muestra (n) y hallazgo principal cuantificado.
- Preferir publicaciones de los últimos 5 años; citar la evidencia clásica cuando sea la más relevante.
- **No confabular referencias.** Si no hay evidencia específica, decirlo.

---

## 8. Estructura de cada documento

### 8.1 Informe clínico de discusión (médico-a-médico)

1. Portada — datos del paciente, fecha, advertencia metodológica.
2. Síntesis ejecutiva — hilo clínico y conclusión principal.
3. Hallazgos críticos — bloque destacado, va antes del resto.
4. Cronología — tabla.
5. Laboratorio comparativo — tablas con columna de tendencia.
6. Imagenología — por modalidad, con nota metodológica.
7. Diagnósticos diferenciales (×3) — bloques codificados por color.
8. Opciones de manejo (×3) — con cifras y advertencias.
9. Próximos pasos — tabla priorizada (crítica / alta / media).
10. Referencias — journals con datos del estudio.

### 8.2 Epicrisis clínica (médico-legal)

Estructura por secciones en numeración romana:
I. Resumen ejecutivo · II. Identificación del paciente y propietaria · III. Cronología clínica · IV. Motivo de consulta · V. Evaluación diagnóstica al ingreso (imagenología, hemograma, química) · VI. Primera intervención · VII. Segunda intervención · VIII. Evento adverso (si aplica) · IX. Maniobras de reanimación (si aplica) · X. Causa de muerte (si aplica) · XI. Evolución clínica y desenlace · XII. Firmas y validación.
Cierre con **aviso de confidencialidad médica** y conservación mínima del expediente (5 años, conforme al Colegio de Profesionales en Medicina Veterinaria de Costa Rica).

### 8.3 Informe de control (para propietario)

Versión sencilla, 1–2 páginas, con identidad visual de la clínica:
- Encabezado con logo + título + fecha.
- Ficha del paciente.
- Motivo de la consulta.
- Hallazgos de la valoración.
- Interpretación clínica (en lenguaje accesible).
- Plan de manejo recomendado (lista numerada).
- Conclusión destacada.
- Nota de uso clínico y datos de contacto.

---

## 9. Identidad visual y elementos de diseño (Vet Planet)

| Elemento | Especificación |
|---|---|
| **Teal principal** | `#1F6B6B` |
| **Teal oscuro (títulos)** | `#14524F` |
| **Teal de encabezados de tabla** | `#2E7D7A` |
| **Fondo suave** | `#E8F1F0` |
| **Dorado (etiquetas)** | `#A98B3D` |
| **Rojo vino (alertas / legal)** | `#7A1F1F` |
| **Verde (favorable)** | `#1E6B3A` |
| **Logo** | Logo Vet Planet (pata + planeta + perro) en el encabezado |
| **Marca de agua** | Logo atenuado (~6% opacidad) centrado en el fondo |
| **Tablas** | Encabezado teal, filas alternas, rejilla suave |
| **Pie de página** | Nombre de la clínica + Cartago, Costa Rica + Tel. 7143 3060 + correo + redes |
| **Correo oficial** | clinicaveterinaria@vetplanetcr.com |
| **Redes** | @clinicavetplanet |

Resaltado por color dentro de las tablas: dorado para el dato a vigilar, verde para el hallazgo tranquilizador/favorable, rojo/naranja para el crítico.

---

## 10. Tono y lenguaje según audiencia

### 10.1 Documento médico-a-médico
- Terminología técnica completa, sin condescendencia.
- Directo, de colega a colega.

### 10.2 Documento para el propietario
- **Tratar de usted** (es un reporte, no una conversación).
- Formal pero accesible; sin jerga innecesaria.
- Cuando un término requiere explicación, va en la misma línea entre paréntesis.
- Lenguaje natural costarricense de consultorio, que se sienta escrito por un veterinario.
- No infantilizar, no aterrorizar, no dar falsas esperanzas.
- Reencuadrar el motivo de forma correcta (ej. "seguimiento de condición urinaria geriátrica" en lugar de "seguimiento de la cirugía") cuando refleje mejor el estado actual del paciente.
- Usar el recurso de "luz amarilla / luz roja" u otras analogías para transmitir el nivel de preocupación sin alarmismo.

---

## 11. Disclaimers obligatorios

Deben aparecer (adaptados al tipo de documento):

- **Diagnóstico:** el diagnóstico definitivo requiere confirmación histopatológica / citológica / microbiológica según el caso.
- **Imagen:** las interpretaciones imagenológicas se basan en revisión de archivos digitales y tienen limitaciones inherentes; deben correlacionarse con la exploración directa del médico tratante.
- **Herramienta de apoyo:** el análisis es soporte a la decisión clínica y no reemplaza al médico veterinario tratante.
- **Evidencia:** las cifras de supervivencia y recomendaciones están basadas en la literatura disponible y pueden no aplicar a todos los pacientes individualmente.
- **Casos complejos / pacientes reales:** en decisiones finas (ej. manejo dietético en un paciente con doble condición), conviene contrastar con un especialista (nutricionista, nefrólogo).

---

## 12. Consideraciones especializadas recurrentes (memoria del modelo)

Puntos clínicos finos que han demostrado ser decisivos y conviene tener siempre presentes:

- **Conflicto dietético oxalato vs. renal.** Las dietas de prevención de oxalato de calcio (no acidificantes, fósforo normal, citrato, alta humedad) y las dietas renales (restringidas en fósforo y proteína) apuntan en direcciones opuestas. La restricción de fósforo y la acidificación favorecen el oxalato. El punto común que reconcilia ambos objetivos es la **hidratación**. En pacientes con doble condición, la dieta no puede ser de "talla única".
- **Dietas urinarias acidificantes en geriátricos.** Un alimento urinario alto en proteína y sodio y acidificante (pH 6.0–6.5) sirve para el control de cálculos, pero no es el perfil ideal para un riñón geriátrico con reserva disminuida. Reevaluar según evolución renal.
- **Parte de la azoemia puede ser dietética.** Un BUN en el límite alto en un paciente con dieta muy proteica puede tener componente dietético, no solo renal. Tenerlo en cuenta al interpretar el recheck.
- **Suplementos de soporte urinario** (ej. glicosaminoglicanos para la mucosa vesical) son benignos y compatibles con el manejo renal; pueden continuarse.
- **Macho entero y neoplasia urinaria.** En obstrucción del trígono/cuello vesical sin litiasis en un macho entero geriátrico, el carcinoma urotelial (TCC) y el carcinoma prostático son los diferenciales prioritarios; ambos comparten la mutación BRAF V595E (test molecular en orina, no afectado por hematuria).
- **Doppler color en masas vesicales.** La vascularización intralesional es el hallazgo imagenológico de mayor peso: distingue masa activa (neoplásica/proliferativa) de coágulo o sedimento (avasculares).

---

## 13. Checklist final antes de entregar un documento

- [ ] ¿El análisis siguió la secuencia obligatoria (urgencias → hilo → cronología → laboratorio → imagen → diferenciales → manejo → pasos)?
- [ ] ¿Las tablas de laboratorio muestran tendencia, no solo valor puntual?
- [ ] ¿Los umbrales usados son los de la especie correcta?
- [ ] ¿Hay exactamente 3 diferenciales, con uno benigno incluido?
- [ ] ¿Hay exactamente 3 opciones de manejo, con cifras y advertencias?
- [ ] ¿Las cifras están respaldadas por fuentes reales (sin referencias inventadas)?
- [ ] ¿El tono y el lenguaje corresponden a la audiencia (médico vs. propietario)?
- [ ] ¿Están los disclaimers correspondientes?
- [ ] ¿La identidad visual de Vet Planet es correcta (logo, colores, marca de agua, pie con correo oficial)?
- [ ] ¿El documento cierra correctamente en sus páginas (sin secciones cortadas)?

---

*Documento de uso interno · Clínica Veterinaria Vet Planet · Cartago, Costa Rica · Modelo de trabajo para informes y reportes clínicos. Complementario al prompt maestro del módulo DR IA (proyecto Nex Vet).*
