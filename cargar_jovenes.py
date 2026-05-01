import pandas as pd
from database import SessionLocal,engine
import models
models.Base.metadata.create_all(bind=engine)
ARCHIVO_EXCEL = "Chicos.xlsx"
models.Base.metadata.create_all(bind=engine)
df = pd.read_excel(ARCHIVO_EXCEL, engine="openpyxl")

db = SessionLocal()

#  convierte TODO el excel en una sola lista
nombres = df.values.flatten()

for nombre in nombres:
    if pd.notna(nombre):
        nombre = str(nombre).strip().title()

        existe = db.query(models.Joven).filter(models.Joven.nombre == nombre).first()

        if not existe:
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

print("Carga completa")

