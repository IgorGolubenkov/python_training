

from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="игорь"))
    app.group.edit_first_group(Group(name="жанна", header="замена", footer="другое"))
