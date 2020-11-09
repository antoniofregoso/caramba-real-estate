# -*- coding: utf-8 -*-


from odoo import api, fields, models



class Website(models.Model):
    _inherit = 'website'
    
    re_sold_ribbon = fields.Boolean('Sold Ribbon', default=True)
    re_stock_ribbon = fields.Boolean('Stock Ribbon', default=True)
    re_disable_sold = fields.Boolean('Disable on sold', help='Disables navigation of sold properties', default=False)
    re_navigation = fields.Boolean('Navigation', help='Add navigation arrows', default=False)
    re_pagination = fields.Selection([('none', 'None'), ('dots', 'Dots'), ('numbered', 'Numbered'), ('progress', 'Progress'), ('fraction', 'Fraction'), ('scrollbar', 'Scrollbar')], String='Pagination', default='numbered', required=True)
    re_map_type = fields.Selection([('ROADMAP', 'RoadMap'),('TERRAIN', 'Terrain'),('SATELLITE', 'Satellite'),('HYBRID', 'Hybrid')], string="Map Type",  default='ROADMAP', required=True)
    re_map_color = fields.Selection([('-', 'Default'),('lightMonoMap', 'Light Mono'),('cupertinoMap', 'Cupertino'),('retroMap', 'Retro'),('cobaltMap', 'Cobalt'),('flatMap', 'Flat'),('blueMap', 'Blue'),('lillaMap', 'Lilla'),('carMap', 'Car'),('bwMap', 'Black & White')], string='Map Color', default='-', required=True)
    re_map_pin_style = fields.Selection([('-','Default'),('flat','Flat')], string='Marker Style', default='-', required=True) 