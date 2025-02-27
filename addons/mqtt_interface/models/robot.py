from odoo import models, fields

class Robot(models.Model):
    _name = 'mqtt_interface.robot'
    _description = 'Robots inside Pickings'

    name = fields.Char(string="Robot Name", required=True)
    picking_id = fields.Many2one('mqtt_interface.picking', string="Picking", ondelete="cascade")
    type = fields.Selection([
        ('welding', 'Welding'),
        ('assembly', 'Assembly'),
        ('transport', 'Transport')
    ], string="Robot Type")
