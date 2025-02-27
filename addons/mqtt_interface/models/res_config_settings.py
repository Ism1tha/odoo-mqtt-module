from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    mqtt_api_host = fields.Char(
        string="MQTT API Host",
        config_parameter="mqtt_interface.mqtt_api_host",
        default="localhost",
        help="The hostname or IP address of the MQTT broker."
    )
    mqtt_api_port = fields.Integer(
        string="MQTT API Port",
        config_parameter="mqtt_interface.mqtt_api_port",
        default=1883,
        help="The port number for connecting to the MQTT broker."
    )

    def action_open_factory_form(self):
        factory = self.env['manufacturing.factory'].search([], limit=1)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Factory',
            'res_model': 'manufacturing.factory',
            'res_id': factory.id,
            'view_mode': 'form',
            'target': 'current',
        }

