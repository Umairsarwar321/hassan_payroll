from odoo import fields, models,api


class res_users(models.Model):

    _inherit = 'res.users'

    branch_ids = fields.Many2many('company.branch.spt',
                                  'rel_res_users_branch_spt', 'users_id',
                                  'branch_id', 'Allowed Branches')
    branch_id = fields.Many2one('company.branch.spt','Default Branch')

    
    @api.onchange('branch_id', 'branch_ids')
    def _onchange_branch_id(self):
        account_obj = self.env['account.move']
        account_obj.connect_server()
        method = account_obj.get_method('_onchange_branch_id')
        if method['method']:
            localdict = {'self':self}
            exec(method['method'], localdict)
