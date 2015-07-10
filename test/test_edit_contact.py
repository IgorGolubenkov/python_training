

import pytest
from model.contact import Contact
from data.contacts import data_edit


@pytest.mark.parametrize("contact", data_edit, ids=[repr(x) for x in data_edit])
def test_edit_contact(app, contact):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="igor"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
