__author__ = 'user'


from model.contact import Contact

def test_edit_contact(app):
    app.open_home_page()

    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(name_contact="ganna", mname_contact="ganna2", lname_contact="ganna",
    nick="cate", header="neft", enterprise="gazprom", location="avenu", j_phone="666", mail_1="ganna@ya.ru",
    mail_2="ganna2@ya.ru", web="www.yandex.ru", phone_2="13666", h_phone="131313", m_phone="66613", location_2="lenina",
    note="No",fax="dom", byear="1991", ayear="1991"))
    app.session.logout()
