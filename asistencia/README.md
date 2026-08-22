# Registro de asistencia

Esta carpeta contiene el registro de asistencia del curso, administrado por el docente directamente en el repositorio. Los estudiantes **no** necesitan una cuenta de GitHub para este proceso.

## Archivos

- **`estudiantes.csv`** — Listado (roster) de estudiantes matriculados. Actualízalo una vez al inicio del curso y cada vez que haya novedades (retiros, adiciones).
- **`registro_asistencia.csv`** — Registro histórico de asistencia, una fila por estudiante y sesión. Se va agregando después de cada clase.
- **`resumen_asistencia.py`** — Script en Python que calcula el porcentaje de asistencia de cada estudiante a partir de los dos archivos anteriores.

## Flujo de trabajo sugerido

1. Al iniciar el curso, completa `estudiantes.csv` con el listado oficial.
2. Después de cada sesión, abre `registro_asistencia.csv` desde GitHub (botón de lápiz ✏️ para editar en el navegador) y agrega una fila por cada estudiante con la fecha, el número de sesión y el estado (`Presente`, `Ausente`, `Excusa`).
   - También puedes editarlo localmente en Excel/Sheets y luego subir el archivo actualizado (commit).
3. Cuando quieras un resumen (por ejemplo, para reportar el % de asistencia), ejecuta:

   ```bash
   python asistencia/resumen_asistencia.py
   ```

   Esto imprime una tabla con el número de sesiones asistidas y el porcentaje de asistencia por estudiante, y guarda el resultado en `asistencia/resumen_asistencia.csv`.

## Formato de `registro_asistencia.csv`

| Columna | Descripción |
|---|---|
| `fecha` | Fecha de la sesión (AAAA-MM-DD) |
| `sesion` | Número de sesión/semana |
| `id_estudiante` | Identificador del estudiante (debe coincidir con `estudiantes.csv`) |
| `estado` | `Presente`, `Ausente` o `Excusa` |
| `observaciones` | Notas opcionales |
