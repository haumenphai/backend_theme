from odoo.tests import standalone



@standalone('gg')
def test_standalone_backend_theme(env):
    assert 1+1 == 2
