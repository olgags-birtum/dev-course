from odoo import _, api, models, fields


class EstateType(models.Model):

    _name = "real.estate.type"
    _description = "type"
    _order = "name"
    _sql_constraints = [
        ("unique_tag_name", "unique (name)", "Property type name should be unique")
    ]
    name = fields.Char(string="Name", required=True)
    property_ids = fields.One2many("real.estate", "property_type_id")
    property_count = fields.Integer(compute="_compute_property_count")

    offer_ids = fields.One2many("real.estate.offer", "type_id")
    offer_count= fields.Integer(compute="_compute_offer_count")


    def _compute_offer_count(self):
        for rec in self:
            rec.offer_count = len(rec.offer_ids)

    def _compute_property_count(self):
        for rec in self:
            rec.property_count = len(rec.property_ids)

    def action_open_property_ids(self):
        return {
            "name": _("Related Properties"),
            "type": "ir.actions.act_window",
            "view_mode": "tree,form",
            "res_model": "real.estate",
            "target": "current",
            "domain": [("property_type_id", "=", self.id)],
            "context": {"default_property_type_id": self.id},
        }
    def action_open_offer_ids(self):
        return {
            "name": _("Related Offers"),
            "type": "ir.actions.act_window",
            "view_mode": "tree,form",
            "res_model": "real.estate.offer",
            "target": "current",
            "domain": [("type_id", "=", self.id)],
            "context": {"default_type_id": self.id},
        }