from database import SessionLocal
from models import Categoria, Producto

db = SessionLocal()

try:
    print("Insertando categorías...")

    # 1. Crear Categorías de Bazar
    cat_cocina = Categoria(nombre="Cocina", descripcion="Artículos y utensilios para la cocina")
    cat_hogar = Categoria(nombre="Hogar y Decoración", descripcion="Accesorios y adornos para el hogar")
    cat_limpieza = Categoria(nombre="Limpieza y Organizadores", descripcion="Productos de organización y aseo")

    db.add_all([cat_cocina, cat_hogar, cat_limpieza])
    db.commit()

    print("Categorías creadas correctamente. Insertando 15 productos...")

    # 2. Lista de 15 productos de bazar
    productos_bazar = [
        # --- Cocina ---
        Producto(nombre="Sartén Antiadherente 24cm", descripcion="Sartén de aluminio con teflón", precio=18.50, stock=20, categoria_id=cat_cocina.id),
        Producto(nombre="Set de 6 Vasos de Vidrio", descripcion="Vasos transparentes de 350ml", precio=12.00, stock=15, categoria_id=cat_cocina.id),
        Producto(nombre="Juego de Cubiertos 24 piezas", descripcion="Acero inoxidable calidad premium", precio=25.99, stock=10, categoria_id=cat_cocina.id),
        Producto(nombre="Tabla para Picar de Bambú", descripcion="Tabla ecológica para verduras y carnes", precio=8.50, stock=30, categoria_id=cat_cocina.id),
        Producto(nombre="Cafetera de Embolo 800ml", descripcion="Cafetera prensa francesa de vidrio templado", precio=16.00, stock=12, categoria_id=cat_cocina.id),
        
        # --- Hogar y Decoración ---
        Producto(nombre="Lámpara LED de Mesa", descripcion="Lámpara táctil recargable USB", precio=22.00, stock=8, categoria_id=cat_hogar.id),
        Producto(nombre="Set de 3 Velas Aromáticas", descripcion="Velas de cera de soya fragancia lavanda", precio=14.50, stock=25, categoria_id=cat_hogar.id),
        Producto(nombre="Cojín Decorativo 45x45", descripcion="Cojín de algodón textura suave", precio=9.99, stock=18, categoria_id=cat_hogar.id),
        Producto(nombre="Florero de Cerámica Blanco", descripcion="Florero moderno estilo nórdico", precio=11.20, stock=14, categoria_id=cat_hogar.id),
        Producto(nombre="Reloj de Pared Minimalista", descripcion="Reloj silencioso de 30cm de diámetro", precio=15.00, stock=10, categoria_id=cat_hogar.id),

        # --- Limpieza y Organizadores ---
        Producto(nombre="Organizador de Plástico Multiuso", descripcion="Caja organizadora apilable transparente", precio=6.50, stock=40, categoria_id=cat_limpieza.id),
        Producto(nombre="Cesto de Ropa Plegable", descripcion="Cesto de tela impermeable 50L", precio=13.80, stock=15, categoria_id=cat_limpieza.id),
        Producto(nombre="Dispenser de Jabón Líquido", descripcion="Dosificador de cerámica para baño/cocina", precio=7.90, stock=22, categoria_id=cat_limpieza.id),
        Producto(nombre="Espejo de Aumento para Baño", descripcion="Espejo con luz LED y soporte giratorio", precio=19.50, stock=9, categoria_id=cat_limpieza.id),
        Producto(nombre="Set de 5 Perchas Antideslizantes", descripcion="Perchas de terciopelo ahorradoras de espacio", precio=5.00, stock=50, categoria_id=cat_limpieza.id)
    ]

    # Guardar productos en la base de datos
    db.add_all(productos_bazar)
    db.commit()

    print("¡15 productos insertados exitosamente en la base de datos!")

except Exception as e:
    db.rollback()
    print(f"Error al insertar datos: {e}")

finally:
    db.close()