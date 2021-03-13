# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ProductProduct(models.Model):
    _inherit = "product.product"
    
    shipping_product = fields.Boolean(groups="base.group_no_one")

    @api.constrains('shipping_product')
    def _check_shipping_product(self):
        res = self.env['product.product'].search([('shipping_product', '=', True)])
        if len(res) > 1:
            raise UserError(_("You can only select one shipping product at a time"))
        else:
            pass