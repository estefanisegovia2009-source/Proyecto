from database import SessionLocal
from models import Producto, Usuario

# Abrimos una sesión de trabajo con la base de datos
db = SessionLocal()

try:
    # 1. Crear un producto de prueba
    nuevo_producto = Producto(
        nombre="Zapatillas Deportivas",
        descripcion="Zapatillas cómodas para correr",
        precio=49.99,
        stock=15
    )

    # 2. Agregar el producto a la sesión y guardar cambios
    db.add(nuevo_producto)
    db.commit() # Guarda los datos en phpMyAdmin
    db.refresh(nuevo_producto) # Recibe el ID generado

    print(f"¡Producto creado exitosamente! ID: {nuevo_producto.id} - Nombre: {nuevo_producto.nombre}")

except Exception as e:
    db.rollback() # Si hay un error, revierte los cambios
    print(f"Error al agregar producto: {e}")

finally:
    db.close() # Siempre cerramos la sesión