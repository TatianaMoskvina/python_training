import re

def test_phones_on_homa_page(app):
    contact_from_home_page = app.address.get_address_list()[0]
    contact_from_edit_page = app.address.get_address_info_from_edit_page(0)
    assert contact_from_home_page.home == clear(contact_from_edit_page.home)
    assert contact_from_home_page.work == clear(contact_from_edit_page.work)
    assert contact_from_home_page.mobile == clear(contact_from_edit_page.mobile)
    assert contact_from_home_page.secondaryphone == clear(contact_from_edit_page.secondaryphone)


def test_phones_on_address_view_page(app):
    contact_from_view_page = app.address.get_address_from_view_page(0)
    contact_from_edit_page = app.address.get_address_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]","", s)