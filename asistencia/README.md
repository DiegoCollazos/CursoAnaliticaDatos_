# Registro de asistencia

El registro de asistencia se administra en un único archivo de Excel: **[`asistencia.xlsx`](asistencia.xlsx)**. El docente es quien lo diligencia; los estudiantes **no** necesitan una cuenta de GitHub para este proceso.

## Cómo usarlo

1. Descarga `asistencia.xlsx` desde GitHub (botón "Download raw file" ⬇️) y ábrelo en Excel, Google Sheets o LibreOffice.
2. En la pestaña **Asistencia**, cada sesión de clase es una columna. La columna `C` ("EJEMPLO") ya está diligenciada para mostrarte el formato.
3. Para cada sesión nueva, escribe la fecha en la fila 1 de la siguiente columna libre y, para cada estudiante, selecciona su estado con la lista desplegable: `P` = Presente, `A` = Ausente, `E` = Excusa.
4. La pestaña **Resumen** calcula automáticamente, por estudiante, el número de sesiones registradas, presentes, ausencias, excusas y el % de asistencia (ya lo tienes formulado, no hay que tocar nada ahí).
5. La pestaña **Estudiantes** contiene el listado oficial (documento, plan, correo); actualízala si hay novedades de matrícula.
6. La pestaña **Instrucciones** trae esta misma guía dentro del archivo.
7. Cuando termines de actualizarlo, sube el archivo de nuevo a esta carpeta en GitHub (arrastrándolo en la página del repositorio o con el botón "Add file → Upload files") para dejar el registro actualizado con control de versiones.

## Notas

- El % de asistencia cuenta `Presente` y `Excusa` como sesión atendida, y solo considera las columnas que ya tengan un estado marcado.
- Según la ficha oficial de la asignatura, se exige un mínimo de **85% de asistencia**.
