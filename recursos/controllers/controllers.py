# -*- coding: utf-8 -*-
from odoo import http

# class Recursos(http.Controller):
#     @http.route('/recursos/recursos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/recursos/recursos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('recursos.listing', {
#             'root': '/recursos/recursos',
#             'objects': http.request.env['recursos.recursos'].search([]),
#         })

#     @http.route('/recursos/recursos/objects/<model("recursos.recursos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('recursos.object', {
#             'object': obj
#         })