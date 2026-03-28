import pandas as pd
from database import SessionLocal
import models

ARCHIVO_EXCEL = "Chicos.xlsx"

df = pd.read_excel(ARCHIVO_EXCEL, engine="openpyxl")

db = SessionLocal()

for index, row in df.iterrows():
    nombre = row['NOMBRE']   # IMPORTANTE: que coincida la columna
    nuevo = models.Joven(
    nombre=nombre,
    puntos_totales=0,
    puntos_racha=0,
    racha_actual=0,
    racha_maxima=0
)
    db.add(nuevo)

db.commit()
db.close()

print("Carga completada")

