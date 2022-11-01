# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniversityClassroom(models.Model):
    _name = 'university.classroom'
    _inherit = 'mail.thread'  # it's main class of message, chat ....
    _rec_name = 'name'
    _description = 'Classroom information'

    name = fields.Char(string="Classroom Name", required=True)
    code = fields.Char("Code")
    size = fields.Char("Size")

    student_ids = fields.One2many(comodel_name="university.student", inverse_name='classroom_id')

    professor_ids = fields.Many2many(comodel_name="university.professor",
                                     relation='class_prof_rel',
                                     column1='name',
                                     column2='first_name')  # les profs qui donnent cours dans des classes

    subject_ids = fields.Many2many(comodel_name="university.subject",
                                   relation='class_sub_rel',
                                   column1='name',
                                   column2='subject_name')
    num_prof = fields.Integer(string='Number of Professors', compute='count_prof')
    num_student = fields.Integer(string='Number of Students', compute='count_student')
    num_subject = fields.Integer(string='Number of Subjects', compute='count_subject')
    state = fields.Selection([("l1", "Level 1"), ("l2", "Level 2"), ("l3", "Level 3"), ("finished", "Finished")])

    def count_prof(self):
        for prof in self:
            self.num_prof = len(prof.professor_ids)

    def count_student(self):
        for stud in self:
            self.num_student = len(stud.student_ids)

    def count_subject(self):
        for subject in self:
            self.num_subject = len(subject.subject_ids)

    @api.multi
    def next_level(self):
        if self.state == 'l1':
            return self.write({'state': 'l2'})
        elif self.state == 'l2':
            return self.write({'state': 'l3'})
        elif self.state == 'l3':
            return self.write({'state': 'finished'})
        else:
            return {'warning': {'title': 'Finished'}}
