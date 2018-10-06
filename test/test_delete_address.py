from model.address import Address

def test_delete_first_group(app):
    if app.address.count() ==0:
        app.address.create(Address(first_name="Fname for deleting", midle_name="Mname for deleting"))
        app.address.submit()
    app.address.delete_first_address()
