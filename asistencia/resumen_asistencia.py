"""Calcula el porcentaje de asistencia por estudiante.

Lee `estudiantes.csv` y `registro_asistencia.csv` (en la misma carpeta),
y genera `resumen_asistencia.csv` con el conteo de sesiones registradas,
las presentes y el porcentaje de asistencia de cada estudiante.

Uso:
    python asistencia/resumen_asistencia.py
"""

from pathlib import Path

import pandas as pd

CARPETA = Path(__file__).parent
ESTADOS_ASISTIO = {"Presente", "Excusa"}


def main() -> None:
    estudiantes = pd.read_csv(CARPETA / "estudiantes.csv")
    registro = pd.read_csv(CARPETA / "registro_asistencia.csv")

    total_sesiones = registro["sesion"].nunique()

    registro["asistio"] = registro["estado"].isin(ESTADOS_ASISTIO)
    conteo = (
        registro.groupby("id_estudiante")
        .agg(sesiones_registradas=("sesion", "nunique"), sesiones_presente=("asistio", "sum"))
        .reset_index()
    )

    resumen = estudiantes.merge(conteo, on="id_estudiante", how="left").fillna(0)
    resumen["sesiones_registradas"] = resumen["sesiones_registradas"].astype(int)
    resumen["sesiones_presente"] = resumen["sesiones_presente"].astype(int)
    resumen["porcentaje_asistencia"] = (
        (resumen["sesiones_presente"] / total_sesiones * 100).round(1) if total_sesiones else 0.0
    )

    salida = resumen[
        ["id_estudiante", "nombre", "sesiones_presente", "sesiones_registradas", "porcentaje_asistencia"]
    ].sort_values("nombre")

    print(salida.to_string(index=False))
    salida.to_csv(CARPETA / "resumen_asistencia.csv", index=False)
    print(f"\nResumen guardado en {CARPETA / 'resumen_asistencia.csv'}")


if __name__ == "__main__":
    main()
