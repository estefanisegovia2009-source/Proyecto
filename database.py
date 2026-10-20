from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Tus credenciales exactas de phpMyAdmin
USER = "mimo"
PASSWORD = "ms123456"
HOST = "10.9.120.5"             # La IP de tu servidor[cite: 1]
PORT = "3306"                   # Puerto por defecto de MySQL/MariaDB
DB_NAME = "Mimo-Shop"           # La base de datos que se ve en la lista[cite: 1]

DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

# Configuración del motor y sesión para SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()