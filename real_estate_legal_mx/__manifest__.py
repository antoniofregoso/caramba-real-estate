# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

{
    'name': "Sale Legal Documents",

    'summary': "Basis for legal documents of sale in Mexico",

    'description': """
        Long description of module's purpose
    """,

    'author': "Antonio Fregoso",
    'website': "http://www.antoniofregoso.blog",
    'category': 'Sale',
    'version': '12.0.0.0.0',


    'depends': ['sale'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/legal_views.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
}