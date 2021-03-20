# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    governorate = fields.Many2one("res.country.state")
    shipping_company_delivery_number = fields.Char("Shpping Company Delivery Number")
    shipping_company_delivery_date = fields.Date("Shpping Company Delivery Date")
    shipping_cost_a = fields.Integer(compute="_get_shipping_price")

    @api.depends('order_line')
    def _get_shipping_price(self):
        for order in self:
            delivery_lines = order.order_line.filtered(lambda x: x.is_delivery)
            if delivery_lines:
                order.shipping_cost_a = sum( delivery_lines.mapped('price_subtotal') )
            else:
                order.shipping_cost_a = 0

        