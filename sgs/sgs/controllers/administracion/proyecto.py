"""Proyecto Controller Info"""
from datetime import datetime
from tg.controllers import RestController, redirect
from tg.decorators import expose, validate, with_trailing_slash
from sgs.model import DBSession
from sgs.model.model import *
from tg import tmpl_context
from sgs.form.new import *
from sgs.form.list import *


#from sprox.formbase import AddRecordForm

#__all__ = ['ProyectoRestController']

class ProyectoRestController(RestController):


    @expose('sgs.templates.administracion.proyecto.new')
    def new(self, **kw):
        tmpl_context.widget = new_proyecto_form
        return dict(value=kw)

    @expose('sgs.templates.administracion.proyecto.list')
    def list(self):
        tmpl_context.widget = list_proyecto
        value = list_proyecto_filler.get_value()
        return dict(value=value)



