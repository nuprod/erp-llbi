# -*- coding: utf-8 -*-
# from odoo import http


# class NuprodPurchaseLlbi(http.Controller):
#     @http.route('/nuprod_purchase_llbi/nuprod_purchase_llbi', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nuprod_purchase_llbi/nuprod_purchase_llbi/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nuprod_purchase_llbi.listing', {
#             'root': '/nuprod_purchase_llbi/nuprod_purchase_llbi',
#             'objects': http.request.env['nuprod_purchase_llbi.nuprod_purchase_llbi'].search([]),
#         })

#     @http.route('/nuprod_purchase_llbi/nuprod_purchase_llbi/objects/<model("nuprod_purchase_llbi.nuprod_purchase_llbi"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nuprod_purchase_llbi.object', {
#             'object': obj
#         })
