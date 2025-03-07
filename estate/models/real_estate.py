# -*- coding: utf-8 -*-

from odoo import _, models, fields, api
from dateutil.relativedelta import relativedelta
import odoo.fields as odoo_fields
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError

class Estate(models.Model):

    def _default_date():
        return fields.Date.today()

    def _availability_date():
        current_datetime = odoo_fields.Datetime.now()

        three_months_later = odoo_fields.Datetime.add(current_datetime, months=3)
        return three_months_later

    _name = "real.estate"
    _description = "estate.estate"
    name = fields.Char(default="House", required=True)
    active = fields.Boolean(
        default=True,
    )  # invisible=True read only
    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("received", "Offer Received"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        required=True,
        copy=False,
        default="new",
    )
    postcode = fields.Char()

    date_availability = fields.Date(default=_availability_date(), copy=False)
    # date_availability = fields.Date(default=_default_date)

    garden_orientation = fields.Selection(
        string="Type",
        selection=[
            ("north", "North"),
            ("south", "South"),
            ("west", "West"),
            ("east", "East"),
        ],
        help="Choose the type of the garden orientation",
    )
    postcode = fields.Char()
    expected_price = fields.Float(default=100)
    best_offer = fields.Float()

    selling_price = fields.Float(copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()

    property_type_id = fields.Many2one("real.estate.type")

    offer_ids = fields.One2many("real.estate.offer", "property_id")

    tag_ids = fields.Many2many("real.estate.tag")
    total_area = fields.Integer(compute="_compute_total_area")
    best_offer = fields.Integer(compute="_compute_best_offer")
    buyer = fields.Char(default="")

    # da error
    # salesperson_id = fields.Many2one("res.users", string="Salesperson", default=lambda self: self.env.user, readonly=True)
    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for property in self:
            property.total_area = property.garden_area + property.living_area

    @api.depends("offer_ids.price")
    def _compute_best_offer(self):
        for property in self:
            property.best_offer = (
                max(property.offer_ids.mapped("price")) if property.offer_ids else 0
            )

    @api.onchange("selling_price")
    def _onchange_selling_price(self):
        if self.selling_price < 0:
            return {
                "warning": {
                    "title": "Warning!",
                    "message": "The price should be more than 0",
                }
            }

    @api.onchange("garden")
    def _onchange_garden(self):
        for state in self:
            if not state.garden:
                state.garden_area = 0
            else:
                return {
                    "warning": {
                        "title": "Warning!",
                        "message": "Do not forget to set garden area",
                    }
                }

    @api.onchange("date_availability")
    def _onchange_date_availability(self):
        current_date = fields.Date.today()
        for property in self:
            if property.date_availability < current_date:

                return {
                    "warning": {
                        "title": "Warning!",
                        "message": "The availability date is set to a date in the past",
                    }
                }

    @api.constrains("date_availability")
    def _check_date_availability(self):
        current_date = fields.Date.today()
        for property in self:
            if property.date_availability < current_date:
                raise ValidationError(
                    _("The availability date can not be set to a date in the past")
                )

    def action_accept_offer(self):
        for property in self:
            offer = property.offer_ids[0]
            offer.action_accept_offer()


    def unlink(self):
        for property in self:
            if property.state == 'sold':
                raise UserError(_("You cannot delete a sold property"))
        return super().unlink()
