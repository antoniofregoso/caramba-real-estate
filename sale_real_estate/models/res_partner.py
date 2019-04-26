# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models, tools

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    is_development =   fields.Boolean('Is Real Estate Development')
     
    
    
    
    
    