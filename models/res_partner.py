# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = "res.partner"

    _sql_constraints = [
        ('unique_name', 'unique (name)', 'Contact already exists!')
    ]

    description = fields.Text("Description")
    
