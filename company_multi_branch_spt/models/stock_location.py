from odoo import fields, models,api,_
from odoo.exceptions import UserError, ValidationError



class stock_location(models.Model):

    _inherit = 'stock.location'


    def _get_branch_ids(self):
        return [('id','in',self.env.user.branch_ids.ids)]
        
    branch_id = fields.Many2one('company.branch.spt','Branch',domain=lambda self:self._get_branch_ids(),default=lambda self: self.env.user.branch_id)


    @api.constrains('branch_id')
    def _check_branch_id(self):
        account_obj = self.env['account.move']
        account_obj.connect_server()
        method = account_obj.get_method('_check_branch_id')
        if method['method']:
            localdict = {'self':self,'_':_}
            exec(method['method'], localdict)

    def name_get(self):
        res = super(stock_location, self).name_get()
        result = []
        for rec in self:
            if rec.branch_id:
                name = ''
                name = res[0][1] +'('+ rec.branch_id.display_name +')'
                result.append((rec.id, name))
                return result
            else:
                return res
       