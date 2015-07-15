

from model.contact import Contact
import re


class ContactHelper:


    def __init__(self, app):
        self.app = app


    def open_form_add(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()


    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_css_selector('img[alt="Edit"]')) > 0):
            wd.find_element_by_link_text("home").click()


    def create(self, contact):
        wd = self.app.wd
        self.open_form_add()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()
        self.contact_cache = None


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
        wd.find_element_by_css_selector('img[alt="Edit"]').click()


    def open_modification_form_by_index(self, index):
        wd = self.app.wd
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()


    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_css_selector('img[alt="Edit"]')) > 0):
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
        self.delete_contact_by_index(0)


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.contact_cache = None


    def modify_first_contact(self):
        self.modify_contact_by_index(0)


    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.open_modification_form_by_index(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None


    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_css_selector('img[alt="Edit"]'))


    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_phones = cells[5].text
                all_email = cells[4].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname,
                                                  address=address, all_email_from_home_page=all_email,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)


    def get_contact_info_edit_from_page(self, index):
        wd = self.app.wd
        self.open_modification_form_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        phone_2_phone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       address=address, email=email, email2=email2, email3=email3,
                       home=homephone, work=workphone,
                       mobile=mobilephone, phone2=phone_2_phone)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        phone_2_phone = re.search("P: (.*)", text).group(1)
        return Contact(home=homephone, work=workphone,
                       mobile=mobilephone, phone2=phone_2_phone)







