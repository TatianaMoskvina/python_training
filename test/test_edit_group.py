# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    if app.group.count() ==0:
        app.group.create(Group(name="test edit"))
    app.group.edit(Group(name="GroupName (edited)", footer="GroupFooter (edited)"))
