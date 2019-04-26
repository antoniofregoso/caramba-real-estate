# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#
from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit  = "product.template"
    
    development_id = fields.Many2one('res.partner', 'Development', select=True)
    area = fields.Float('Total Area (m2)')
    lot = fields.Float('Lot (m2)')
    floor = fields.Integer('Floor', help='Floor in which the unit is located.')
    floors = fields.Integer('Number of floors', help='Number of floors in unit', default=1)
    living_room = fields.Boolean('Living Room', default=1)
    kitchen = fields.Boolean('Kitchen', default=1)
    suite = fields.Integer('Master Suite', default=0)
    bedrooms = fields.Integer('Bedrooms', default=1)
    study = fields.Integer('Bedroom/Study', default=1)
    bathrooms = fields.Integer('Bathrooms', default=1)
    hbathrooms = fields.Integer('1/2 Bathrooms', default=1)
    offices = fields.Integer('Offices', default=0)
    boardrooms = fields.Integer('Boardrooms', default=0)
    common_area = fields.Integer('Common Office Area', default=1)
    parking = fields.Integer('Parking Places', default=1)
    balcony = fields.Float('Balcony (m2)', default=0.0)
    terrace = fields.Float('Terrace (m2)', default=0.0)
    garden = fields.Float('Garden (m2)', default=0.0)
    roof_garden = fields.Float('Roof Garden (m2)', default=0.0)
    storage = fields.Float('Storage(m3)', default=0.0)
    service_room = fields.Integer('Service Rooms', default=0)
    service_yard = fields.Float('Service Yard (m2)', default=0.0)
    delivery =  fields.Char('Delivery')
    real_estate_unit_ok = fields.Boolean(string='Is an Real Estate Unit')
    
class ProductParkingPlace(models.Model):
    _name = 'product.parking_place'
    _description = 'Allocation of Parking Places'
    
    name = fields.Char('Name', required=True, select=True)
    development_id = fields.Many2one('res.partner', 'Development', select=True, domain="[('development', '=', 1)]")
    product_id = fields.Many2one('product.template', 'Property', domain="['|',('area', '>', 0),('lot', '>', 0)]")
    