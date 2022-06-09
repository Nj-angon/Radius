from odoo import models, fields, api


class MultiSaleQuotation(models.Model):
    _name = 'multi.sale.quotation'
    _inherit = ['mail.thread']
    _description = 'Multi Sale Quotation'

    STATES = [
        ('boq', 'Bill of Quantity'),
        ('draft', 'Quotation'),
        ('sale', 'Sales Order')
    ]
    boq_id = fields.Char(string="BOQ ID")
    quot_id = fields.Char(string="Quotation ID", states={'draft': [('readonly', False)], 'draft': [('readonly', False)],                                           'sent': [('readonly', False)]})
    name = fields.Char('Reference', compute='_compute_name')
    # project_name = fields.Char('Project')
    project_id = fields.Many2one('project.project', string='Project')
    partner_id = fields.Many2one('res.partner', string='Customer')
    contact_person_id = fields.Many2one('res.partner', string='Attention', domain="[('parent_id', '=', partner_id)]")
    validity_date = fields.Date('Expiration')
    date_order = fields.Datetime('Quotation Date', default=fields.Datetime.now)
    state = fields.Selection(selection=STATES, string='Status', default='boq')
    forwarding_letter = fields.Boolean('Forwarding Letter', default=False)
    subject = fields.Char('Subject')
    quotation_ids = fields.Many2many('sale.order', string='Quotations')
    terms_and_conditions = fields.Many2many('terms.conditions', string='Terms and Conditions')

    @api.depends('quotation_ids')
    def _compute_name(self):
        for rec in self:
            rec.name = '-'.join([q.name for q in rec.quotation_ids])

    def action_make_quotation(self):
        if self.quotation_ids:
            self.quotation_ids.write({
                'state': 'draft'
            })
        self.state = 'draft'

    def action_sales_order(self):
        if self.quotation_ids:
            self.quotation_ids.write({
                'state': 'sale'
            })
        self.state = 'sale'




