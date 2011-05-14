# -*- coding: utf-8 -*-


from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode
#from sqlalchemy.orm import relation, backref

from sgs.model import DeclarativeBase, metadata, DBSession
__all__ = ['Usuario','Permiso','Proyecto','Fase','TipoItem','Item','LineaBase','Relacion','VersionadoItem','ArchivosExternos','Historico','Rol','DetalleTipoItem','DetalleItem','DetalleVersionadoItem']


class Usuario(DeclarativeBase):
    __tablename__ = 'usuario'
    
    #{ Columns
    
    id_usuario = Column(Integer, autoincrement=True, primary_key=True)
    
    cod_usuario = Column(Unicode(20), unique=True, nullable=False)

    nombre_usuario = Column(Unicode(20))
    
    contrasena = Column(Unicode(16), nullable=False)

    nombre = Column(Unicode(20), nullable=False)

    apellido = Column(Unicode(20), nullable=False)

    fecha_nacimiento = Column(DateTime)

    genero = Column(Unicode(1))
    
    
    #}



class Proyecto(DeclarativeBase):
    __tablename__ = 'proyecto'
    
    #{ Columns
    
    id_proyecto = Column(Integer, autoincrement=True, primary_key=True)
      
    cod_proyecto = Column(Unicode(10), unique=True, nullable=False)

    nombre_proyecto = Column(Unicode(20), nullable=False)
    
    descripcion = Column(Unicode(100))

    fecha_inicio = Column(DateTime)
    
    #}


class Fase(DeclarativeBase):
    __tablename__ = 'fase'
    
    #{ Columns
    
    id_fase = Column(Integer, autoincrement=True, primary_key=True)

    cod_fase = Column(Unicode(10), unique=True, nullable=False)

    nombre_fase = Column(Unicode(20), nullable=False)
    
    descripcion = Column(Unicode(100))

    #}



class TipoItem(DeclarativeBase):
    __tablename__ = 'tipo_item'
    
    #{ Columns
    
    id_tipoitem = Column(Integer, autoincrement=True, primary_key=True)
    
    cod_tipoitem = Column(Unicode(10), unique=True, nullable=False)
    
    nombre_tipoitem = Column(Unicode(20), nullable=False)
    
    descripcion = Column(Unicode(100))

    fase = Column(Unicode(10), nullable=False)
    
    #}


class Item(DeclarativeBase):
    __tablename__ = 'item'
    
    #{ Columns
    
    id_item = Column(Integer, autoincrement=True, primary_key=True)

    cod_item = Column(Unicode(10), unique=True, nullable=False)
    
    nombre_item = Column(Unicode(20), nullable=False)
    
    descripcion = Column(Unicode(100))

    version = Column(Integer, nullable=False)

    estado = Column(Unicode(10), nullable=False)

    complejidad = Column(Integer, nullable=False)
    
    #}



class LineaBase(DeclarativeBase):
    __tablename__ = 'linea_base'
    
    #{ Columns
    
    id_lb = Column(Integer, autoincrement=True, primary_key=True)

    cod_lb = Column(Unicode(10), unique=True, nullable=False)
    
    fase = Column(Unicode(10), nullable=False)
    
    estado = Column(Unicode(10), nullable=False)

    #}



class Relacion(DeclarativeBase):
    __tablename__ = 'relacion'
    
    #{ Columns
    
    id_relacion = Column(Integer, autoincrement=True, primary_key=True)

    cod_relacion = Column(Unicode(10), unique=True, nullable=False)
    
    descripcion = Column(Unicode(100))

    tiporelacion = Column(Unicode(10), nullable=False)

    #}


class VersionadoItem(DeclarativeBase):
    __tablename__ = 'versionado_item'
    
    #{ Columns
    
    id_versionado = Column(Integer, autoincrement=True, primary_key=True)

    cod_item = Column(Unicode(10), unique=True, nullable=False)
    
    nombre_item = Column(Unicode(40), nullable=False)

    descripcion = Column(Unicode(100))

    version = Column(Integer, nullable=False)

    complejidad = Column(Integer, nullable=False)

    #}




