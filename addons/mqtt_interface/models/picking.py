from odoo import models, fields

class Picking(models.Model):
    _name = 'mqtt_interface.picking'
    _description = 'Picking (PKG) inside Warehouses'

    name = fields.Char(string="Picking Code", required=True)
    warehouse_id = fields.Many2one('mqtt_interface.warehouse', string="Warehouse", ondelete="cascade")
    robot_ids = fields.One2many('mqtt_interface.robot', 'picking_id', string="Robots")
    status = fields.Selection([
        ('pending', 'Pending'),
        ('processed', 'Processed'),
        ('canceled', 'Canceled')
    ], string="Status", default="pending")
