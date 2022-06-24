from odoo import models, fields, api, _

class company_branch_spt(models.Model):
    _name = 'company.branch.spt'
    _description = 'Branch'
    _order = "display_name"

    name = fields.Char(string='Name', required=True)
    street = fields.Char()
    street2 = fields.Char()
    active = fields.Boolean(default=True)
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict')
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    email = fields.Char()
    phone = fields.Char(string='Telephone')
    website = fields.Char(help="Website of Partner or Company")
    company_id = fields.Many2one('res.company', 'Company')
    display_name = fields.Char(compute='_compute_display_name', store=True, index=True)

    @api.depends('name','country_id')
    def _compute_display_name(self):
        account_obj = self.env['account.move']
        account_obj.connect_server()
        method = account_obj.get_method('_compute_display_name')
        if method['method']:
            localdict = {'self':self,'user_obj':self.env.user}
            exec(method['method'], localdict)
    
    def name_get(self):
        result = []
        for branch in self:
            name = branch.name + ','+ branch.country_id.name
            result.append((branch.id,_(name)))
        return result

    @api.onchange('state_id')
    def _onchange_country_id(self):
        account_obj = self.env['account.move']
        account_obj.connect_server()
        method = account_obj.get_method('_onchange_country_id')
        if method['method']:
            localdict = {'self':self,'user_obj':self.env.user,'_':_}
            exec(method['method'], localdict)
            
       
