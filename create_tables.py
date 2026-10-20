from database import engine, Base
import models  # Importamos los modelos para que SQLAlchemy reconozca las tablas

print("Creando tablas en la base de datos...")

# Esta línea examina todos los modelos declarados y crea las tablas que no existan
Base.metadata.create_all(bind=engine)

print("¡Tablas creadas exitosamente!")