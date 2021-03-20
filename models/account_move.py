# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = "account.move"

    sale_id = fields.Many2one("sale.order", compute="_get_sale_order_id")
    sale_shipping_cost = fields.Integer(related="sale_id.shipping_cost_a", string="Shipping Company Cost")
    sale_shipping_company_delivery_number = fields.Char("Shpping Company Delivery Number", related="sale_id.shipping_company_delivery_number")
    sale_shipping_company_delivery_date = fields.Date("Shpping Company Delivery Date", related="sale_id.shipping_company_delivery_date")
    sale_governorate_id = fields.Many2one("res.country.state", related="sale_id.governorate")
    
    @api.depends('invoice_origin')
    def _get_sale_order_id(self):
        for move in self:
            if move.invoice_origin:
                sale_id = self.env['sale.order'].search([('name', '=', move.invoice_origin)])
                move.sale_id = sale_id.id
            else:
                move.sale_id = False
