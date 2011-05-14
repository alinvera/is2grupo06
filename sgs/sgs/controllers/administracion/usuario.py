"""Usuario Controller Info"""
from datetime import datetime
from tg.controllers import RestController, redirect
from tg import expose, flash, require, url, request, redirect
from sgs.model import DBSession
from sgs.model.model import *
from sgs.form.new import *
from sgs.form.list import *
from tg import tmpl_context


#from sprox.formbase import AddRecordForm

__all__ = ['UsuarioRestController']

class UsuarioRestController(RestController):


    @expose('sgs.templates.administracion.usuario.new')
    def new(self, **kw):
        tmpl_context.widget = new_usuario_form
        return dict(value=kw)

    #@validate(new_usuario_form, error_handler=new)
    @expose()
    def post(self, **kw):
        #del kw['sprox_id']
        usuario = Usuario(**kw)
        DBSession.add(usuario)
        flash("El usuario ha sido creado correctamente.")
        redirect("/administracion/usuario/list")

    @expose('sgs.templates.administracion.usuario.list')
    def list(self, **kw):
        tmpl_context.widget = list_usuario
        value = list_usuario_filler.get_value()
        return dict(value=value)



