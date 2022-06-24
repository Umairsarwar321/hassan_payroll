# -*- coding: utf-8 -*-
# Part of SnepTech See LICENSE file for full copyright and licensing details.##
##################################################################################

{
    'name': 'Company Multi Branch',
    'version': '13.0.0.1',
    'summary': 'Company Branch Management',
    'sequence': 1,
    'author': 'SnepTech',
    'license': 'AGPL-3',
    'website': 'https://www.sneptech.com/',
    'description':"""
        This Module provides functionality to manage Multiple Branches for a single Company.
    """,
    "images": ["static/description/Banner.png"],
    "price": "99.99",
    "currency": "USD",
    'depends':['sale','crm','sale_crm','sale_management','account','stock','purchase'],
    'data':[
        'security/ir.model.access.csv',
        'security/res_groups.xml',
        'views/branch_spt.xml',
        'views/res_users_views.xml',
        # 'views/res_partner_view.xml',
        'views/res_company_view.xml',
        'views/sale_order_views.xml',
        'views/purchase_order_view.xml',
        'views/stock_picking_view.xml',
        'views/stock_warehouse_view.xml',
        # 'views/stock_move_view.xml',
        # 'views/stock_move_line_view.xml',
        'views/stock_location_view.xml',
        'views/account_move_view.xml',
        'views/account_payment_view.xml',
        'views/account_journal_view.xml',
        'views/crm_lead_view.xml',
        'views/account_move_line_view.xml',
        'views/stock_production_lot_view.xml',
        'views/stock_picking_type_view.xml',
        'views/stock_quant_view.xml',


        'report/sale_quotation_report_extend.xml',
        'report/purchase_quotation_report_extend_spt.xml',
        'report/purchase_order_report_extend_spt.xml',
        'report/report_picking_order_report_inherit_spt.xml',
        'report/report_deliveryslip_extend_spt.xml',
        'report/report_payment_receipt_document_extend_spt.xml',
        'report/report_invoice_document_extend_spt.xml',
        ],
        
    'application': True,
    'installable': True,
    'auto_install': False,
}
