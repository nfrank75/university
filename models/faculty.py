# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniversityFaculty(models.Model):
    _name = 'university.faculty'
    _description = "Faculty information"

    name = fields.Char(string="Faculty Name", required=True)
    phone = fields.Char()
    email = fields.Char()
    code = fields.Char()

    department_id = fields.Many2one(comodel_name="university.department")  # each faculty is related to one department
