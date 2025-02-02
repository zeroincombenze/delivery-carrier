# -*- coding: utf-8 -*-
# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Delivery Carrier Default Tracking Url',
    'summary': """
        Adds the default tracking url on delivery carrier""",
    'version': '10.0.1.1.0',
    'license': 'AGPL-3',
    'maintainers': ['rousseldenis'],
    'development_status': 'Alpha',
    'author': 'ACSONE SA/NV,Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/delivery-carrier',
    'depends': [
        'delivery',
    ],
    'data': [
        'views/delivery_carrier.xml',
        'views/sale_order.xml',
        'views/stock_picking.xml',
    ],
}
