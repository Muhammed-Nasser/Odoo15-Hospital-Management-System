from odoo import fields, models, api


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'

    name = fields.Char(string="Patient Name", tracking=True)
    age = fields.Integer(string="Patient Age", tracking=True)
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ('other', 'Other')
                               ], string="Patient Gender", tracking=True)
    active = fields.Boolean(string="Active", default=1, tracking=True)
