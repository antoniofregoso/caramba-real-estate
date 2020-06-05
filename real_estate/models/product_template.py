

from odoo import api, fields, models



class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    development_id = fields.Many2one('real_estate.development', 'Development', select=True)
    area = fields.Float('Builded surface (m2)')
    lot = fields.Float('Total area: (m2)')
    floor = fields.Integer('Floor', help="Floor in which the property is located.")
    storeys = fields.Integer('Storeys', help="Number of floors the property has.")
    beds = fields.Integer('Bedrooms')
    baths = fields.Integer('Bathrooms')
    hbaths = fields.Integer('Half Bathrooms')
    parking = fields.Integer('Parking Places')
    balcony = fields.Float('Balcony (m2)')
    terrace = fields.Float('Terrace (m2)')
    garden = fields.Float('Garden (m2)')
    roof_garden = fields.Float('Roof Garden (m2)')
    storage = fields.Float('Storage (m3)')
    service_yard = fields.Float('Service Yard (m2)')
    environments_ids = fields.Many2many('real_estate.environment', 'product_real_state_environmen_rel',
                                        'product_id', 'envirnment_id', string = 'Environments')

    
    

    
    