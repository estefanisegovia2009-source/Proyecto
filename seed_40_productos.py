from database import SessionLocal
from models import Categoria, Producto

db = SessionLocal()

try:
    print("Verificando categorías...")

    # Crear o recuperar categorías
    def get_or_create_cat(nombre, descripcion):
        cat = db.query(Categoria).filter_by(nombre=nombre).first()
        if not cat:
            cat = Categoria(nombre=nombre, descripcion=descripcion)
            db.add(cat)
            db.commit()
            db.refresh(cat)
        return cat

    cat_cocina = get_or_create_cat("Cocina y Bazar", "Utensilios, ollas, vajilla y accesorios de cocina")
    cat_hogar = get_or_create_cat("Hogar y Decoración", "Artículos de decoración, iluminación y confort")
    cat_organizadores = get_or_create_cat("Organización y Limpieza", "Cajas, cestos, contenedores y accesorios")
    cat_bano = get_or_create_cat("Baño y Cuidado Personal", "Accesorios para baño y aseo personal")
    cat_mesa = get_or_create_cat("Mesa y Cristalería", "Copas, vasos, platos y mantelería")

    print("Insertando 40 productos de bazar...")

    productos_40 = [
        # --- Cocina y Bazar (10 productos) ---
        Producto(nombre="Sartén Antiadherente 24cm", descripcion="Aluminio con teflón reforzado", precio=18.50, stock=20, categoria_id=cat_cocina.id),
        Producto(nombre="Juego de Cubiertos 24 Piezas", descripcion="Acero inoxidable calidad premium", precio=25.99, stock=15, categoria_id=cat_cocina.id),
        Producto(nombre="Tabla para Picar de Bambú", descripcion="Tabla ecológica para verduras y carnes", precio=8.50, stock=30, categoria_id=cat_cocina.id),
        Producto(nombre="Cafetera de Émbolo 800ml", descripcion="Prensa francesa de vidrio templado", precio=16.00, stock=12, categoria_id=cat_cocina.id),
        Producto(nombre="Olla a Presión 5 Litros", descripcion="Acero inoxidable con válvula de seguridad", precio=45.00, stock=8, categoria_id=cat_cocina.id),
        Producto(nombre="Pelador de Verduras Cerámico", descripcion="Mango ergonómico hoja ultra afilada", precio=3.50, stock=50, categoria_id=cat_cocina.id),
        Producto(nombre="Balanza Digital de Cocina", descripcion="Precisión de 1g hasta 5kg con pantalla LCD", precio=12.90, stock=25, categoria_id=cat_cocina.id),
        Producto(nombre="Set de 3 Moldes de Silicona", descripcion="Aptos para horno y congelador", precio=14.00, stock=18, categoria_id=cat_cocina.id),
        Producto(nombre="Esptula de Silicona Termoresistente", descripcion="Resiste hasta 230°C", precio=4.20, stock=40, categoria_id=cat_cocina.id),
        Producto(nombre="Tostadora Eléctrica 2 Panes", descripcion="6 niveles de tostado en acero inoxidable", precio=28.50, stock=10, categoria_id=cat_cocina.id),

        # --- Hogar y Decoración (10 productos) ---
        Producto(nombre="Lámpara LED de Mesa Táctil", descripcion="Luz cálida recargable por USB", precio=22.00, stock=14, categoria_id=cat_hogar.id),
        Producto(nombre="Set de 3 Velas Aromáticas", descripcion="Cera de soya fragancia lavanda y vainilla", precio=14.50, stock=30, categoria_id=cat_hogar.id),
        Producto(nombre="Cojín Decorativo 45x45cm", descripcion="Fundas lavables textura suave", precio=9.99, stock=22, categoria_id=cat_hogar.id),
        Producto(nombre="Florero de Cerámica Blanco", descripcion="Diseño nórdico minimalista", precio=11.20, stock=16, categoria_id=cat_hogar.id),
        Producto(nombre="Reloj de Pared Silencioso 30cm", descripcion="Mecanismo continuo sin tic-tac", precio=15.00, stock=12, categoria_id=cat_hogar.id),
        Producto(nombre="Espejo Circular Marco Dorado 40cm", descripcion="Para colgar en sala o vestíbulo", precio=29.90, stock=7, categoria_id=cat_hogar.id),
        Producto(nombre="Camino de Mesa Tejido 180cm", descripcion="Algodón estilo rústico", precio=13.40, stock=20, categoria_id=cat_hogar.id),
        Producto(nombre="Portarretratos Múltiple 4 fotos", descripcion="Madera natural estilo collage", precio=10.50, stock=25, categoria_id=cat_hogar.id),
        Producto(nombre="Humidificador y Difusor de Aroma", descripcion="Ultrasónico con luz RGB 300ml", precio=21.00, stock=15, categoria_id=cat_hogar.id),
        Producto(nombre="Manta Tejida para Sofá", descripcion="Acrílico súper suave 130x160cm", precio=24.00, stock=9, categoria_id=cat_hogar.id),

        # --- Organización y Limpieza (8 productos) ---
        Producto(nombre="Caja Organizadora Apilable 15L", descripcion="Plástico transparente con traba", precio=7.50, stock=35, categoria_id=cat_organizadores.id),
        Producto(nombre="Cesto de Ropa Plegable 50L", descripcion="Tela de lino impermeable", precio=13.80, stock=18, categoria_id=cat_organizadores.id),
        Producto(nombre="Set de 10 Perchas de Terciopelo", descripcion="Antideslizantes ahorran espacio", precio=9.00, stock=45, categoria_id=cat_organizadores.id),
        Producto(nombre="Organizador de Calzado Bajo Cama", descripcion="Capacidad para 12 pares con cierre", precio=11.50, stock=20, categoria_id=cat_organizadores.id),
        Producto(nombre="Mop Limpiador Giratorio 360", descripcion="Incluye balde con escurridor y 2 paños", precio=26.00, stock=11, categoria_id=cat_organizadores.id),
        Producto(nombre="Organizador de Escritorio de Malla", descripcion="5 compartimentos para papelería", precio=8.90, stock=28, categoria_id=cat_organizadores.id),
        Producto(nombre="Especiero Giratorio 12 Frascos", descripcion="Acero inoxidable frascos de vidrio", precio=23.50, stock=10, categoria_id=cat_organizadores.id),
        Producto(nombre="Frasco Hermético de Vidrio 1.5L", descripcion="Tapa de bambú con silicona", precio=6.80, stock=30, categoria_id=cat_organizadores.id),

        # --- Baño y Cuidado Personal (6 productos) ---
        Producto(nombre="Dispenser de Jabón Cerámico", descripcion="Diseño elegante con bomba plateada", precio=7.90, stock=22, categoria_id=cat_bano.id),
        Producto(nombre="Espejo con Luz LED y Aumento 5x", descripcion="Soporte giratorio táctil", precio=19.50, stock=13, categoria_id=cat_bano.id),
        Producto(nombre="Set de 3 Toallas de Algodón 500g", descripcion="Súper absorbentes 1 mano, 1 rostro, 1 baño", precio=22.00, stock=15, categoria_id=cat_bano.id),
        Producto(nombre="Jabonera de Bambú con Drenaje", descripcion="Resistente al agua y moho", precio=3.80, stock=50, categoria_id=cat_bano.id),
        Producto(nombre="Cortina de Ducha Impermeable", descripcion="Peva ecológico incluye 12 ganchos", precio=8.50, stock=25, categoria_id=cat_bano.id),
        Producto(nombre="Alfombra de Baño Antideslizante", descripcion="Microfibra Ultra Absorbente 50x80cm", precio=10.90, stock=19, categoria_id=cat_bano.id),

        # --- Mesa y Cristalería (6 productos) ---
        Producto(nombre="Set de 6 Vasos de Vidrio 350ml", descripcion="Vidrio labrado transparente", precio=12.00, stock=20, categoria_id=cat_mesa.id),
        Producto(nombre="Set de 4 Copas de Vino 450ml", descripcion="Cristal sin plomo para vino tinto", precio=18.90, stock=14, categoria_id=cat_mesa.id),
        Producto(nombre="Juego de Platos Playos 6 Piezas", descripcion="Losa blanca apta para microondas", precio=27.50, stock=12, categoria_id=cat_mesa.id),
        Producto(nombre="Jarra de Vidrio con Tapa 1.8L", descripcion="Resistente al calor y frío", precio=11.00, stock=16, categoria_id=cat_mesa.id),
        Producto(nombre="Set de 4 Tazas Mugs de Cerámica", descripcion="Capacidad 330ml colores pasteles", precio=14.20, stock=22, categoria_id=cat_mesa.id),
        Producto(nombre="Ensaladera de Vidrio Templado 26cm", descripcion="Ideal para ensaladas y postres", precio=9.50, stock=18, categoria_id=cat_mesa.id)
    ]

    db.add_all(productos_40)
    db.commit()

    print("¡40 productos de bazar insertados exitosamente en la base de datos!")

except Exception as e:
    db.rollback()
    print(f"Error al cargar productos: {e}")

finally:
    db.close()