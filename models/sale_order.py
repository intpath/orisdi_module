# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    governorate = fields.Many2one("res.country.state")
    shipping_company_delivery_number = fields.Char("Shpping Company Delivery Number")
    shipping_company_delivery_date = fields.Date("Shpping Company Delivery Date")        

    sourcing_date = fields.Datetime('Sourcing Date', readonly=False, copy=False)
    sourcing_delay = fields.Integer('Sourcing Delay', readonly=False, copy=False)

    def action_confirm(self):
        date_order = self.date_order
        res = super(SaleOrder, self).action_confirm()
        self.date_order = date_order
        self.sourcing_delay = (self.date_order - self.sourcing_date).days
        return res

    def draft_to_confirm(self):
        res = super(SaleOrder, self).draft_to_confirm()
        self.sourcing_date = self.date_order
        return res
