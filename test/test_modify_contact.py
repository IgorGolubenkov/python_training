
from model.contact import Contact


def test_modify_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="igor"))
    app.contact.modify_first_contact(Contact(address="street"))