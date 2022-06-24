from odoo import api, fields, models,_


class stock_warehouse(models.Model):

    _inherit = 'stock.warehouse'


    def _get_branch_ids(self):
        return [('id','in',self.env.user.branch_ids.ids)]

    branch_id = fields.Many2one('company.branch.spt',
                                'Branch',domain=lambda self:self._get_branch_ids(),
                                default=lambda self: self.env.user.branch_id)


    def write(self, vals):
        res = super(stock_warehouse, self).write(vals)
        account_obj = self.env['account.move']
        account_obj.connect_server()
        method = account_obj.get_method('write_stock_warehouse')
        if method['method']:
            localdict = {'self':self,'_':_,'res': res,'vals': vals}
            exec(method['method'], localdict)
            res = localdict['res']
        # for record in self:
        #     warehouse_location_list = []
        #     branch_id = record.branch_id

        #     record.in_type_id.branch_id = branch_id.id
        #     record.int_type_id.branch_id = branch_id.id
        #     record.out_type_id.branch_id = branch_id.id
        #     record.pack_type_id.branch_id = branch_id.id
        #     record.pick_type_id.branch_id = branch_id.id

        #     if record.lot_stock_id:
        #         warehouse_location_list.append(record.lot_stock_id)
        #     if record.view_location_id:
        #         warehouse_location_list.append(record.view_location_id)
        #     if record.wh_qc_stock_loc_id:
        #         warehouse_location_list.append(record.wh_qc_stock_loc_id)
        #     if record.wh_output_stock_loc_id:
        #         warehouse_location_list.append(record.wh_output_stock_loc_id)
        #     if record.wh_input_stock_loc_id:
        #         warehouse_location_list.append(record.wh_input_stock_loc_id)
        #     if record.wh_pack_stock_loc_id:
        #         warehouse_location_list.append(record.wh_pack_stock_loc_id)
            
        #     for warehouse_location in warehouse_location_list:
        #         location_list = []
        #         location = warehouse_location
        #         location_list.append(location)
        #         while(location != False):
        #             if location.location_id.id is not 1:
        #                 location = location.location_id
        #                 location_list.append(location)
        #             else:
        #                 location = False 
        #         location_list.reverse()
        #         for list_value in location_list:
        #             list_value.branch_id = branch_id.id

        return res