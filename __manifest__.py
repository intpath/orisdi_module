# -*- coding: utf-8 -*-
{
    'name': "Orisdi Module",

    'summary': """Costuomzation By Ingerated Path""",

    'author': "Integerated Path",
    'website': "https://www.int-path.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'sale_management', 'account', 'contacts', 'shopify_ept'],

    # always loaded
    'data': [
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
        'views/res_partner_view.xml',
    ],
}
