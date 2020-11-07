


from odoo import api, fields, models
from odoo.addons.http_routing.models.ir_http import slug
from odoo.tools.translate import html_translate
from datetime import date

import logging
_logger = logging.getLogger(__name__)

class RealEstateAmenitie(models.Model):
    _name = 'real_estate.amenitie'
    _description = 'Real State Amenitie'
    
    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index', default=0)
    
class RealEstateService(models.Model):
    _name = 'real_estate.service'
    _description = 'Real State Service'
    
    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index', default=0)
    
class RealEstateEnvironment(models.Model):
    _name = 'real_estate.environment'
    _description = 'Real State Environment'
    
    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer('Color Index', default=0)
    
class RealEstateType(models.Model):
    _name = 'real_estate.type'
    _description = 'Real State Type'
    
    name = fields.Char('Name', required=True, translate=True)
    

class RealEstateDevelopment(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin', 'website.seo.metadata', 'website.published.multi.mixin']
    _name = 'real_estate.development'
    _description = 'Real State Development'
    _order = 'name asc, priority desc'
    
    def _compute_website_url(self):
        super(RealEstateDevelopment, self)._compute_website_url()
        for estate in self:
            estate.website_url = "/real-estate/development/%s" % slug(estate)


    name = fields.Char('Name', required=True, translate=True)
    summary = fields.Char('Summary', translate=True)
    development_type = fields.Selection([('residential','Residential Real Estate'), ('commercial','Commercial Real Estate'), ('mixed','Mixed Real Estate'), ('industrial','Industrial Real Estate'), ('land','Land')], default='residential', required=True)
    description = fields.Html('Description', translate=html_translate)
    website_header = fields.Html('Description for the website', sanitize_attributes=False, translate=html_translate)
    active = fields.Boolean(default=True)
    color = fields.Integer('Kanban Color Index')
    real_estate_sequence = fields.Integer('Portal Sequence')
    state = fields.Selection([
        ('draft', 'Draft'), ('onpresale', 'On Presale'), ('onsale', 'On Sale'), ('sold', 'Sold'), ('stopped','Stopped'), ('cancel', 'Cancelled')],
        string='Status', default='draft', required=True, copy=False, track_visibility='onchange', group_expand='_expand_states')
    delivery_date = fields.Date('Estimated delivery date', default=date.today())
    immediate_delivery = fields.Boolean(default=False)
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict', domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    date_localization = fields.Date(string='Geolocation Date')
    latitude = fields.Float(string='Geo Latitude', digits=(16, 5))
    longitude = fields.Float(string='Geo Longitude', digits=(16, 5))
    zoom = fields.Integer(string='Zoom Map', default=12)
    priority = fields.Selection([('0', 'Free'), ('1', 'Bronze'), ('2', 'Silver'), ('3', 'Gold')], string ='Location on website', default='0')
    offer = fields.Selection([('rent', 'For Rent'), ('sale', 'For Sale')], default='sale')
    amenities_ids = fields.Many2many('real_estate.amenitie', 'real_state_development_real_state_amenitie_rel', 'real_state_development_id', 'real_state_amenitie_id', string='Amenities')
    services_ids = fields.Many2many('real_estate.service','real_state_development_real_state_service_rel', 'real_state_devlopment_id','real_state_service_id', string='Services')
    user_id = fields.Many2one('res.users', string='Responsible', index=True, tracking=True, default=lambda self: self.env.user)
    units_ids = fields.One2many('product.template', 'development_id', string='Unit', ondelete='cascade')  
    price_from = fields.Float('From')
    price_to = fields.Float('To')
    currency_id = fields.Many2one('res.currency', required=True)
       
    def _expand_states(self, states, domain, order):
        return ['draft', 'onpresale', 'onsale', 'sold', 'stopped']
    
    @api.model
    def create(self, vals):        
        prices = []
        if self.units_ids:
            for unit in self.units_ids:
                prices.append(unit.list_price)
            vals['price_from'] = min(prices)
            vals['price_to'] = max(prices)
        res = super(RealEstateDevelopment, self).create(vals)
        return res
    
    def write(self, vals):
        prices = []
        if self.units_ids:
            for unit in self.units_ids:
                prices.append(unit.list_price)           
            vals['price_from'] = min(prices)
            vals['price_to'] = max(prices)  
        res = super(RealEstateDevelopment, self).write(vals)
        return res

    @api.model
    def _geo_localize(self, street='', zip='', city='', state='', country=''):
        geo_obj = self.env['base.geocoder']
        search = geo_obj.geo_query_address(street=street, zip=zip, city=city, state=state, country=country)
        result = geo_obj.geo_find(search, force_country=country)
        if result is None:
            search = geo_obj.geo_query_address(city=city, state=state, country=country)
            result = geo_obj.geo_find(search, force_country=country)
        return result

    def geo_localize(self):
        # We need country names in English below
        for partner in self.with_context(lang='en_US'):
            result = self._geo_localize(partner.street,
                                        partner.zip,
                                        partner.city,
                                        partner.state_id.name,
                                        partner.country_id.name)

            if result:
                partner.write({
                    'latitude': result[0],
                    'longitude': result[1],
                    'date_localization': fields.Date.context_today(partner)
                })
        return True

    

    
    
