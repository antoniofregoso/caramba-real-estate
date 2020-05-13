# -*- coding: utf-8 -*-
{
    'name': "Product Real State",

    'summary': "Add address and specific attributes of real estate to product template",



    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Real State',
    'version': '13.0.0.0.0',

    'depends': ['product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_template_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
