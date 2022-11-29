from odoo import models, fields, api

class DelmanAccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    item_status = fields.Selection(
        [('commercial', 'Commercial'), ('warranty', 'Warranty')], 
        'Item Status', 
        default='commercial',
        required=True
    )
    
    @api.onchange('item_status')
    def onchange_item_status(self):
        if self.item_status == "warranty":
            self.price_unit = 0
        else:
            self.price_unit = self.product_id.list_price

    # @api.model
    # def create(self, values):
    #     """Override default Odoo create function and extend."""
    #     # Do your custom logic here
    #     self = self.with_context(check_move_validity=False)

    #     # values["item_status"] = "warranty"
    #     return super(DelmanAccountMoveLine, self).create(values)
