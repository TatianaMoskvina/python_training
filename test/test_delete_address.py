from model.address import Address
import random

def test_delete_first_group(app, db):
    old_addresses = db.get_address_list()
    if len(db.get_address_list()) ==0:
        app.address.create(Address(first_name="Fname for deleting", midle_name="Mname for deleting"))
        app.address.submit()
    address = random.choice(old_addresses)
    app.address.delete_address_by_id(address.id)
    assert len(old_addresses) - 1 == app.address.count()
    new_addresses = db.get_address_list()
    old_addresses.remove(address)
    assert old_addresses == new_addresses

