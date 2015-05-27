# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from supplement import Supplement

@pytest.fixture
def app(request):
    fixture = Supplement()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_form_add()
    app.creat_contact(Contact(name_contact="igor", mname_contact="igor2", lname_contact="igor3",
    nick="nick", header="dir", enterprise="app", location="street", j_phone="09876", mail_1="igor@ya.ru",
    mail_2="igor2@ya.ru", web="www", phone_2="home phone", h_phone="54321", m_phone="67890", location_2="street-street",
    note="non",fax="dom"))
    app.logout()

