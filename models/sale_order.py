# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    governorate = fields.Many2one("res.country.state")
    shipping_company_delivery_number = fields.Char("Shpping Company Delivery Number")
    shipping_company_delivery_date = fields.Date("Shpping Company Delivery Date")        
