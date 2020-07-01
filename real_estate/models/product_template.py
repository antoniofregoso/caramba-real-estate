

from odoo import api, fields, models
from odoo.addons.http_routing.models.ir_http import slug
from odoo.tools.translate import html_translate



class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    
    type = fields.Selection(selection_add=[('estate', 'Real Estate')], tracking=True)
    development_id = fields.Many2one('real_estate.development', 'Development', select=True)
    real_estate_type_id = fields.Many2one('real_estate.type', 'Type')  
    area = fields.Float('Builded Surface (m2)')
    lot = fields.Float('Total Area: (m2)')
    floor = fields.Integer('Floor', help="Floor in which the property is located.")
    storeys = fields.Integer('Storeys', help="Number of floors the property has.")
    beds = fields.Integer('Bedrooms')
    master_suite = fields.Integer('Master Suite')
    baths = fields.Integer('Bathrooms')
    hbaths = fields.Integer('Half Bathrooms')
    parking = fields.Integer('Parking Places')
    balcony = fields.Float('Balcony (m2)')
    terrace = fields.Float('Terrace (m2)')
    garden = fields.Float('Garden (m2)')
    roof_garden = fields.Float('Roof Garden (m2)')
    storage = fields.Float('Storage (m3)')
    service_yard = fields.Float('Service Yard (m2)')
    real_estate_website_url = fields.Char(compute='_compute_real_estate_website_url()')
    environments_ids = fields.Many2many('real_estate.environment', 'product_real_state_environmen_rel',
                                        'product_id', 'envirnment_id', string = 'Environments')
    real_estate_sequence = fields.Integer('Website Sequence', help="Determine the display order in the Website E-commerce",
                                      default=lambda self: self._default_real_estate_sequence(), copy=False)
    real_estate_description = fields.Html('Description', translate=html_translate)
    real_estate_website_header = fields.Html('Description for the website', sanitize_attributes=False, translate=html_translate)
    
      
    def _default_real_estate_sequence(self):
        ''' We want new product to be the last (highest seq).
        Every product should ideally have an unique sequence.
        Default sequence (10000) should only be used for DB first product.
        As we don't resequence the whole tree (as `sequence` does), this field
        might have negative value.
        '''
        self._cr.execute("SELECT MAX(real_estate_sequence) FROM %s" % self._table)
        max_sequence = self._cr.fetchone()[0]
        if max_sequence is None:
            return 10000
        return max_sequence + 5
    
    def _compute_website_url(self):
        super(ProductTemplate, self)._compute_website_url()
        for product in self:
            if product.type == 'estate':
                product.website_url =  "/real-estate/development/{}/unit/{}".format(slug(product.development_id), slug(product))
            else:
                product.website_url = "/shop/product/%s" % slug(product)

  
    
    