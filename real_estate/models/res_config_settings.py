# -*- coding: utf-8 -*-


from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    
    
    re_sold_ribbon = fields.Boolean('Sold Ribbon',related='website_id.re_sold_ribbon', readonly=False)
    re_disable_sold = fields.Boolean('Disable on sold',related='website_id.re_disable_sold', readonly=False)
    re_navigation = fields.Boolean('Navigation', help='Add navigation arrows',related='website_id.re_navigation', readonly=False)
    re_pagination = fields.Selection([('none', 'None'), ('dots', 'Dots'), ('numbered', 'Numbered'), ('progress', 'Progress'), ('fraction', 'Fraction'), ('scrollbar', 'Scrollbar')], String='Pagination', default='numbered'
                                     ,related='website_id.re_pagination', readonly=False)