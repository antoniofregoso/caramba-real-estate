# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models

class LegalTag(models.Model):

    _name = "legal.tag"
    _description = "Legal Tag"

    name = fields.Char('Tag', required=True, translate=True)
    color = fields.Integer('Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Meeting place name already exists !"),
    ]
    
class LegalSale(models.Model):

    _name = "legal.sale"
    _description = "Purchase-Sale Contract"
    
    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, states={'draft': [('readonly', False)]}, index=True, default=lambda self: _('New'))
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent to signature'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', track_sequence=3, default='draft')
    type = fields.Selection([('sale','Real Estate Purchase-Sale Contract'), ('rental','Real Estate Rental Contract'),('exclusive','Real Estate Brokerage Agreement- Exclusive'), ('no-exclusive','Real Estate Brokerage Agreement-No Exclusive')])
    date_order = fields.Datetime(string='Order Date', required=True, readonly=True, index=True)
    signature_date = fields.Date(string='Signature Date')
    sale_order_id = fields.Many2one('sale.order', string='Sale Order', help="Reference of the sale order that generated this contract request.")
    development_id = fields.Many2one('res.partner', string='Development')
    product_id = fields.Many2one('product.product', string='Unit')
    partner_id = fields.Many2one('res.partner', string='Buyer')
    legal_representative_id = fields.Many2one('res.partner', string='Legal representative')
    tag_ids = fields.Many2many('lean_marketing.brand.tag', 'lean_marketing_brand_tags_rel', 'brand_id', 'tag_id', string='Tags') 
    color = fields.Integer('Kanban Color Index')
    priority = fields.Selection([('0', 'Low'),('1', 'Medium'),('2', 'High'),('3', 'Very High')], string='Priority', index=True, default='0')
    
    