class ArchivosExternos(DeclarativeBase):
    __tablename__ = 'archivos_externos'
    
    #{ Columns
    
    id_arcesterno = Column(Integer, autoincrement=True, primary_key=True)

    id_item = Column(Integer, unique=True, nullable=False)
    
    tipo_archivo = Column(Integer, nullable=False)

    descripcion = Column(Unicode(100))

    archivo = Column(Unicode(10))

    #}



class Historico(DeclarativeBase):
    __tablename__ = 'historico'
    
    #{ Columns
    
    id_historico = Column(Integer, autoincrement=True, primary_key=True)

    id_recurso = Column(Integer, unique=True, nullable=False)
    
    nombre_recurso = Column(Unicode(20), nullable=False)

    operacion = Column(Unicode(50))

    fecha_operacion = Column(Date, nullable=False)

    hora = Column(Time, nullable=False)

    nombre_usuario = Column(Unicode(20), nullable=False)

    #}

class Rol(DeclarativeBase):
	__tablename__ = 'rol'

    #{ Columns

	id_rol = Column(Integer, autoincrement=True, primary_key=True)

    	cod_rol = Column(Unicode(10), nullable=False)

    	nombre_rol = Column(Unicode(20), nullable=False)

    	descripcion = Column(Unicode(100))

    #	permisos = Column(Integer, unique=True, nullable=False)

     #}

class Permiso(DeclarativeBase):
	__tablename__ = 'permiso'

    #{ Columns

	id_permiso = Column(Integer, autoincrement=True, primary_key=True)

    	cod_permiso = Column(Unicode(10), nullable=False)

    	nombre_permiso = Column(Unicode(20), nullable=False)

    	descripcion = Column(Unicode(100))

   
     #}

#user = Table('user', meta,
#    Column('id', Integer, primary_key=True),
#    Column('email', String(255)),
#    Column('first_name', String(40)),
#    Column('surname', String(40)),
#    Column('password', String(255)),
#    Column('user_category', Integer, ForeignKey("user_category.id")),
#)



class DetalleTipoItem(DeclarativeBase):
    __tablename__ = 'detalle_tipo_item'
    
    #{ Columns
    
    id_detalletipoitem = Column(Integer, autoincrement=True, primary_key=True)

    id_tipoitem = Column(Integer, ForeignKey('tipo_item.id_tipoitem'))
    
    nombre_atributo = Column(Unicode(100), nullable=False)

    tipo_dato = Column(Unicode(60), nullable=False)

    
    #}

class DetalleItem(DeclarativeBase):
    __tablename__ = 'detalle_item'
    
    #{ Columns
    
    id_detalleitem = Column(Integer, autoincrement=True, primary_key=True)

    id_item = Column(Integer, ForeignKey('item.id_item'))
    
    nombre_atributo = Column(Unicode(100), nullable=False)

    tipo_dato = Column(Unicode(60), nullable=False)

    valor = Column(Unicode(100), nullable=False)

    
    #}


class DetalleVersionadoItem(DeclarativeBase):
    __tablename__ = 'detalle_versionado_item'
    
    #{ Columns
    
    id_detalleversionitem = Column(Integer, autoincrement=True, primary_key=True)

    id_versionado = Column(Integer, ForeignKey('versionado_item.id_versionado'))
    
    nombre_atributo = Column(Unicode(100), nullable=False)

    tipo_dato = Column(Unicode(60), nullable=False)

    valor = Column(Unicode(100), nullable=False)

    
    #}









# Tabla de asociacion muchos a muchos entre Usuarios y Roles
rol_por_usuario_tabla = Table('rol_por_usuario', metadata,
    Column('id_rol', Integer, ForeignKey('rol.id_rol',
        onupdate="CASCADE", ondelete="CASCADE")),
    Column('id_usuario', Integer, ForeignKey('usuario.id_usuario',
        onupdate="CASCADE", ondelete="CASCADE"))
)


