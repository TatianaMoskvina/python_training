# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import pytest
from model.address import Address
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new(app):
    app.login(username="admin", password="secret")
    app.create_new_address(Address(first_name="Fname", midle_name="Mname", last_name="Lname", nick_name="NickName",
                                company="Ant", addrs="123", home="123", mobile="123", work="1234", fax="12345",
                                email="a@a.com"))
    app.submit()
    app.logout()


