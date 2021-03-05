
from odoo import http, _
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)


class WebsiteRealEstate(http.Controller):
    
    @http.route([
        '''/real-estate/development/<model("real_estate.development", "[('website_id', 'in', (False, current_website_id))]"):development>'''
        ], type='http', auth="public", website=True)
    def development(self, development=None, **opt):
        development = request.env['real_estate.development'].sudo().browse(development.id)
        values = {
            'development':development,
            'main_object':development,
            'web_values': {
                'rent': _('For Rent'),
                'sale': _('For Sale'),
                'residential':_('Residential Real Estate'),
                'commercial':_('Commercial Real Estate'),
                'mixed':_('Mixed Real Estate'), 
                'industrial':_('Industrial Real Estate'), 
                'land':_('Land'),
                'draft':_('Draft'),
                'onpresale':_('On Presale'),
                'onsale':_('On Sale'),
                'sold':_('Sold'),
                'stopped':_('Stopped'),
                'cancel':_('Cancelled'),
                }}
        return request.render("real_estate.real_estate_development_content", values)
    
    @http.route([
        '''/real-estate/development/<model("real_estate.development"):development>/unit/<model("product.template"):unit>'''
    ], type='http', auth="public", website=True)
    def unit(self, development, unit, **opt):
        development = request.env['real_estate.development'].sudo().browse(development.id)
        values = {
            'development':development,
            'unit': unit,
            'main_object':unit,
            'web_values': {
                'rent': _('For Rent'),
                'sale': _('For Sale'),
                'residential':_('Residential Real Estate'),
                'commercial':_('Commercial Real Estate'),
                'mixed':_('Mixed Real Estate'), 
                'industrial':_('Industrial Real Estate'), 
                'land':_('Land'),
                'draft':_('Draft'),
                'onpresale':_('On Presale'),
                'onsale':_('On Sale'),
                'sold':_('Sold'),
                'stopped':_('Stopped'),
                'cancel':_('Cancelled'),
                }}
        return  request.render("real_estate.real_estate_unit_content", values)
    
