# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniversityProfessor(models.Model):
    _name = 'university.professor'
    _description = 'Professor information'
    _rec_name = 'first_name'

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    sex = fields.Selection([("male", "Male"), ("female", "Female")], default="male", string="Sex", required=True)

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
    start_date = fields.Datetime(string="Start Date")
    state = fields.Selection([("l1", "Level 1"), ("l2", "Level 2"), ("l3", "Level 3"), ("finished", "Finished")])

    department_id = fields.Many2one(comodel_name="university.department")  # each professor is related to one dept
    subject_id = fields.Many2one(comodel_name="university.subject")  # the professor's subject

    classroom_ids = fields.Many2many(comodel_name="university.classroom",
                                     relation='prof_class_rel',
                                     column1='first_name',
                                     column2='name')

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

    @api.multi
    def name_get(self):
        result = []
        for student in self:
            name = student.first_name + '' + student.last_name
            result.append((student.id, name))
        return result