# -*- coding: utf-8 -*-
# Copyright 2016, 2019 Openworx - Mario Gielissen
# Copyright 2012, 2019 Openworx - T.V.T Marine Automation
# Copyright 2019,2021 Viindoo
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Dotd Backend Theme",
    "summary": "Backend theme for Odoo community",
    "version": "1.0.23",
	"description": """Dotd Backend Theme""",

    'author': 'Openworx,T.V.T Marine Automation,Viindoo, Dotd',
    'website': 'https://viindoo.com',
    'live_test_url': 'https://v13demo-int.erponline.vn',
    'support': 'apps.support@viindoo.com',

    'category': 'Website/Theme/Backend',
    "depends": ['web', 'web_editor', 'web_responsive'],
    "data": [
        'views/assets.xml',
		'views/res_company_view.xml',
    ],
    'images': [
        'images/screen.png'
    ],
    'installable': True,
    'application': False,
    'auto_install': ['web'],
    'price': 99.9,
    'currency': 'EUR',
    'license': 'LGPL-3',
}

