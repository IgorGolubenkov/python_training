
from model.contact import Contact


def test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(name_contact="igor", mname_contact="igor2", lname_contact="igor3",
    nick="nick", header="dir", enterprise="app", location="street", j_phone="09876", mail_1="igor@ya.ru",
    mail_2="igor2@ya.ru", web="www", phone_2="home phone", h_phone="54321", m_phone="67890", location_2="street-street",
    note="non",fax="dom", byear="1991", ayear="1991"))
    app.session.logout()


def test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(name_contact="igor", mname_contact="igor2", lname_contact="igor3",
    nick="nick", header="dir", enterprise="app", location="street", j_phone="09876", mail_1="igor@ya.ru",
    mail_2="igor2@ya.ru", web="www", phone_2="home phone", h_phone="54321", m_phone="67890", location_2="street-street",
    note="non",fax="dom", byear="1991", ayear="1991"))
    app.session.logout()

