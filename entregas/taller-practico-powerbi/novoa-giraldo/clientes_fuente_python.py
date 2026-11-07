# Fuente C: clientes simulados para el taller de Power BI
# Power BI detecta los DataFrame creados en el script.
import pandas as pd
import numpy as np

rng = np.random.default_rng(2026)
n = 120
clientes = pd.DataFrame({
    "ID_Cliente": [f"C{i:04d}" for i in range(1, n + 1)],
    "Ciudad": rng.choice(
        ["Manizales", "Bogotá", "Medellín", "Cali", "Pereira"],
        size=n,
        p=[0.30, 0.25, 0.20, 0.15, 0.10],
    ),
    "Segmento": rng.choice(
        ["Minorista", "Frecuente", "Corporativo"],
        size=n,
        p=[0.55, 0.30, 0.15],
    ),
    "Edad": rng.integers(18, 66, size=n),
})
