from model.address import Address
import re

class AddressHelper:

    def __init__(self,app):
        self.app = app

    def edit(self, address, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_address_by_index(index)
        wd.find_elements_by_css_selector("img[alt='Edit']")[index].click()
        self.fill_address_form(address)
        self.address_cache = None


    def create(self, address):
        wd = self.app.wd
        self.open_home_page()
        # initial address creation
        wd.find_element_by_link_text("add new").click()
        self.fill_address_form(address)
        self.address_cache = None

    def fill_address_form(self, address):
        wd = self.app.wd
        if address.first_name is not None:
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(address.first_name)
        if address.midle_name is not None:
            wd.find_element_by_name("middlename").click()
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(address.midle_name)
        if address.last_name is not None:
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(address.last_name)
        if address.nick_name is not None:
            wd.find_element_by_name("nickname").click()
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(address.nick_name)
        if address.company is not None:
            wd.find_element_by_name("company").click()
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys(address.company)
        if address.addrs is not None:
            wd.find_element_by_name("address").click()
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(address.addrs)
        if address.home is not None:
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(address.home)
        if address.mobile is not None:
            wd.find_element_by_name("mobile").click()
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(address.mobile)
        if address.work is not None:
            wd.find_element_by_name("work").click()
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(address.work)
        if address.fax is not None:
            wd.find_element_by_name("fax").click()
            wd.find_element_by_name("fax").clear()
            wd.find_element_by_name("fax").send_keys(address.fax)
        if address.email is not None:
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(address.email)
        if address.email is not None:
            wd.find_element_by_name("email2").click()
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys(address.email)
        if address.email2 is not None:
            wd.find_element_by_name("email3").click()
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys(address.email)
        if address.email3 is not None:
            wd.find_element_by_name("phone2").click()
            wd.find_element_by_name("phone2").clear()
            wd.find_element_by_name("phone2").send_keys(address.email)

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']"))) >0:
            wd.find_element_by_link_text("home").click()

    def submit(self):
        wd = self.app.wd
        # submit address creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def delete_first_address(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        # select first address
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()
        self.address_cache = None

    def delete_address_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.select_address_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()
        self.address_cache = None

    def select_address_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    address_cache = None

    def get_address_list(self):
        if self.address_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.address_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                last_name = cells[1].text
                first_name = cells[2].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.address_cache.append(Address(last_name=last_name, first_name=first_name, id=id, all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return list(self.address_cache)

    def get_address_info_from_edit_page(self, index):
        wd = self.app.wd
        self.select_address_by_index(index)
        wd.find_elements_by_css_selector("img[alt='Edit']")[index].click()
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Address(first_name=firstname, last_name=lastname, id=id, home=home, work=work, mobile=mobile, secondaryphone=secondaryphone, email=email, email2=email2, email3=email3)

    def get_address_from_view_page(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_css_selector('img[alt="Details"]')[index].click()
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Address(home=home, work=work, mobile=mobile,
                       secondaryphone=secondaryphone)

    def delete_address_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.select_address_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()
        self.address_cache = None


    def select_address_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        #wd.find_element_by_css_selector("input[value={0}]".format(id)).click()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()




