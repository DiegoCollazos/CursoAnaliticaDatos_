# Registro de asistencia

El registro de asistencia se administra con una página web: **[`asistencia.html`](asistencia.html)**. Permite ver la asistencia, agregar o eliminar estudiantes y consultar el resumen con solo hacer clic, y guarda los cambios directamente en este repositorio. Los estudiantes **no** necesitan una cuenta de GitHub; solo la usa el docente.

## Cómo usarla

1. Abre [`asistencia.html`](asistencia.html) (puedes descargarla y abrirla localmente en el navegador, o publicarla con GitHub Pages para tener un enlace fijo — ver más abajo).
2. La primera vez, despliega **⚙️ Configuración de GitHub** y pega un *Personal Access Token* de GitHub:
   - Ve a **GitHub → Settings (de tu perfil) → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**.
   - Limita el token a este repositorio (`CursoAnaliticaDatos_`) con permiso **Contents: Read and write**.
   - Pega el token en la página y haz clic en **Guardar configuración**. Queda guardado solo en tu navegador (no se envía a ningún otro sitio); trátalo como una contraseña y no lo compartas.
3. Haz clic en **Cargar datos desde GitHub** para traer el registro actual.
4. Pestaña **Asistencia**: haz clic en **+ Nueva sesión** para agregar la fecha de una clase, y haz clic sobre cada celda del estudiante para ir marcando su estado (en blanco → `P` Presente → `A` Ausente → `E` Excusa → en blanco).
5. Pestaña **Estudiantes**: agrega o elimina estudiantes del listado.
6. Pestaña **Resumen**: muestra automáticamente sesiones registradas, presentes, ausencias, excusas y el % de asistencia de cada estudiante (con el mínimo del 85% resaltado).
7. Cuando termines, haz clic en **💾 Guardar cambios en GitHub** (barra inferior) para dejar el registro actualizado en el repositorio, con historial de cambios incluido.

Los datos se guardan en [`datos.json`](datos.json), un archivo plano versionado en Git — puedes revisarlo o editarlo a mano si lo necesitas.

## Publicar con GitHub Pages (opcional, recomendado)

Para tener un enlace fijo (sin descargar el archivo cada vez): ve a **Settings → Pages** en este repositorio, en "Source" elige la rama `main` y carpeta `/ (root)`, y guarda. Unos minutos después la página quedará disponible en algo como:

`https://diegocollazos.github.io/CursoAnaliticaDatos_/asistencia/asistencia.html`

## Notas

- El % de asistencia cuenta `Presente` y `Excusa` como sesión atendida.
- Según la ficha oficial de la asignatura, se exige un mínimo de **85% de asistencia**.
- Si trabajas desde varios computadores, debes configurar el token en cada uno (queda guardado por navegador, no viaja con el repositorio).
