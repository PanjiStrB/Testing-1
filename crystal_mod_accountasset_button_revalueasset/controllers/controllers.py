# -*- coding: utf-8 -*-
# from odoo import http


# class CrystalModAccountassetButtonRevalueasset(http.Controller):
#     @http.route('/crystal_mod_accountasset_button_revalueasset/crystal_mod_accountasset_button_revalueasset/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crystal_mod_accountasset_button_revalueasset/crystal_mod_accountasset_button_revalueasset/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crystal_mod_accountasset_button_revalueasset.listing', {
#             'root': '/crystal_mod_accountasset_button_revalueasset/crystal_mod_accountasset_button_revalueasset',
#             'objects': http.request.env['crystal_mod_accountasset_button_revalueasset.crystal_mod_accountasset_button_revalueasset'].search([]),
#         })

#     @http.route('/crystal_mod_accountasset_button_revalueasset/crystal_mod_accountasset_button_revalueasset/objects/<model("crystal_mod_accountasset_button_revalueasset.crystal_mod_accountasset_button_revalueasset"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crystal_mod_accountasset_button_revalueasset.object', {
#             'object': obj
#         })
