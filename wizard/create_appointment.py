# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CreateAppointmentWizard(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description = 'Create Appointment Wizard'

    name = fields.Char(string="Appointment Name", required=True)
    date = fields.Datetime(string="Appointment Date", required=True)

    classroom_id = fields.Many2one("university.classroom", string='Classroom Name')

    def action_create_appointment(self):
        print('Button is ok')
