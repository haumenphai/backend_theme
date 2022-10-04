# Copyright 2016, 2019 Openworx - Mario Gielissen
# Copyright 2012, 2019 Openworx - T.V.T Marine Automation
# Copyright 2019,2021 Viindoo
# Copyright 2022 vjpthe.pro
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Vjpthe.pro Backend Theme",
    "summary": "Mobile backend theme for Odoo community",
    "version": "1.0.23",
    'author': 'Openworx,T.V.T Marine Automation,Viindoo, vjpthe.pro',
    'website': 'https://vjpthe.pro',
    'support': 'https://vjpthe.pro',
    'category': 'Website/Theme/Backend',
    "depends": ['web', 'web_editor', 'web_responsive'],
    "data": [
        'views/web.xml'
    ],
    'images': [
        # 'images/screen.png'
    ],
    'assets': {
        'web.assets_backend': [
            ('after', '/web_responsive/static/src/legacy/scss/web_responsive.scss', '/to_backend_theme/static/src/legacy/scss/web_responsive.scss'),
            ('after', '/web_responsive/static/src/components/apps_menu/apps_menu.scss', 'to_backend_theme/static/src/scss/apps_menu.scss'),
            'to_backend_theme/static/src/scss/style.scss',
            'to_backend_theme/static/src/scss/discuss.scss',
            ],
        'web._assets_primary_variables': [
            'to_backend_theme/static/src/scss/primary_vars.scss',
        ],
    },
    'installable': True,
    'price': 99.9,
    'currency': 'EUR',
    'license': 'LGPL-3',
}
