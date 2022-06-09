from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection([
        ('boq', 'Bill of Quantity'),
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='boq')
    partner_id = fields.Many2one(
        'res.partner', string='Customer', readonly=True,
        states={'boq': [('readonly', False)], 'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True, tracking=1,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", )
    partner_invoice_id = fields.Many2one(
        'res.partner', string='Invoice Address',
        readonly=True, required=True,
        states={'boq': [('readonly', False)], 'draft': [('readonly', False)], 'sent': [('readonly', False)], 'sale': [('readonly', False)]},
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", )
    partner_shipping_id = fields.Many2one(
        'res.partner', string='Delivery Address', readonly=True, required=True,
        states={'boq': [('readonly', False)], 'draft': [('readonly', False)], 'sent': [('readonly', False)], 'sale': [('readonly', False)]},
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", )

    pricelist_id = fields.Many2one(
        'product.pricelist', string='Pricelist', check_company=True,  # Unrequired company
        required=True, readonly=True, states={'boq': [('readonly', False)], 'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", tracking=1,
        help="If you change the pricelist, only newly added lines will be affected.")

    analytic_account_id = fields.Many2one(
        'account.analytic.account', 'Analytic Account',
        readonly=True, copy=False, check_company=True,  # Unrequired company
        states={'boq': [('readonly', False)], 'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        help="The analytic account related to a sales order.")
    project_id = fields.Many2one(
        'project.project', 'Project', readonly=True,
        states={'boq': [('readonly', False)], 'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        help='Select a non billable project on which tasks can be created.')

    quotation_type = fields.Selection(selection=[('local', 'Local Part'), ('imported', 'Imported Part')], string='Quotation Type')
    terms_and_conditions = fields.Many2many('terms.conditions', string='Terms and Conditions')

    def action_make_quotation(self):
        self.state = 'draft'

    # @api.model
    # def create(self, vals):
    #     vals['boq_id'] = self.env['ir.sequence'].next_by_code('sale.order')
        # return super(SaleOrder, self).create(vals)