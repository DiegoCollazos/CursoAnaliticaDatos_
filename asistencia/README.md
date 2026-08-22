# Registro de asistencia

El registro de asistencia se administra con una página web. Permite ver la asistencia, agregar o eliminar estudiantes y consultar el resumen con solo hacer clic, y guarda los cambios directamente en este repositorio. Los estudiantes **no** necesitan una cuenta de GitHub; solo la usa el docente.

### 👉 [Abrir la página de asistencia](https://diegocollazos.github.io/CursoAnaliticaDatos_/asistencia/asistencia.html)

(Publicada con GitHub Pages. También puedes abrir el archivo [`asistencia.html`](asistencia.html) localmente en tu navegador si lo prefieres.)

## Cómo usarla

1. Abre la [página de asistencia](https://diegocollazos.github.io/CursoAnaliticaDatos_/asistencia/asistencia.html) (o el archivo [`asistencia.html`](asistencia.html) localmente).
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

## Publicación con GitHub Pages

La página está publicada con GitHub Pages (Settings → Pages, rama `main`, carpeta `/ (root)`) en:

**https://diegocollazos.github.io/CursoAnaliticaDatos_/asistencia/asistencia.html**

## Notas

- El % de asistencia cuenta `Presente` y `Excusa` como sesión atendida.
- Según la ficha oficial de la asignatura, se exige un mínimo de **85% de asistencia**.
- Si trabajas desde varios computadores, debes configurar el token en cada uno (queda guardado por navegador, no viaja con el repositorio).
