from datetime import date

from odoo import fields, models, api
from odoo.exceptions import UserError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'

    name = fields.Char(string="Patient Name", tracking=True)
    date_of_birth = fields.Date(string="Date of Birth", tracking=True)
    age = fields.Integer(string="Patient Age", compute='_compute_age', store=True)
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ('other', 'Other')
                               ], string="Patient Gender", tracking=True)
    active = fields.Boolean(string="Active", default=1, tracking=True)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                if rec.date_of_birth < date.today():
                    rec.age = date.today().year - rec.date_of_birth.year
                else:
                    raise UserError("Sorry, Birth date not valid.")
