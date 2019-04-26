# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#
from odoo import api, fields, models

class StockPicking(models.Model):
    _inherit  = "stock.picking"
    
    delivery_man =  fields.Many2one('res.partner', 'Delivery Man')
