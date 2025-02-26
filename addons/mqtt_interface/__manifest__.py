{
    "name": "Odoo MQTT Interface",
    "summary": "Integrate MQTT communication with Odoo for robotic automation.",
    "description": "A module to integrate MQTT communication with Odoo for robotic automation.",
    "author": "Ismael Semmar Galvez",
    "website": "https://github.com/Ism1tha/odoo-mqtt-module.git",
    "category": "Manufacturing",
    "version": "1.0",
    "license": "GPL-3",
    "depends": ["base", "mrp"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_config_settings.xml",
    ],
    "application": True,
}
