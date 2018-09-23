# -*- coding: utf-8 -*-
from odoo import http

# class PhoneDirectory(http.Controller):
#     @http.route('/phone_directory/phone_directory/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/phone_directory/phone_directory/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('phone_directory.listing', {
#             'root': '/phone_directory/phone_directory',
#             'objects': http.request.env['phone_directory.phone_directory'].search([]),
#         })

#     @http.route('/phone_directory/phone_directory/objects/<model("phone_directory.phone_directory"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('phone_directory.object', {
#             'object': obj
#         })