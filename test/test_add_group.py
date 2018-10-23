# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import string
import random

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits+ string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
        Group(name="", header="", footer="")] + [
        Group(name=random_string("GroupName", 10), header=random_string("GroupHeader", 10), footer=random_string("GroupFooter", 20))
        for i in range(5)

]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups,key=Group.id_or_max)