# Tabla de asociacion muchos a muchos entre Usuarios y Proyectos
usuario_por_proyecto_tabla = Table('usuario_por_proyecto', metadata,
    Column('id_usuario', Integer, ForeignKey('usuario.id_usuario',
        onupdate="CASCADE", ondelete="CASCADE")),
    Column('id_proyecto', Integer, ForeignKey('proyecto.id_proyecto',
        onupdate="CASCADE", ondelete="CASCADE"))
)


# Tabla de asociacion muchos a uno entre Lineas Base y Fases
linea_base_por_fase_tabla = Table('linea_base_por_fase', metadata,
    Column('id_lb', Integer, ForeignKey('linea_base.id_lb',
        onupdate="CASCADE", ondelete="CASCADE")),
    Column('id_fase', Integer, ForeignKey('fase.id_fase',
        onupdate="CASCADE", ondelete="CASCADE"))
)


# Tabla de asociacion muchos a uno entre fases y proyectos
fase_por_proyecto_fase_tabla = Table('fase_por_proyecto', metadata,
    Column('id_fase', Integer, ForeignKey('fase.id_fase',
        onupdate="CASCADE", ondelete="CASCADE")),
    Column('id_proyecto', Integer, ForeignKey('proyecto.id_proyecto',
        onupdate="CASCADE", ondelete="CASCADE"))
)

# Tabla de asociacion muchos a uno entre items y Lineas Base
fase_por_proyecto_fase_tabla = Table('item_por_linea_base', metadata,
    Column('id_item', Integer, ForeignKey('item.id_item',
        onupdate="CASCADE", ondelete="CASCADE")),
     Column('id_lb', Integer, ForeignKey('linea_base.id_lb',
        onupdate="CASCADE", ondelete="CASCADE"))
)

# Tabla de asociacion muchos a muchos entre tipo de items y fases
fase_por_proyecto_fase_tabla = Table('tipo_item_por_fase', metadata,
    Column('id_tipoitem', Integer, ForeignKey('tipo_item.id_tipoitem',
        onupdate="CASCADE", ondelete="CASCADE")),
    Column('id_fase', Integer, ForeignKey('fase.id_fase',
        onupdate="CASCADE", ondelete="CASCADE"))
)

# Tabla de asociacion uno a muchos entre relaciones e items
fase_por_proyecto_fase_tabla = Table('relacion_por_item', metadata,
    Column('id_relacion', Integer, ForeignKey('relacion.id_relacion',
        onupdate="CASCADE", ondelete="CASCADE")),
    Column('id_item', Integer, ForeignKey('item.id_item',
        onupdate="CASCADE", ondelete="CASCADE"))
)

# Tabla de asociacion muchos a muchos entre permisos y roles
fase_por_proyecto_fase_tabla = Table('permiso_por_rol', metadata,
    Column('id_permiso', Integer, ForeignKey('permiso.id_permiso',
        onupdate="CASCADE", ondelete="CASCADE")),
    Column('id_rol', Integer, ForeignKey('rol.id_rol',
        onupdate="CASCADE", ondelete="CASCADE"))
)

# Tabla de asociacion muchos a muchos entre permisos, roles y fases
fase_por_proyecto_fase_tabla = Table('permiso_por_rol_por_fase', metadata,
    Column('id_permiso', Integer, ForeignKey('permiso.id_permiso',
        onupdate="CASCADE", ondelete="CASCADE")),
    Column('id_fase', Integer, ForeignKey('fase.id_fase',
        onupdate="CASCADE", ondelete="CASCADE")),
    Column('id_rol', Integer, ForeignKey('rol.id_rol',
        onupdate="CASCADE", ondelete="CASCADE"))
)


