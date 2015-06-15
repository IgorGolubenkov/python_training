

from model.contact import Contact

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="igor"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit(Contact(firstname="ganna", middlename="ganna2", lastname="ganna3",
    nickname="cate", title="neft", company="gazprom", address="avenu", home="666", mobile="131313", work="777",
    fax="222", email="ganna@ya.ru", email2="ganna2@ya.ru", email3="derty@ya.ru", homepage="www.yandex.ru",
    byear="2002", ayear="2020", phone2="13666", address2="lenina", notes="No"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)