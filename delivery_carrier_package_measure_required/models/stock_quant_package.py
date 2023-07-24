# Copyright 2022 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class StockQuantPackage(models.Model):
    _inherit = "stock.quant.package"

    length_required = fields.Boolean(related="packaging_id.package_length_required")
    width_required = fields.Boolean(related="packaging_id.package_width_required")
    height_required = fields.Boolean(related="packaging_id.package_height_required")
    weight_required = fields.Boolean(related="packaging_id.package_weight_required")

    # The boolean field use to check if a dimension is required are intentionally left out.
    # To not raise error when changing packaging configuration.
    @api.constrains("pack_length", "width", "height", "shipping_weight", "quant_ids")
    def _check_required_dimension(self):
        ignore_pack_content = self.env.context.get(
            "delivery_pkg_measure__ignore_package_content"
        )
        for package in self:
            if not ignore_pack_content and not package.quant_ids:
                # Only validate a package when it contains goods
                continue
            required_dimension = []
            if package.length_required and not package.pack_length:
                required_dimension.append(_("length"))
            if package.width_required and not package.width:
                required_dimension.append(_("width"))
            if package.height_required and not package.height:
                required_dimension.append(_("height"))
            if package.weight_required and not package.shipping_weight:
                required_dimension.append(_("weight"))
            if required_dimension:
                raise ValidationError(
                    _(
                        "The measurement(s) [{dimension}] are required "
                        "on the package {pack_name} and need to be set."
                    ).format(
                        dimension=", ".join(required_dimension), pack_name=package.name
                    )
                )
