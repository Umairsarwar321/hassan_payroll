from odoo import fields, models,api

class res_company(models.Model):

    _inherit = 'res.company'

    def _get_branch_ids(self):
        return [('id','in',self.env.user.branch_ids.ids)]

    branch_id = fields.Many2one('company.branch.spt','Branch',domain=lambda self:self._get_branch_ids(),default=lambda self: self.env.user.branch_id)
