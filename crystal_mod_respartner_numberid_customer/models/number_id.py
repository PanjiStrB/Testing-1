from odoo import models, fields, api

class NumberId(models.Model):
    _inherit ='res.partner'

    number_id=fields.Char(string='Number ID', required=True)
    name=fields.Char( required=True)