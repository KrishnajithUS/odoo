from odoo import fields, models


class RealEstateProperty(models.Model):
    _name = "real.estate.property"
    _description = "Demo real estate module"

    name = fields.Char(string="Real estate property name", required=True)
    description = fields.Text(string="A breif description about real estate property")
    postcode = fields.Integer(required=True)
    date_availability = fields.Date()
    expected_price = fields.Boolean()
    selling_price = fields.Boolean()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        [("north", "North"), ("west", "West"), ("south", "South"), ("east", "Easte")]
    )
