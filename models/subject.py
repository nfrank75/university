# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniversitySubject(models.Model):
    _name = 'university.subject'
    _description = 'Subject information'

    subject_name = fields.Char(string="Subject Name", required=True)
    code = fields.Char("Code")

    department_id = fields.Many2one(comodel_name="university.department")  # each subject is related to one dept

    professor_ids = fields.Many2many(comodel_name="university.professor",
                                     relation='sub_prof_rel',
                                     column1='subject_name',
                                     column2='first_name')
