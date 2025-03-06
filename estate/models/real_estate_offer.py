from odoo import _
from odoo import models
from odoo import fields
from odoo import api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError


class EstateOffer(models.Model):

    _name = "real.estate.offer"
    _description = "Offers made for estate"
    _order = "property_id" 



    #_order = "sequence desc"
    #sequence = fields.Integer(default=1)

    price = fields.Float()
    status = fields.Selection(
        [
            ("accepted", "Accepted"),
            ("refused", "Refused"),
            ("done", "Done"),
        ],
        copy=False,
        default="done",
    )
    partner_id = fields.Many2one("res.partner", required=True, string="Buyer")
    property_id = fields.Many2one("real.estate", required=True)


     # store tru no funciona
     #psycopg2.errors.UndefinedColumn: column real_estate_offer.property_name does not exist
#LINE 1: ...fer"."validity" FROM "real_estate_offer" ORDER BY "real_esta...

    property_name = fields.Char(related="property_id.name")
    
    type_id = fields.Many2one(related="property_id.property_type_id", store= "True")
    name = fields.Char(related="property_id.name")
    validity = fields.Integer(default=7)

    date_deadline = fields.Date(
        string="Deadline",
        compute="_compute_date_deadline",
        inverse="_inverse_date_deadline",
    )

    @api.depends("validity")
    def _compute_date_deadline(self):
        for offer in self:
            offer.date_deadline = fields.Date.today() + relativedelta(
                days=offer.validity
            )

    @api.depends("validity")
    def _inverse_date_deadline(self):
        for property in self:
            property.validity = (property.date_deadline - fields.Date.today()).days

    def action_accept_offer(self):
        self.ensure_one()
        if self.property_id.state == "sold":

            raise UserError(_("The property has already been sold"))
        if "accepted" in self.property_id.offer_ids.mapped("status"): 
            raise UserError(_("One offer has been already accepted"))
        if self.status == "refused":
            raise UserError(_("Offer has been already refused"))
        if self.price < self.property_id.expected_price * 0.9:
            self.status = "refused"  
            raise ValidationError(
                _("The selling price cannot be lower than 90% of the expected price")
            )
        self.status = "accepted"
        self.property_id.selling_price = self.price
        self.property_id.state = "sold"
        self.property_id.buyer = self.partner_id # no funciona

    def action_refuse_offer(self):
        self.ensure_one()
        if self.status == "refused":
            raise UserError(_("Offer has been already refused"))
        self.status = "refused"
