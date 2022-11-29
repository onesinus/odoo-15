from odoo import models, fields

class DelmanSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    jagung = fields.Text()

