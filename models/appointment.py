from odoo import fields, models, api


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'

    # Note: model name should be in first
    patient_id = fields.Many2one('hospital.patient', string="Patient Name", tracking=True)
    age = fields.Integer(string="Patient Age", related='patient_id.age', readonly=True)
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ('other', 'Other')
                               ], string="Patient Gender", related='patient_id.gender', readonly=True)
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)

