from sys import maxsize

class Address:
    def __init__(self, first_name=None, midle_name=None, last_name=None, nick_name=None, company=None, addrs=None, home=None, mobile=None, work=None, fax=None,
         email=None, email2=None, email3=None, id=None, name = None, secondaryphone=None, all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.first_name = first_name
        self.midle_name = midle_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.company = company
        self.addrs = addrs
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id
        self.name = name
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s;%s" % (self.id)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

