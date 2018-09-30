# -*- coding: utf-8 -*-

import pytest
from address import Address
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    return fixture
    request.addfinalizer(fixture.destroy)




def test_add_new(app):
    app.login(username="admin", password="secret")
    app.open_add_new_address()
    app.create_new_address(Address(first_name="Fname", midle_name="Mname", last_name="Lname", nick_name="NickName",
                                company="Ant", addrs="123", home="123", mobile="123", work="1234", fax="12345",
                                email="a@a.com"))
    app.submit()
    app.logout()

