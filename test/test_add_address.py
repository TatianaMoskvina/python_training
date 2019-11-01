
from model.address import Address


def test_add_new(app, json_address, db):
    address = json_address
    old_addresses = db.get_address_list()
    app.address.create(address)
    app.address.submit()
    new_addresses = db.get_address_list()
    old_addresses.append(address)
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)


