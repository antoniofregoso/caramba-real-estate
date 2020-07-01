
from odoo import http, fields, _
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)


VALUES = {
    'draft':_('Draft'),
    'onpresale':_('On Presale'),
    'onsale':_('On Sale'),
    'sold':_('Sold'),
    'stopped':_('Stopped'),
    'cancel':_('Cancelled'),
    'residential':_('Residential Real Estate'),
    'commercial':_('Commercial Real Estate'),
    'mixed':_('Mixed Real Estate'),
    'industrial':_('Industrial Real Estate'),
    'land':_('Land'),
    'rent':_('For Rent'),
    'sale':_('For Sale')
    }


class WebsiteRealEstate(http.Controller):
    
    @http.route([
        '''/real-estate/development/<model("real_estate.development", "[('website_id', 'in', (False, current_website_id))]"):development>'''
        ], type='http', auth="public", website=True)
    def development(self, development=None, **opt):
        development = request.env['real_estate.development'].sudo().browse(development.id)
        web_values = {'type':  self.get_web_value(development.development_type)}
        web_values['state'] =  self.get_web_value(development.state)
        web_values['offer'] =  self.get_web_value(development.offer)
        values = {
            'development':development,
            'web_values': web_values,
            }
        return request.render("real_estate.real_state_development_content", values)
    
    @http.route([
        '''/real-estate/development/<model("real_estate.development", "[('website_id', 'in', (False, current_website_id))]"):development>/unit/<model("product.template", "[('development_id','=',development[0])]"):product_template>''',
    ], type='http', auth="public", website=True)
    def unit(self, development, product_template, tag_id=None, page=1, enable_editor=None, **post):
        development = request.env['real_estate.development'].sudo().browse(development.id)
        unit = request.env['product.template'].sudo().browse(product_template.id)
        web_values = {'type':  self.get_web_value(development.development_type)}
        web_values['state'] =  self.get_web_value(development.state)
        web_values['offer'] =  self.get_web_value(development.offer)
        values = {
            'development':development,
            'unit': product_template,
            'web_values': web_values
            }
        return  request.render("real_estate.real_state_unit_content", values)
    
    def get_web_value(self,key):
        return VALUES[key]
        