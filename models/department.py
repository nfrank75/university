# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniversityDepartment(models.Model):
    _name = 'university.department'
    _description = 'Department information'

    name = fields.Char(string="Department Name", required=True)
    phone = fields.Char()
    email = fields.Char()
    code = fields.Char()

    professor_ids = fields.One2many(comodel_name="university.professor",
                                    inverse_name='department_id')  # each dept contains the professors where thy tey
    # teach subjects
    subject_ids = fields.One2many(comodel_name="university.subject", inverse_name='department_id')
