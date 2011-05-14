"""Administracion Controller Info"""
import pylons
from datetime import datetime
from tg.controllers import RestController, redirect
from sgs.lib.base import BaseController
from pylons import request
from tg.decorators import expose, validate, with_trailing_slash
from sgs.model import DBSession
from sgs.model.model import *
from formencode.validators import DateConverter, Int, NotEmpty
from sprox.tablebase import TableBase
from sgs.controllers.administracion.usuario import UsuarioRestController
from sgs.controllers.administracion.proyecto import ProyectoRestController
from sgs.controllers.administracion.rol import RolRestController


#__all__ = ['AdministracionRestController']

class AdministracionController(BaseController):

    
    usuario = UsuarioRestController()

    proyecto = ProyectoRestController()

    rol = RolRestController()

    @expose('sgs.templates.administracion.administracion')
    def index(self):
        """Handle the front-page."""
        return dict(page='index')

   
