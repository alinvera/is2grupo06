"""New"""
import pylons
from datetime import datetime
from tg.controllers import RestController, redirect
from pylons import request
from tg.decorators import expose, validate, with_trailing_slash
from sgs.model import DBSession
from sgs.model.model import Usuario, Permiso, Proyecto, Fase, TipoItem, Item, LineaBase, Relacion, VersionadoItem, ArchivosExternos, Historico, Rol, DetalleTipoItem, DetalleItem, DetalleVersionadoItem
from formencode.validators import DateConverter, Int, NotEmpty
from sprox.tablebase import TableBase

from sprox.formbase import AddRecordForm

class NewUsuarioForm(AddRecordForm):
    __model__ = Usuario
#    __omit_fields__ = ['genre_id', 'movie_id']
new_usuario_form = NewUsuarioForm(DBSession)

class NewProyectoForm(AddRecordForm):
    __model__ = Proyecto
#    __omit_fields__ = ['genre_id', 'movie_id']
new_proyecto_form = NewProyectoForm(DBSession)

class NewRolForm(AddRecordForm):
    __model__ = Rol
#    __omit_fields__ = ['genre_id', 'movie_id']
new_rol_form = NewRolForm(DBSession)

class NewFaseForm(AddRecordForm):
    __model__ = Fase
#    __omit_fields__ = ['genre_id', 'movie_id']
new_fase_form = NewFaseForm(DBSession)

class NewTipoItemForm(AddRecordForm):
    __model__ = TipoItem
#    __omit_fields__ = ['genre_id', 'movie_id']
new_tipoitem_form = NewTipoItemForm(DBSession)

class NewItemForm(AddRecordForm):
    __model__ = Item
#    __omit_fields__ = ['genre_id', 'movie_id']
new_item_form = NewItemForm(DBSession)

class NewRelacionForm(AddRecordForm):
    __model__ = Relacion
#    __omit_fields__ = ['genre_id', 'movie_id']
new_relacion_form = NewRelacionForm(DBSession)
