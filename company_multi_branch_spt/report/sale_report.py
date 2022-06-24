# -*- coding: utf-8 -*-
# Part of SnepTech See LICENSE file for full copyright and licensing details.##
##################################################################################
from odoo import tools
from odoo import api, fields, models


class sale_report(models.Model):
    _inherit = "sale.report"

    branch_id = fields.Many2one('company.branch.spt','Branch', readonly=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['branch_id'] = ", s.branch_id as branch_id"
        groupby += ', s.branch_id'
        return super(sale_report, self)._query(with_clause, fields, groupby, from_clause)
