from model.address import Address

def test_delete_first_group(app):
    old_addresses = app.address.get_address_list()
    if app.address.count() ==0:
        app.address.create(Address(first_name="Fname for deleting", midle_name="Mname for deleting"))
        app.address.submit()
    app.address.delete_first_address()
    new_addresses = app.address.get_address_list()
    assert len(old_addresses) - 1 == len(new_addresses)
    old_addresses[0:1] = []
    assert old_addresses == new_addresses

