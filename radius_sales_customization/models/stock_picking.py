from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    purchase_ref = fields.Char('Purchase Reference')
    has_purchase_ref_custom_label = fields.Boolean('Has Purchase Reference Custom Label', default=False)
    purchase_ref_custom_label = fields.Char('Purchase Reference Label')