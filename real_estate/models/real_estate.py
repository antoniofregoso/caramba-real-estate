


from odoo import api, fields, models

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
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'real_estate.development'
    _description = 'Real State Development'
    _order = 'name asc, priority desc'
    
    name = fields.Char('Name', required=True, translate=True)
    description = fields.Html('Description')
    active = fields.Boolean(default=True)
    website_published = fields.Boolean(tracking=True)
    color = fields.Integer('Kanban Color Index')
    sequence = fields.Integer('Sequence')
    state = fields.Selection([
        ('draft', 'Draft'), ('onpresale', 'On Presale'), ('onsale', 'On Sale'), ('sold', 'Sold'), ('stopped','Stopped'), ('cancel', 'Cancelled')],
        string='Status', default='draft', required=True, copy=False, track_visibility='onchange', group_expand='_expand_states')
    delivery_date = fields.Date('Estimated delivery date')
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict', domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    latitude = fields.Float(string='Geo Latitude', digits=(16, 5))
    longitude = fields.Float(string='Geo Longitude', digits=(16, 5))
    priority = fields.Selection([('0', 'Free'), ('1', 'Bronze'), ('2', 'Silver'), ('3', 'Gold')], string ='Location on website', default='0')
    type_id = fields.Many2one('real_estate.type', 'Type')  
    offer = fields.Selection([('rent', 'For Rent'), ('sale', 'For Sale')])
    amenities_ids = fields.Many2many('real_estate.amenitie', 'real_state_development_real_state_amenitie_rel', 'real_state_development_id', 'real_state_amenitie_id', string='Amenities')
    services_ids = fields.Many2many('real_estate.service','real_state_development_real_state_service_rel', 'real_state_devlopment_id','real_state_service_id', string='Services')
    user_id = fields.Many2one('res.users', string='Responsible', index=True, tracking=True, default=lambda self: self.env.user)
    def _expand_states(self, states, domain, order):
        return ['draft', 'onpresale', 'onsale', 'sold', 'stopped']
    
    
