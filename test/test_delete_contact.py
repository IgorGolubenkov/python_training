__author__ = 'Игра Света!'


def test_delete_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_contact()
    app.session.logout()

