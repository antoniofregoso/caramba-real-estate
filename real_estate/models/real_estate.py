


from odoo import api, fields, models
from odoo.addons.http_routing.models.ir_http import slug
from odoo.tools.translate import html_translate
from datetime import date

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
    sequence = fields.Integer('Sequence')
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
    latitude = fields.Float(string='Geo Latitude', digits=(16, 5))
    longitude = fields.Float(string='Geo Longitude', digits=(16, 5))
    priority = fields.Selection([('0', 'Free'), ('1', 'Bronze'), ('2', 'Silver'), ('3', 'Gold')], string ='Location on website', default='0')
    offer = fields.Selection([('rent', 'For Rent'), ('sale', 'For Sale')], default='sale')
    amenities_ids = fields.Many2many('real_estate.amenitie', 'real_state_development_real_state_amenitie_rel', 'real_state_development_id', 'real_state_amenitie_id', string='Amenities')
    services_ids = fields.Many2many('real_estate.service','real_state_development_real_state_service_rel', 'real_state_devlopment_id','real_state_service_id', string='Services')
    user_id = fields.Many2one('res.users', string='Responsible', index=True, tracking=True, default=lambda self: self.env.user)
    units_ids = fields.One2many('product.template', 'development_id', string='Unit')  
    price_from = fields.Float('From', default=10000000.00)
    price_to = fields.Float('To', default=20000000.00)
    currency_id = fields.Many2one('res.currency', required=True)
       
    def _expand_states(self, states, domain, order):
        return ['draft', 'onpresale', 'onsale', 'sold', 'stopped']
    

    
    
