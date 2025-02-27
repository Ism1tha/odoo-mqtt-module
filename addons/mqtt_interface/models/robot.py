from odoo import models, fields

class Robot(models.Model):
    _name = "mqtt_interface.robot"

    name = fields.Char(string="Robot Name")
    workcenter_id = fields.Many2one("mrp.workcenter", string="Work Center", help="Work Center where this robot is working")
