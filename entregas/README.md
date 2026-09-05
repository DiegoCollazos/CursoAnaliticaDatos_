# Entrega de trabajos

Los estudiantes suben sus entregables (laboratorios, proyecto integrador, etc.) con una página web: **[`entregas.html`](entregas.html)**. No requiere usar `git` ni la línea de comandos: se elige la categoría de la entrega, se escriben los apellidos del equipo, se seleccionan los archivos y la página los sube directamente a GitHub.

### 👉 [Abrir la página de entregas](https://diegocollazos.github.io/CursoAnaliticaDatos_/entregas/entregas.html)

(Publicada con GitHub Pages, igual que la página de asistencia. También puedes abrir el archivo [`entregas.html`](entregas.html) localmente en tu navegador.)

## Cómo funciona

La entrega **no se escribe directamente en `main`**. La página:

1. Crea una rama nueva solo para esa entrega (una por cada combinación de categoría + apellidos, p. ej. `entrega/laboratorio-de-simulacion-1/perez-gomez`).
2. Sube ahí los archivos seleccionados.
3. Abre un **Pull Request** hacia `main` para que el docente lo revise.
4. Si el mismo equipo vuelve a subir archivos para la misma entrega (por ejemplo, para corregir algo antes de la fecha límite), los agrega al **mismo** Pull Request en vez de crear uno nuevo — y si un archivo ya existía, lo actualiza.

De esta forma ningún estudiante puede escribir directamente sobre el contenido del curso: todo pasa por un Pull Request que tú revisas y fusionas (o pides ajustar) antes de que quede en `main`.

## Cómo usarla (para los estudiantes)

1. Abre la [página de entregas](https://diegocollazos.github.io/CursoAnaliticaDatos_/entregas/entregas.html).
2. La primera vez, despliega **⚙️ Configuración de GitHub** y crea tu propio *Personal Access Token*:
   - **GitHub → Settings (de tu perfil) → Developer settings → Personal access tokens → Tokens (classic) → Generate new token (classic)**.
   - Marca el permiso **repo** (acceso completo a repositorios).
   - ⚠️ **Debe ser un token clásico ("classic"), no un "fine-grained token"** — como este repositorio es de una cuenta personal (no una organización), los fine-grained tokens de un colaborador nunca van a poder verlo como "Resource owner", así que jamás van a funcionar aquí. Este es un límite conocido de GitHub, no un error de configuración.
   - Pega el token en la página y haz clic en **Guardar configuración**. Queda guardado solo en tu navegador; trátalo como una contraseña y no lo compartas.
3. Elige qué estás entregando, escribe los apellidos del equipo, selecciona el o los archivos, y haz clic en **Subir entrega y crear Pull Request**.
4. Guarda el enlace al Pull Request que te muestra la página — ahí puedes ver el estado de tu entrega y agregar comentarios si el docente te pide algo.

## Notas para el docente

- Cada entrega llega como un Pull Request individual, fácil de revisar en la pestaña **Pull requests** del repositorio.
- Los archivos quedan organizados en `entregas/<categoría>/<apellidos>/`.

### ⚠️ Paso obligatorio: agregar a cada estudiante como colaborador

Para que el token de un estudiante pueda crear una rama y un Pull Request, GitHub exige que esa persona tenga permiso de **escritura sobre el repositorio** — no existe una forma de darle permiso de escritura *solo* sobre la carpeta `entregas/`. Por eso, antes de compartir esta página con el curso:

1. Ve a **Settings → Collaborators** en este repositorio.
2. Agrega a cada estudiante (por su usuario o correo de GitHub) con rol **Write**.
3. Cada estudiante debe aceptar la invitación (le llega por correo o aparece en su cuenta de GitHub) antes de poder usar la página.

El flujo de rama + Pull Request de esta página existe justamente para que, aun con ese permiso de escritura, ningún estudiante pueda modificar `main` directamente sin que tú lo revises y apruebes primero — pero **si prefieres no dar permiso de escritura a los estudiantes**, la alternativa es el flujo clásico de GitHub (fork del repositorio + Pull Request), que no requiere agregarlos como colaboradores; avísame si en algún momento quieres cambiar a ese modelo.

### 🩹 Error 403 al subir ("no se pudo crear la rama")

La página ahora verifica el permiso de escritura *antes* de intentar nada (llamando a la API de GitHub) y muestra un mensaje específico en vez de solo "403". Causas posibles, en este orden de probabilidad:

1. **El estudiante generó un token "fine-grained" en vez de un token clásico.** Este es la causa más común y **un límite real de GitHub, no un error de configuración**: al crear un fine-grained token, el campo "Resource owner" solo permite elegir la propia cuenta del estudiante o una organización a la que pertenezca — nunca la cuenta de otra persona (como `DiegoCollazos`), aunque el estudiante ya sea colaborador aceptado. Por eso, si a un estudiante "no le aparece DiegoCollazos en Resource owner, solo su usuario", es totalmente normal y esperado con un fine-grained token: **no hay ninguna forma de arreglar eso, el estudiante tiene que usar un token clásico (classic) con el permiso `repo`** (ver instrucciones arriba). Más detalle en la [discusión de la comunidad de GitHub sobre este límite](https://github.com/orgs/community/discussions/53641).
2. **La invitación de colaborador sigue pendiente** (no la ha aceptado, aunque ya se le haya agregado). El estudiante debe revisar su correo o `https://github.com/DiegoCollazos/CursoAnaliticaDatos_/invitations` y aceptar.
3. El token clásico no tiene marcado el permiso **repo**, o se generó antes de aceptar la invitación (en ese caso, genera uno nuevo después de aceptar).

Si un estudiante ya aceptó la invitación (aparece en Settings → Collaborators con rol Write), ya generó un token **clásico** con permiso `repo` después de aceptar, y el error persiste, revisa si el repositorio tiene alguna regla de protección de rama (Settings → Rules/Branches) que esté bloqueando la creación de ramas `entrega/*`.
