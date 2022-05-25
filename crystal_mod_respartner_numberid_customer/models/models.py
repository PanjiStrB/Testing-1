# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class crystal_mod_respartner_numberid_customer(models.Model):
#     _name = 'crystal_mod_respartner_numberid_customer.crystal_mod_respartner_numberid_customer'
#     _description = 'crystal_mod_respartner_numberid_customer.crystal_mod_respartner_numberid_customer'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
