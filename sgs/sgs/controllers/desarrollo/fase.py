"""Fase Rest Controller Info"""
from datetime import datetime
from tg.controllers import RestController, redirect
from tg.decorators import expose, validate, with_trailing_slash
from sgs.model import DBSession
from sgs.model.model import *
from tg import tmpl_context
from sgs.form.new import *
from sgs.form.list import *


#from sprox.formbase import AddRecordForm

#__all__ = ['FaseRestController']

class FaseRestController(RestController):


    @expose('sgs.templates.desarrollo.fase.new')
    def new(self, **kw):
        tmpl_context.widget = new_fase_form
        return dict(value=kw)

    @expose('sgs.templates.desarrollo.fase.list')
    def list(self):
        tmpl_context.widget = list_fase
        value = list_fase_filler.get_value()
        return dict(value=value)



