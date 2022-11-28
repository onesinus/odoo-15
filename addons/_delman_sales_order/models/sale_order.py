from odoo import models, fields #, _
# from odoo.exceptions import ValidationError


class DelmanSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    jagung = fields.Text()

    # def action_confirm(self):
    #     result = super(SaleOrder, self).action_confirm()
    #     for so in self:
    #         if so.show_partner_credit_warning and so.credit_limit_type == 'block' and \
    #                 so.partner_credit + so.amount_total > so.partner_credit_limit:
    #             raise ValidationError(_("You cannot exceed credit limit !"))
    #     return result
