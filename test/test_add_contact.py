
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(name_contact="igor", mname_contact="igor2", lname_contact="igor3",
    nick="nick", header="dir", enterprise="app", location="street", j_phone="09876", email2="igor@ya.ru",
    email3="igor2@ya.ru", homepage="www", phone2="home phone", h_phone="54321", m_phone="67890", address2="street-street",
    notes="non",fax="dom", byear="1991", ayear="1991"))


