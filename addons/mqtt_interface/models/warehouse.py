from odoo import models, fields

class Warehouse(models.Model):
    _name = 'mqtt_interface.warehouse'
    _description = 'Warehouse inside a Factory'

    name = fields.Char(string="Warehouse Name", required=True)
    factory_id = fields.Many2one('mqtt_interface.factory', string="Factory", ondelete="cascade")
    picking_ids = fields.One2many('mqtt_interface.picking', 'warehouse_id', string="Pickings")
