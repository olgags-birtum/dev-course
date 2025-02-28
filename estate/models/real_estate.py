# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Estate(models.Model):
    _name = "real.estate"
    _description = "estate.estate"
    name = fields.Char(default="House", required=True)
    # expected_price = fields.Float()
    garden_orientation = fields.Selection(
        string="Type",
        selection=[("north", "North"), ("south", "South")],
        help="Choose the type of the garden orientation",
    )
    postcode = fields.Char()
    date_availability = fields.Date()
    selling_price = fields.Float(required=True)
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()


#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
