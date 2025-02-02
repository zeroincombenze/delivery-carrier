# -*- coding: utf-8 -*-
# Copyright 2012 Camptocamp SA
# Author: Guewen Baconnier
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    carrier_file_id = fields.Many2one('delivery.carrier.file', 'Carrier File')
