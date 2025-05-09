from behave import given, when, then
from myapp.auth import autenticar

@given(r'el usuario "(?P<user>[^"]+)" con contraseña "(?P<pass>[^"]+)"')
def step_user(c, user, pass_):
    c.user, c.passwd = user, pass_

@when('intenta iniciar sesión')
def step_try(c):
    c.result = autenticar(c.user, c.passwd)

@then(r'debe ver "(?P<msg>[^"]+)"')
def step_verify(c, msg):
    assert c.result == msg