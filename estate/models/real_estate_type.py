from odoo import models, fields, api


class EstateType(models.Model):

    _name = "real.estate.type"
    _description = "type"
    _order = "name"

    name = fields.Char(string="Name", required=True)
    property_ids =  fields.One2many('real.estate', 'property_type_id')
