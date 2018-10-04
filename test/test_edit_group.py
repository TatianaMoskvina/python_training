# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.edit(Group(name="GroupName (edited)", footer="GroupFooter (edited)"))
