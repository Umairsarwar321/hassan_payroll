from odoo import fields, models,api

class stock_quant(models.Model):

    _inherit = 'stock.quant'


    branch_id = fields.Many2one('company.branch.spt','Branch',related='location_id.branch_id', store=True, readonly=False)
