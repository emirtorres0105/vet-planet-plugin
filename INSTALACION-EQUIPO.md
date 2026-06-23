# Instalación para el equipo — Plugin Vet Planet

Guía para que cada médico instale el asistente clínico de Vet Planet en su
sesión de **Claude Cowork**.

---

## Requisitos previos (una sola vez)

En tu sesión de Claude, verificá que estén activos:

- **Ejecución de código** (Settings → Capabilities). Sin esto, el motor de PDF
  no corre.
- **Búsqueda web**. Sin esto, Claude no puede verificar dosis ni consultar
  journals.

---

## Instalar el plugin (desde GitHub)

1. Abrí **Customize** en la barra lateral → pestaña **Plugins**.
2. En *Personal plugins*, tocá **"+"** → **Add marketplace**.
3. Pegá la URL del repositorio del plugin (te la comparte la clínica). Como el
   repositorio es **privado**, necesitás haber aceptado la invitación de
   colaborador en GitHub y tener tu cuenta de GitHub conectada.
4. Una vez agregado el marketplace, buscá el plugin **vet-planet** e instalalo.
5. Dejalo **habilitado**.

> Si el repositorio es privado y no carga, confirmá que aceptaste la invitación
> de GitHub y que tu cuenta está vinculada.

---

## Cómo se usa

- **Lenguaje natural:** *"informe de control para [paciente]"*, *"analicemos
  este caso, te paso los exámenes"*, *"¿qué dosis de metronidazol para 5.6 kg?"*.
  Las skills se activan solas.
- **Comandos rápidos:** `/informe-control`, `/informe-medico`, `/epicrisis`,
  `/dosis`.

---

## Qué información usa Claude para el apoyo diagnóstico

1. **Lo que cargás en el caso** (exámenes, imágenes, reseña) — fuente principal.
2. **Búsqueda web en tiempo real** — dosis, cifras de pronóstico y referencias
   de journals; lee fuentes públicas en el momento (no tiene bases de pago).
3. **La metodología del plugin** — estructura, umbrales por especie, reglas de
   dosificación y formato de los informes.
4. **El conocimiento general de Claude** — con fecha de corte; por eso toda
   cifra/dosis se verifica con búsqueda web antes de usarla.

**Límites a tener presentes:** no accede al expediente de la clínica ni a bases
veterinarias de suscripción; las lecturas de imagen son de apoyo ("compatible
con / sugestivo de") y no reemplazan la valoración directa; es **soporte a la
decisión**, no diagnóstico definitivo — el médico tratante valida y ajusta todo.

---

*Clínica Veterinaria Vet Planet · Cartago, Costa Rica · clinicaveterinaria@vetplanetcr.com*
