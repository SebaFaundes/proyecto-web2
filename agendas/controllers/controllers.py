# -*- coding: utf-8 -*-
from odoo import http

# class Agendas(http.Controller):
#     @http.route('/agendas/agendas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agendas/agendas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('agendas.listing', {
#             'root': '/agendas/agendas',
#             'objects': http.request.env['agendas.agendas'].search([]),
#         })

#     @http.route('/agendas/agendas/objects/<model("agendas.agendas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agendas.object', {
#             'object': obj
#         })