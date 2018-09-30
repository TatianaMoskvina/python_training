
import pytest
from model.address import Address
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new(app):
    app.session.login(username="admin", password="secret")
    app.address.create(Address(first_name="Fname", midle_name="Mname", last_name="Lname", nick_name="NickName",
                              company="Ant", addrs="123", home="123", mobile="123", work="1234", fax="12345",
                              email="a@a.com"))
    app.address.submit()
    app.session.logout()


