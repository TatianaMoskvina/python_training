# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="GroupName (edited)", header="GroupHeader (edited)", footer="GroupFooter (edited)"))
    app.session.logout()