# -*- coding: utf-8 -*-
# from odoo import http


# class CrystalModRespartnerNumberidCustomer(http.Controller):
#     @http.route('/crystal_mod_respartner_numberid_customer/crystal_mod_respartner_numberid_customer/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crystal_mod_respartner_numberid_customer/crystal_mod_respartner_numberid_customer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crystal_mod_respartner_numberid_customer.listing', {
#             'root': '/crystal_mod_respartner_numberid_customer/crystal_mod_respartner_numberid_customer',
#             'objects': http.request.env['crystal_mod_respartner_numberid_customer.crystal_mod_respartner_numberid_customer'].search([]),
#         })

#     @http.route('/crystal_mod_respartner_numberid_customer/crystal_mod_respartner_numberid_customer/objects/<model("crystal_mod_respartner_numberid_customer.crystal_mod_respartner_numberid_customer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crystal_mod_respartner_numberid_customer.object', {
#             'object': obj
#         })
