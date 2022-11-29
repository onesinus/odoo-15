from odoo import models, fields

class DelmanAccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    jagung = fields.Text()

