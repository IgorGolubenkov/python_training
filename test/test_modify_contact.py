
from model.contact import Contact


def test_modify_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="igor"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(address="street"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)