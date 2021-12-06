# -*- coding: utf-8 -*-
# (C) 2019 Smile (<https://www.smile.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Database Upgrade",
    "version": "15.0.1",
    "depends": ["web"],
    "author": "Smile",
    "license": 'AGPL-3',
    "description": "",
    "summary": "",
    "website": "",
    "category": 'Tools',
    "sequence": 20,
    "data": [
    ],
    "auto_install": True,
    "installable": True,
    "application": False,
    "assets": {
        'web.assets_backend': [
            'smile_upgrade/static/src/css/code_version.css',
            'smile_upgrade/static/src/js/code_version.js'
        ],
        'web.assets_qweb': [
            'smile_upgrade/static/src/xml/**/*',
        ],
    },
}
