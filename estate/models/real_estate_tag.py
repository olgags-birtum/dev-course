import random
from odoo import models, fields, api


class EstateTag(models.Model):

    _name = "real.estate.tag"
    _description = "Tags of real estate model"
    _order = "name"
    _sql_constraints = [
        ('unique_tag_name', 'unique (name)','Tag name should be unique')
    ]
    name = fields.Char(string="Tag Name", required=True)
    color=fields.Char()

  
