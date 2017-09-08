# -*- coding: utf-8 -*-
from openerp import fields, models

class Address_models(models.Model):
    _inherit = "hr.employee"

    direccion_trabajo = fields.Char(string="Dirección de trabajo")

    direccion_particular = fields.Char(string="Dirección particular")