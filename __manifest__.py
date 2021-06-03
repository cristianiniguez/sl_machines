# -*- coding: utf-8 -*-
{
    'name': "SaitoLab Machines",

    'summary': """Machines and Maintenance System Management Module""",

    'description': """
        Machine Management by Areas and Groups
        Preventive and Corrective Maintenance Management
    """,

    'author': "Cristian Iniguez",
    'website': "http://www.cristianiniguez.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'views/machines_menuitems.xml',
        'views/machines_area_views.xml',
        'views/machines_model_views.xml',
        'views/machines_machine_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
