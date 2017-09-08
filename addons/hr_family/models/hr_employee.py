# -*- coding: utf-8 -*-
# Copyright (C) 2011 Michael Telahun Makonnen <mmakonnen@gmail.com>.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    fam_spouse = fields.Char("Name")
    fam_spouse_employer = fields.Char("Employer")
    fam_spouse_tel = fields.Char("Telephone.")
    #Personalizados
    fam_spose_borndate = fields.Date(string="Fecha de nacimiento")
    fam_spouse_address = fields.Char(string="Dirección", help="Dirección de conyugue")

    fam_children_ids = fields.One2many(
        'hr.employee.children', 'employee_id', "Children")
    fam_father = fields.Char("Father's Name")
    fam_father_date_of_birth = fields.Date(
        "Date of Birth", oldname='fam_father_dob')
    #Personalizado
    fam_address = fields.Char(string="Dirección de los padres", help="Dirección de los padres del empleado")
    
    fam_mother = fields.Char("Mother's Name")
    fam_mother_date_of_birth = fields.Date(
        "Date of Birth", oldname='fam_mother_dob')
