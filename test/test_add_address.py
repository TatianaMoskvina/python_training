
from model.address import Address
import pytest
import string
import random

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits+ string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_number(prefix, maxlen):
    symbols = string.digits+" "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
        Address(first_name="", midle_name="", last_name= "", nick_name="", company="", addrs="") ] + [
        Address(first_name=random_string("first_name", 10), midle_name=random_string("midle_name", 10), last_name=random_string("last_name", 20),
                company=random_string("company", 10), addrs=random_string("address",10), home=random_number("1",20), mobile=random_number("1", 30),
                work=random_number("1", 30), fax=random_number("1",20), email=random_string("e@", 10), secondaryphone=random_number("8913", 13))
        for i in range(5)]

@pytest.mark.parametrize("address", testdata, ids=[repr(x) for x in testdata])
def test_add_new(app, address):
    old_addresses = app.address.get_address_list()
    app.address.create(address)
    app.address.submit()
    assert len(old_addresses) + 1 == app.address.count()
    new_addresses = app.address.get_address_list()
    old_addresses.append(address)
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)





