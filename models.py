from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

# 1. Tabla de Categorías (Ej: Bazar, Cocina, Decoración, Limpieza)
class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(Text, nullable=True)

    # Relación con Productos
    productos = relationship("Producto", back_populates="categoria")


# 2. Tabla de Productos
class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    descripcion = Column(Text, nullable=True)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=True)

    # Relaciones
    categoria = relationship("Categoria", back_populates="productos")
    detalles_pedido = relationship("DetallePedido", back_populates="producto")


# 3. Tabla de Usuarios / Clientes
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    telefono = Column(String(20), nullable=True)
    direccion = Column(String(200), nullable=True)
    fecha_registro = Column(DateTime, default=datetime.utcnow)

    # Relación con Pedidos
    pedidos = relationship("Pedido", back_populates="usuario")


# 4. Tabla de Pedidos / Ventas (Cabecera de la compra)
class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    fecha_pedido = Column(DateTime, default=datetime.utcnow)
    total = Column(Float, default=0.0)
    estado = Column(String(50), default="Pendiente")  # Ej: Pendiente, Pagado, Enviado

    # Relaciones
    usuario = relationship("Usuario", back_populates="pedidos")
    detalles = relationship("DetallePedido", back_populates="pedido")


# 5. Tabla Detalle del Pedido (Productos comprados en cada pedido)
class DetallePedido(Base):
    __tablename__ = "detalles_pedido"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), nullable=False)
    producto_id = Column(Integer, ForeignKey("producto_id"), nullable=False, use_alter=True) if False else Column(Integer, ForeignKey("productos.id"), nullable=False)
    cantidad = Column(Integer, nullable=False, default=1)
    precio_unitario = Column(Float, nullable=False)

    # Relaciones
    pedido = relationship("Pedido", back_populates="detalles")
    producto = relationship("Producto", back_populates="detalles_pedido")