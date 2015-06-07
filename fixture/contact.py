

class ContactHelper:

    def __init__(self, app):
        self.app = app


    def open_form_add(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()


    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()


    def create(self, contact):
        wd = self.app.wd
        self.open_form_add()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()


    def edit(self, contact):
        wd = self.app.wd
        self.open_home_page()
        self.open_modification_form()
        self.fill_contact_form(contact)
        # submit edit contact
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def open_modification_form(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/select[1]//option[3]").click()
        wd.find_element_by_xpath("//div[@id='content']/form[1]/select[2]//option[3]").click()
        self.change_field_value("byear", contact.byear)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/select[3]//option[4]").click()
        wd.find_element_by_xpath("//div[@id='content']/form[1]/select[4]//option[3]").click()
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def delete_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()


    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.open_modification_form()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()


    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_css_selector("img[alt=\"Edit\"]"))






