# -*- coding: utf-8 -*-
{
    'name': "university",

    'summary': """
        This module aim to manage the university information  """,

    'description': """
        This module aim to manage the university information 
    """,

    'author': "Ngaleu Frank",
    'github': "http://www.its-nh.com",
    'email': "ngaleufrank94@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/classroom_views.xml',
        'views/department_views.xml',
        'views/faculty_views.xml',
        'views/professor_views.xml',
        'views/student_views.xml',
        'views/subject_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}