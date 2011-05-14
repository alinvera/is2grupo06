"""Configuracion Controller Info"""
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
from sgs.controllers.configuracion.lineabase import LineaBaseRestController

#__all__ = ['ConfiguracionController']

class ConfiguracionController(BaseController):

    
    lineabase = LineaBaseRestController()


    @expose('sgs.templates.configuracion.configuracion')
    def index(self):
        """Handle the front-page."""
        return dict(page='index')

   
