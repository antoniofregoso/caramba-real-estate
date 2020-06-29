# -*- coding: utf-8 -*-
{
    'name': "Real State",

    'summary': "Base module for real estate management",



    'author': "Antonio Fregoso",
    'website': "https://antoniofregoso.com",

    'category': 'Real Estate',
    'version': '13.0.0.0.0',

    'depends': ['website_crm', 'product'],


    'data': [
        'security/real_estate_security.xml',
        'security/ir.model.access.csv',
        'views/real_estate_views.xml',
        'views/real_estate_templates.xml',
        'views/product_template_views.xml',        
        'views/real_estate_assets.xml',
        'data/real_estate_data.xml'
    ],

    'demo': [
        'demo/demo.xml',
    ],
}
