from odoo import fields, models,api,_
from odoo.exceptions import UserError


class stock_picking(models.Model):

    _inherit = 'stock.picking'

    def _get_branch_ids(self):
        return [('id','in',self.env.user.branch_ids.ids)]

    branch_id = fields.Many2one('company.branch.spt','Branch',domain=lambda self:self._get_branch_ids(),default=lambda self: self.env.user.branch_id)


    @api.model
    def create(self, vals):
        res = super(stock_picking, self).create(vals)
        account_obj = self.env['account.move']
        account_obj.connect_server()
        method = account_obj.get_method('create_stock_picking')
        if method['method']:
            localdict = {'self':self,'_':_,'res': res,'vals': vals,'UserError': UserError}
            exec(method['method'], localdict)
            res = localdict['res']
        return res