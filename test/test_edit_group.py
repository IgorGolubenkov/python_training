# -*- coding: utf-8 -*-
__author__ = 'user'

from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="жанна", header="замена", footer="другое"))
    app.session.logout()