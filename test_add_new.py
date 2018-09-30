# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from address import Address
from application import Application


class AddNew(unittest.TestCase):
    def setUp(self):
        self.app = Application()


    def test_add_new(self):
        self.app.login(username="admin", password="secret")
        self.app.open_add_new_address()
        self.app.create_new_address(Address(first_name="Fname", midle_name="Mname", last_name="Lname", nick_name="NickName",
                                company="Ant", addrs="123", home="123", mobile="123", work="1234", fax="12345",
                                email="a@a.com"))
        self.app.submit()
        self.app.logout()



    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()