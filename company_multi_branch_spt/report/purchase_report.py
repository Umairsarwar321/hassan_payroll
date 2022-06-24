# -*- coding: utf-8 -*-
# Part of SnepTech See LICENSE file for full copyright and licensing details.##
##################################################################################
from odoo import tools
from odoo import api, fields, models


class purchase_report(models.Model):
    _inherit = "purchase.report"

    branch_id = fields.Many2one('company.branch.spt','Branch', readonly=True)

    def _select(self):
        return super(purchase_report, self)._select() + ", po.branch_id as branch_id"

    def _group_by(self):
        return super(purchase_report, self)._group_by() + ", po.branch_id"
