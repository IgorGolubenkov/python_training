
import re
from model.contact import Contact


def test_db_matches_ui_list_all_contact_on_home_page(app, db):
    ui_all_contact = app.contact.get_contact_list()
    db_all_contact = db.get_contact_list_on_home_page()
    assert sorted(db_all_contact, key=Contact.id_or_max) == sorted(ui_all_contact, key=Contact.id_or_max)


#def test_contact_home_with_edit_pages(app):
    #contact_all_list_home_page = app.contact.get_contact_list()[0]
    #contact_all_list_edit_page = app.contact.get_contact_info_edit_from_page(0)
    #assert contact_all_list_home_page.firstname == clear(contact_all_list_edit_page.firstname)
    #assert contact_all_list_home_page.lastname == clear(contact_all_list_edit_page.lastname)
    #assert contact_all_list_home_page.address == clear(contact_all_list_edit_page.address)
    #assert contact_all_list_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_all_list_edit_page)
    #assert contact_all_list_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_all_list_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_all_list_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.lastname, contact.firstname, contact.address,
                                        contact.email, contact.email2, contact.email3,
                                        contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
