from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    mqtt_api_host = fields.Char(
        string="MQTT API Host",
        config_parameter="mqtt_module.mqtt_api_host",
        default="localhost"
    )
    mqtt_api_port = fields.Char(
        string="MQTT API Port",
        config_parameter="mqtt_module.mqtt_api_port",
        default="1883"
    )

    @api.constrains("mqtt_api_port")
    def _check_mqtt_api_port(self):
        for record in self:
            if not record.mqtt_api_port.isdigit():
                raise ValidationError("MQTT API Port must be numeric.")
