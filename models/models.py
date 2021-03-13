# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class orisdi_module(models.Model):
#     _name = 'orisdi_module.orisdi_module'
#     _description = 'orisdi_module.orisdi_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
