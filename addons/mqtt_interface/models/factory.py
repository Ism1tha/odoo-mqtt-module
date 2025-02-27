from odoo import models, fields

class Factory(models.Model):
    _name = 'mqtt_interface.factory'
    _description = 'Factory'

    name = fields.Char(string="Factory Name", required=True)
    warehouse_ids = fields.One2many('mqtt_interface.warehouse', 'factory_id', string="Warehouses")
