import pandas as pd
import numpy as np

np.random.seed(42)

dataset_envios = pd.DataFrame({
    'ID_Pedido': [f'PED-{1000+i}' for i in range(500)],
    'Dias_Envio': np.random.randint(1, 10, size=500),
    'Costo_Envio_USD': np.round(np.random.uniform(5.0, 45.0, size=500), 2),
    'Calificacion_Cliente': np.random.randint(1, 6, size=500)
})