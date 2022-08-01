# -*- coding: utf-8 -*-
# from odoo import http


# class NuprodContactCustom(http.Controller):
#     @http.route('/nuprod_contact_custom/nuprod_contact_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nuprod_contact_custom/nuprod_contact_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nuprod_contact_custom.listing', {
#             'root': '/nuprod_contact_custom/nuprod_contact_custom',
#             'objects': http.request.env['nuprod_contact_custom.nuprod_contact_custom'].search([]),
#         })

#     @http.route('/nuprod_contact_custom/nuprod_contact_custom/objects/<model("nuprod_contact_custom.nuprod_contact_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nuprod_contact_custom.object', {
#             'object': obj
#         })
