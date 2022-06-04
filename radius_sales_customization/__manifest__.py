# -*- coding: utf-8 -*-

{
    'name': "Sales Customization (Radius)",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Daffodil Computers Ltd.",
    'website': "https://daffodil-bd.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'project', 'sale_project', 'stock', 'mail', 'sales_dynamic_terms_conditions'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'views/multi_sale_quotation_view.xml',
        'views/stock_picking_view.xml',
        'reports/layouts/report_layout_header.xml',
        'reports/layouts/report_layout_footer.xml',
        'reports/forwarding_letter_template.xml',
        'reports/terms_and_conditions_template.xml',
        'reports/quotation_report_template.xml',
        'reports/boq_report_template.xml',
        'reports/report_deliveryslip.xml',
        'reports/reports.xml',
        'reports/sale_report_inherit.xml'
        # 'data/sequence_data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [],
}
