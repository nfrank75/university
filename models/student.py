# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniversityStudent(models.Model):
    _name = 'university.student'
    _description = 'Student information'
    _rec_name = 'first_name'

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)

    @api.model
    def _get_default_country(self):
        country = self.env['res.country'].search([('code', '=', 'CM')], limit=1)

        return country

    country_id = fields.Many2one('res.country', string='Country', default=_get_default_country)

    phone = fields.Char()
    email = fields.Char()
    birth_date = fields.Date(string="Birth Date")
    identity_cart = fields.Char(string="Identity Cart")
    address = fields.Char(string="Address")
    registration_date = fields.Datetime(string="Registration Date")
    sex = fields.Selection([("male", "Male"), ("female", "Female")], default="male", string="Sex", required=True)
    department_id = fields.Many2one(comodel_name="university.department")  # each student is related to one department
    faculty_id = fields.Many2one(comodel_name="university.faculty")  # each student is related to one faculty
    classroom_id = fields.Many2one(comodel_name="university.classroom")
    state = fields.Selection([("l1", "Level 1"), ("l2", "Level 2"), ("l3", "Level 3"), ("finished", "Finished")])

    subject_ids = fields.Many2many(comodel_name="university.subject",
                                   relation='sub_stud_rel',
                                   column1='first_name',
                                   column2='subject_name')

    @api.multi
    def name_get(self):
        result = []
        for student in self:
            name = student.first_name + '' + student.last_name
            result.append((student.id, name))
        return result

    @api.multi  # process on multi records
    def next_level(self):
        if self.state == 'l1':
            return self.write({'state': 'l2'})
        elif self.state == 'l2':
            return self.write({'state': 'l3'})
        elif self.state == 'l3':
            return self.write({'state': 'finished'})
        elif self.state == 'finished':
            return {'warning': {'title': 'Finished',
                                'message': 'This student has already finished his level'}}
