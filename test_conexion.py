from database import engine
from sqlalchemy import text

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT VERSION();"))
        for row in result:
            print(f"\n¡Conexión exitosa! Versión de la base de datos: {row[0]}\n")
except Exception as e:
    print(f"\nError al conectar a la base de datos: {e}\n")