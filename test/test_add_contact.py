
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="igor", middlename="igor2", lastname="igor3",
    nickname="nick", title="dir", company="app", address="street", home="09876", mobile="54321", work="777",
    fax="222", email="qwerty@yandex.ru", email2="igor@ya.ru", email3="igor2@ya.ru", homepage="www",
    byear="1991", ayear="1991", phone2="home phone", address2="street-street", notes="non")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


