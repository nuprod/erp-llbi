# -*- coding: utf-8 -*-
{
    'name': "Purchase Llbi Nuprod",

    'summary': """
        Add functionality to module purchase""",

    'description': """
        Handle format for steel plate
    """,

    'author': "Nuprod",
    'website': "https://www.nuprod.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
