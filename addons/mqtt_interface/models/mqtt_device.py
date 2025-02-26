from odoo import models, fields, api

class MQTTDevice(models.Model):
    _name = "mqtt_interface.device"
    _description = "MQTT Device"

    name = fields.Char("Device Name", required=True, help="The human-readable name of the device.")
    device_code = fields.Char("Device Code", required=True, index=True, unique=True, help="A unique identifier for the device.")
    status = fields.Selection([
        ('online', 'Online'),
        ('offline', 'Offline')
    ], string="Status", default="offline", readonly=True, tracking=True)
    last_check = fields.Datetime("Last Check", readonly=True, help="The last time the device status was checked.")
