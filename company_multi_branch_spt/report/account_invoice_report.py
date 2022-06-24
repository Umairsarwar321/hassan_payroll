# -*- coding: utf-8 -*-
# Part of SnepTech See LICENSE file for full copyright and licensing details.##
##################################################################################
from odoo import fields, models


class account_invoice_report(models.Model):
    _inherit = 'account.invoice.report'

    branch_id = fields.Many2one('company.branch.spt','Branch', readonly=True)

    def _select(self):
        return super(account_invoice_report, self)._select() + ", move.branch_id as branch_id"

    def _group_by(self):
        return super(account_invoice_report, self)._group_by() + ", move.branch_id"
