
from model.address import Address

def test_add_new(app):
    old_addresses = app.address.get_address_list()
    app.address.create(Address(first_name="Fname", midle_name="Mname", last_name="Lname", nick_name="NickName",
                              company="Ant", addrs="123", home="123", mobile="123", work="1234", fax="12345",
                              email="a@a.com"))
    app.address.submit()
    new_adresses = app.address.get_address_list()
    assert len(old_addresses) + 1 == len(new_adresses)




