# modulos/compartido.py
import os
import pandas as pd

# Construye la ruta a tu CSV
ruta_base = os.path.dirname(__file__)
ruta_csv = os.path.join(ruta_base, "..", "data.csv")

# Carga el DataFrame al importar el módulo
df = pd.read_csv("../data.csv")