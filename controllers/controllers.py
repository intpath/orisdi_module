# -*- coding: utf-8 -*-
# from odoo import http


# class OrisdiModule(http.Controller):
#     @http.route('/orisdi_module/orisdi_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/orisdi_module/orisdi_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('orisdi_module.listing', {
#             'root': '/orisdi_module/orisdi_module',
#             'objects': http.request.env['orisdi_module.orisdi_module'].search([]),
#         })

#     @http.route('/orisdi_module/orisdi_module/objects/<model("orisdi_module.orisdi_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('orisdi_module.object', {
#             'object': obj
#         })
