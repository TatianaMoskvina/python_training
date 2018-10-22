
from model.address import Address

def test_add_new(app):
    old_addresses = app.address.get_address_list()
    address = Address(first_name="Fname", midle_name="Mname", last_name="Lname", nick_name="NickName",
                              company="Ant", addrs="123", home="123", mobile="123", work="1234", fax="12345",
                              email="a@a.com", email2="a@a.com", email3="a@a.com", secondaryphone="123")
    app.address.create(address)
    app.address.submit()
    assert len(old_addresses) + 1 == app.address.count()
    new_addresses = app.address.get_address_list()
    old_addresses.append(address)
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)




