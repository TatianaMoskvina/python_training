


from model.address import Address

def test_edit_address(app):
    app.address.edit(Address(first_name="Firstname (edited)", midle_name="MidleName (edited)", last_name="Lastname (edited)", nick_name="NickName (edited)",
                              company="Ant (edited)", addrs="123 (edited)", home="123 (edited)", mobile="123 (edited)", work="1234 (edited)", fax="12345 (edited)",
                              email="a@a.com (edited)"))



