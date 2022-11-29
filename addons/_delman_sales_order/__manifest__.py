# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Delman Odoo 15 Sales Invoice Custom Module',
    'version': '0.0.1',
    'category': 'Sales Order',
    'summary': 'Delman Odoo 15 Sales Invoice Custom Module',
    'description': 'Delman Odoo 15 Sales Invoice Custom Module',
    # 'live_test_url': '',
    'sequence': '1',
    'website': 'delman.io',
    'author': 'Delman data Lab',
    'maintainer': 'Engineer Delman',
    'license': 'LGPL-3',
    'support': 'engineering@delman.com',
    'depends': ['sale'],
    'excludes': [],
    'demo': [],
    'data': [
        'views/sale_order.xml',
        'views/account_move.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [
        # 'static/description/banner.png'
    ],
}
