from odoo import models, fields, api

class DelmanSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    item_status = fields.Selection(
        [('commercial', 'Commercial'), ('warranty', 'Warranty')], 
        'Item Status', 
        default='commercial',
        required=True
    )

    def _set_price_unit(self, obj):
        return 0 if obj.item_status == "warranty" else obj.product_id.list_price

    @api.onchange('item_status')
    def onchange_item_status(self):
        self.price_unit = self._set_price_unit(self)

    def _prepare_invoice_line(self, sequence):
        res = super(DelmanSaleOrderLine, self)._prepare_invoice_line()
        res.update({ 'item_status': self.item_status })
        return res