import random
from odoo import _,models, fields, api


class EstateTag(models.Model):

    _name = "real.estate.tag"
    _description = "Tags of real estate model"
    _order = "name"
    _sql_constraints = [
        ('unique_tag_name', 'unique (name)','Tag name should be unique')
    ]
    name = fields.Char(string="Tag Name", required=True)
    color=fields.Char()

  
    def action_open_property_ids(self):
            return {
                "name": _("Related Properties"),
                "type": "ir.actions.act_window",
                "view_mode": "tree,form",
                "res_model": "real.estate",
                "target": "iframe",
                "domain": [("tag_ids", "=", self.id)],# filter por tag id of the properties - should be equal to the currect tag id 
                "context":  {"default_tag_ids": [(6, 0, [self.id])]},
            }