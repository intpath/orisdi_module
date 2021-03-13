# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    governorate = fields.Many2one("res.country.state")
    shipping_company_delivery_number = fields.Char("Shpping Company Delivery Number")
    shipping_company_delivery_date = fields.Date("Shpping Company Delivery Date")
    shipping_cost_a = fields.Integer(readonly=True)

    @api.constrains('order_line')
    def _get_delivery_product(self):
        delivery_product__line_id = self.order_line.filtered(lambda x: x.product_id.shipping_product)
        if len(delivery_product__line_id) == 0:
            self.shipping_cost_a = 0

        elif len(delivery_product__line_id) == 1:
            self.shipping_cost_a = delivery_product__line_id.price_subtotal

        else:
            raise UserError(_("More Than One Delivery Products Detected ! You only enter one per sale order"))
        