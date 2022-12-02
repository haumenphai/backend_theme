# -*- coding: utf-8 -*-
# Copyright 2016, 2019 Openworx - Mario Gielissen
# Copyright 2012, 2019 Openworx - T.V.T Marine Automation
# Copyright 2019,2021 Viindoo
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": "Dotd Backend Theme",
    "summary": "Mobile backend theme for Odoo community",
	"description": """Dotd Backend Theme""",
    'author': 'Openworx,T.V.T Marine Automation,Viindoo',

    'category': 'Website/Theme/Backend',
    'version': '0.1.0',

    "depends": ['web', 'web_editor', 'web_responsive'],
    "data": [
        'views/assets.xml',
		'views/res_company_view.xml',
    ],
    'images': ['images/screen.png'],
    'installable': True,
    'auto_install': ['web'],
    'license': 'LGPL-3',
}

