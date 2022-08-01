# -*- coding: utf-8 -*-
{
    'name': "nuprod_contactCustom",

    'summary': """
        Add button on contact invoice pages to create new account""",

    'description': """
        Add button on contact invoice pages to create new account for
        customer or supplier, if it exist we will raise an error
    """,

    'author': "Nuprod",
    'website': "https://www.nuprod.fr",

    "category": "Accounting",
    'version': '0.1',
    "license": "AGPL-3",
    'installable': True,

    'depends': ['base', 'account'],

    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}
