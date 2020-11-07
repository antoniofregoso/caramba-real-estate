# -*- coding: utf-8 -*-


from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    
    
    re_sold_ribbon = fields.Boolean('Sold Ribbon',related='website_id.re_sold_ribbon', readonly=False)
    re_stock_ribbon = fields.Boolean('Stock Ribbon',related='website_id.re_stock_ribbon', readonly=False)
    re_disable_sold = fields.Boolean('Disable on sold',related='website_id.re_disable_sold', readonly=False)
    re_navigation = fields.Boolean('Navigation', help='Add navigation arrows',related='website_id.re_navigation', readonly=False)
    re_pagination = fields.Selection([('none', 'None'), ('dots', 'Dots'), ('numbered', 'Numbered'), ('progress', 'Progress'), ('fraction', 'Fraction'), ('scrollbar', 'Scrollbar')], String='Pagination', default='numbered'
                                     ,related='website_id.re_pagination', readonly=False)
    re_map_type = fields.Selection([('ROADMAP', 'RoadMap'),('TERRAIN', 'Terrain'),('SATELLITE', 'Satellite'),('HYBRID', 'Hybrid')],related='website_id.re_map_type'
                                    , default='ROADMAP', readonly=False)
    re_map_color = fields.Selection([('-', 'Default'),('lightMonoMap', 'Default'),('cupertinoMap', 'Cupertino'),('retroMap', 'Retro'),('cobaltMap', 'Cobalt'),('flatMap', 'Flat'),('blueMap', 'Blue'),('lillaMap', 'Lilla'),('carMap', 'Car'),('bwMap', 'Black & White')]
                                    ,related='website_id.re_map_color', readonly=False)
    re_map_pin_style = fields.Selection([('-','Default'),('flat','Flat')],related='website_id.re_map_pin_style', readonly=False) 