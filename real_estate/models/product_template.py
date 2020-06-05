

from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    development = fields.Many2one()
    area = fields.Float('Total Area (m2)')
    lot = fields.Float('Lot (m2)')
    floor = fields.Integer('Floor', help="Floor in which the property is located.")
    storeys = fields.Integer('Storeys', help="Number of floors the property has.")
    living_room = fields.Boolean('Living Room')
    kitchen = fields.Boolean('Kitchen')
    suite = fields.Integer('Master Suite')
    beds = fields.Integer('Bedrooms')
    study = fields.Integer('Bedroom/Study')
    baths = fields.Integer('Bathrooms')
    hbaths = fields.Integer('Half Bathrooms')
    offices = fields.Integer('Offices')
    boardrooms = fields.Integer('Boardrooms')
    common_area = fields.Integer('Common Office Area')
    parking = fields.Integer('Parking Places')
    balcony = fields.Float('Balcony (m2)')
    terrace = fields.Float('Terrace (m2)')
    garden = fields.Float('Garden (m2)')
    roof_garden = fields.Float('Roof Garden (m2)')
    amenities = fields.Boolean('Amenities')
    swimming_pool = fields.Boolean('Swimming Pool')
    storage = fields.Float('Storage (m3)')
    service = fields.Integer('Service Room')
    service_yard = fields.Float('Service Yard (m2)')

    
    