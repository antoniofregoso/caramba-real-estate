# -*- coding: utf-8 -*-
# from odoo import http


# class Product-real-state(http.Controller):
#     @http.route('/product-real-state/product-real-state/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product-real-state/product-real-state/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product-real-state.listing', {
#             'root': '/product-real-state/product-real-state',
#             'objects': http.request.env['product-real-state.product-real-state'].search([]),
#         })

#     @http.route('/product-real-state/product-real-state/objects/<model("product-real-state.product-real-state"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product-real-state.object', {
#             'object': obj
#         })
