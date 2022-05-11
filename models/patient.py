from odoo import fields, models, api


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string="Patient Name")
    age = fields.Integer(string="Patient Age")
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ('other', 'Other')
                               ], string="Patient Gender")
    active = fields.Boolean(string="Active", default=1)
