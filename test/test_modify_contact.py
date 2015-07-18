
from model.contact import Contact
import random


def test_modify_some_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="igor"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    modify_data = Contact(firstname="vanya")
    app.contact.modify_contact_by_id(contact.id, modify_data)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts.remove(contact)
    new_contacts.remove(modify_data)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
