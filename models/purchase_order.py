# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class PurchaseOrderLine(models.Model):
	_inhrerit = "purchase.order.line"

	selling_price = fields.Float("Selling Price", related="product_id.lst_price")