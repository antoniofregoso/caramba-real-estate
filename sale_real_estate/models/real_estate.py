# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models, tools

class SocialArea(models.Model):
    _name = 'real_estate.development.social_area'
    _order = 'name'

    name = fields.Char(string='Name', required=True, translate=True)
    color = fields.Integer('Color Index')
    
    
    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Social area already exists !"),
    ]
    
class Exterior(models.Model):
    _name = 'real_estate.development.exterior'
    _order = 'name'

    name = fields.Char(string='Name', required=True, translate=True)
    color = fields.Integer('Color Index')
    
    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Exterior already exists !"),
    ]
    
class Service(models.Model):
    _name = 'real_estate.development.service'
    _order = 'name'

    name = fields.Char(string='Name', required=True, translate=True)
    color = fields.Integer('Color Index')
    
    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Service already exists !"),
    ]
    
class Amenities(models.Model):
    _name = 'real_estate.development.amenity'
    _order = 'name'
    
    name = fields.Char(string='Name', required=True, translate=True)
    color = fields.Integer('Color Index')
    
    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Amenity already exists !"),
    ]

    name = fields.Char(string='Name', required=True, translate=True)
    
class General_characteristic(models.Model):
    _name = 'real_estate.development.general_characteristic'
    _order = 'name'

    name = fields.Char(string='Name', required=True, translate=True)
    color = fields.Integer('Color Index')
    
    _sql_constraints = [
        ('name_uniq', 'unique (name)', "General Characteristic already exists !"),
    ]
    
class RealEstateDevelopment(models.Model):
    _name = "real_estate.development"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin', 'real_estate.location']
    _description = "Real State Development"
    _order = 'name desc, id desc'
    
    name = fields.Char('Name', required=True)
    state = fields.Selection([('cancel','Cancel'), ('draft', 'Concept'), ('presale', 'Presale'), ('sale', 'Sale'), ('sold','Sold')], string='Status',
      required=True,  copy=False, default='draft')
    type = fields.Selection([('greenfield','Greenfield'), ('brownfield','Brownfield'), ('sub-division','Sub-division'), 
                             ('residential_v','Residential Vertical'), ('residential_h','Residential Horizontal'), ('resort','Resort'),
                             ('vacation', 'Vacation'), ('office','Office'), ('mixed', 'Mixed-Use'), ('retail', 'Retail'), 
                             ('commercial','Commercial'), ('industrial','Industrial'), ('repositioning','Repositioning and re-development')])
    location_id = fields.Many2one('res.partner', string='Location')
    delivery =  fields.Char('Delivery')
    units = fields.Integer('Units', compute='_get_units', copy=False, readonly=True)
    price_from = fields.Float('Price from', compute='_get_price_from', copy=False, readonly=True)
    price_to = fields.Float('Price to', compute='_get_price_to', copy=False, readonly=True)
    area_from = fields.Float('Area from', compute='_get_area_from', copy=False, readonly=True)
    area_to = fields.Float('Area to', compute='_get_area_to', copy=False, readonly=True)
    description = fields.Html('Description')
    social_areas_ids =  fields.Many2many('real_estate.development.social_area', 'real_estate_development_social_area_rel', 'development_id', 'social_area_id', 'Social Areas')
    exteriors_ids =  fields.Many2many('real_estate.development.exterior', 'real_estate_development_exterior_rel', 'development_id', 'exterior_id', 'Exteriors')
    services_ids =  fields.Many2many('real_estate.development.service', 'real_estate_development_service_rel', 'development_id', 'service_id', 'Services')
    amenities_ids = fields.Many2many('real_estate.development.amenity', 'real_estate_development_amenity_rel', 'development_id', 'amenity_id', 'Amenities')
    general_characteristics_ids =  fields.Many2many('real_estate.development.general_characteristic', 'real_estate_development_general_rel', 'development_id', 'general_id', 'General Characteristics')
    units = fields.One2many('real_estate.unit', 'development_id', 'Units', states={'cancel': [('readonly', True)], 'done': [('readonly', True)]}, copy=True)
    color = fields.Integer(string='Color Index')
    sequence = fields.Integer('Sequence')
    product_ids = fields.One2many('product.product', 'product_id', string='Units') 
    deed = fields.char('Title Deed')
    deed_date = fields.date('Date Deed')
    notary_public = fields.many2one('res.partner', 'Deed Notary Public')
    folio = fields.char('Folio Real')
    deed_country_id = fields.many2one('res.country', 'Deed Country', ondelete='restrict'),
    deed_state_id = fields.many2one("res.country.state", 'Deed State', ondelete='restrict')
    deed_city = fields.char('Deed City')
    condominium = fields.boolean('Condominium', default = True)
    condominium_property = fields.char('Condominium Property')
    condominium_date = fields.date('Date Condominium')
    condominium_notary_public = fields.many2one('res.partner', 'Condominium Notary Public')
    condominium_country_id = fields.many2one('res.country', 'Condominium Country', ondelete='restrict')
    condominium_state_id = fields.many2one("res.country.state", 'Condominium State', ondelete='restrict')
    condominium_city = fields.char('Condominium City')
    property_tax = fields.char('Property Tax')
    land_use = fields.many2one('res.partner.land_use', 'Land Use Type')
    land_use_forwarder = fields.many2one('res.partner', 'Land Use Forwarder')
    land_use_licence = fields.char('Land Use Licence Number')
    land_use_date = fields.date('Land Use Date')
    electricity_service = fields.char('ID Electricity Service')
    water_service = fields.char('ID Water Service')
    gas_service = fields.char('ID Gas Service')
    telephone_service = fields.char('ID Telephone Service')
    days_to_deed = fields.integer('Days to Client Deed')
    days_to_deliver = fields.integer('Days to Deliver')
    structures_warranty = fields.integer('Structures Warranty', default= 5 ,help='It can not be less than five years')
    waterproofing_warranty = fields.integer('Waterproofing Warranty', default=3,help='It can not be less than three years')
    other_warranty = fields.integer('Other Elements Warranty', default=1, help='It can not be less than one year')
    bonuse_small = fields.float('Defects Light %', default=5.0 ,help='In the case of faults or failures slight. It is levied on the value of the repair')
    bonuse_big = fields.float('Defects Serius %', default=20, help='In the case of faults or failures slight. It is applied to the total purchase price')
    
    
    

