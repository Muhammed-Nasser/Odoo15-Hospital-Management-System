from odoo import fields, models, api


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'

    # Note: model name should be in first
    patient_id = fields.Many2one('hospital.patient', string="Patient Name", tracking=True)
    # age = fields.Integer(string="Patient Age", tracking=True)
    # gender = fields.Selection([('male', 'Male'),
    #                            ('female', 'Female'),
    #                            ('other', 'Other')
    #                            ], string="Patient Gender", tracking=True)
    appointment_time = fields.Datetime(string="Appointment Time")
    booking_date = fields.Date(string="Booking Date")

