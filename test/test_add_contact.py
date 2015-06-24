
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_number(maxlen):
    symbols =  string.digits + " "*10 + "+" + "-"*4
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



testdata = [Contact(firstname="igor", middlename="igor2", lastname="igor3",
    nickname="nick", title="dir", company="app", address="street", home="09876", mobile="54321", work="777",
    fax="222", email="qwerty@yandex.ru", email2="igor@ya.ru", email3="igor2@ya.ru", homepage="www",
    byear="1991", ayear="1991", phone2="home phone", address2="street-street", notes="non")] + [
    Contact(firstname = random_string("firstname", 15), middlename = random_string("middlename", 15), lastname = random_string("lastname", 15),
            nickname = random_string("nickname", 25), title = random_string("title", 20), company = random_string("company", 25),
            address = random_string("address", 40), home = random_number(30), mobile = random_number(25),
            work = random_number(30), fax = random_number(25),
            email = random_string("email", 20), email2 = random_string("email2", 20), email3 = random_string("email3", 15),
            byear="1991", ayear="1991",
            phone2 = random_number(30), address2 = random_string("address2", 40), notes = random_string("notes", 30))
]


@pytest.mark.parametrize("contact", testdata)
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


