
from odoo import models, fields, api

class AccountAsset(models.Model):
    _inherit = 'account.asset.asset'

    

    revalue_count = fields.Integer(compute='_revalue_count', string='# Revalue Asset')

    def _revalue_count(self):
        for record in self:
            revalue_count = self.env['account.asset.depreciation.line'].search_count([('asset_id', '=', record.id)])
            record.revalue_count= revalue_count
            

    def open_revalues(self):
        return {
            'name': ('Revalue Assets'),
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'account.asset.depreciation.line',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'domain': [('asset_id', '=', self.id)],
            'target':'new',
            'context': "{'default_asset_id': active_id, 'create': False}"
        }