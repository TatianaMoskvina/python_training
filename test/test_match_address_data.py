import re
from random import randrange

def test_data_on_home_page(app):
    old_addresses = app.address.get_address_list()
    if app.address.count() == 0:
        app.address.create(Address(first_name="Fname", midle_name="Mname", last_name="Lname", nick_name="NickName",
                              company="Ant", addrs="123", home="123", mobile="123", work="1234", fax="12345",
                              email="a@a.com", email2="a@a.com", email3="a@a.com", secondaryphone="123"))
        app.address.submit()
    index = randrange(len(old_addresses))
    contact_from_home_page = app.address.get_address_list()[index]
    contact_from_edit_page = app.address.get_address_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name

def clear(s):
    return re.sub("[() -]","", s)

def merge_phones_like_on_home_page(address):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [address.home, address.mobile,address.work, address.secondaryphone]))))

def merge_emails_like_on_home_page(address):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [address.email, address.email2, address.email3])))