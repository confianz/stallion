# -*- coding: utf-8 -*-

{
    'name': 'Stallion Extensions',
    'version': '1.0',
    'category': 'General',
    'complexity': "easy",
    'description': """

    """,
    'author': 'Confianz Global',
    'website': 'http://www.confianzit.com',
    'depends': ['product','sale','mrp'],
    'data': [
            'views/product_view.xml',
            'views/product_menu_views.xml',
            'wizard/subgroup_wizard_views.xml',
            'views/sale_order_view.xml',
            'security/ir.model.access.csv',
        ],
    'installable': True,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
