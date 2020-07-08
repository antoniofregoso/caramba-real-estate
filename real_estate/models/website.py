# -*- coding: utf-8 -*-


from odoo import api, fields, models



class Website(models.Model):
    _inherit = 'website'
    
    re_sold_ribbon = fields.Boolean('Sold Ribbon', default=True)
    re_disable_sold = fields.Boolean('Disable on sold', help='Disables navigation of sold properties', default=False)
    re_navigation = fields.Boolean('Navigation', help='Add navigation arrows', default=False)
    re_pagination = fields.Selection([('none', 'None'), ('dots', 'Dots'), ('numbered', 'Numbered'), ('progress', 'Progress'), ('fraction', 'Fraction'), ('scrollbar', 'Scrollbar')], String='Pagination', default='numbered')