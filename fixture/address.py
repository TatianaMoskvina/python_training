from model.address import Address

class AddressHelper:

    def __init__(self,app):
        self.app = app

    def edit(self, address, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_address_by_index(index)
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
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
                self.address_cache.append(Address(last_name=cells[1].text,first_name=cells[2].text, id=id))
        return list(self.address_cache)
