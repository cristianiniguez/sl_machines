# -*- coding: utf-8 -*-
# from odoo import http


# class SlMachines(http.Controller):
#     @http.route('/sl_machines/sl_machines/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sl_machines/sl_machines/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sl_machines.listing', {
#             'root': '/sl_machines/sl_machines',
#             'objects': http.request.env['sl_machines.sl_machines'].search([]),
#         })

#     @http.route('/sl_machines/sl_machines/objects/<model("sl_machines.sl_machines"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sl_machines.object', {
#             'object': obj
#         })
