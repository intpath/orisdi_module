# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = "res.partner"

    description = fields.Text("Description")
    
    # @api.model
    # def create(self, values):
    #     name = values['name']
    #     dup = self.env['res.partner'].search([('name', '=', name)])
    #     if dup:
    #         raise UserError(_(f"There are already {len(dup)} contact(s) with the same name"))
    #     else:
    #         result = super(ResPartner, self).create(values)
    #         return result
