# -*- coding: utf-8 -*-
{
    'name': "Real State",

    'summary': "Base module for real estate management",



    'author': "Antonio Fregoso",
    'website': "https://www.antoniofregoso.com",

    'category': 'Real Estate/Real Estate',
    'version': '0.0.0',
    'license': 'AGPL-3',

    'depends': ['website_crm', 'website_sale', 'sale_stock', 'base_geolocalize'],


    'data': [
        'security/real_estate_security.xml',
        'security/ir.model.access.csv',
        'views/real_estate_views.xml',
        'views/res_config_settings_views.xml',
        'views/real_estate_templates.xml',
        'views/product_template_views.xml',        
        'views/real_estate_assets.xml',
        'data/real_estate_data.xml'
    ],

    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
