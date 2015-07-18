

from model.group import Group
import random
from random import randrange


def test_edit_group_by_id(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="игорь"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    edit_data = Group(name="igor", header="dream", footer="sun")
    app.group.edit_group_by_id(group.id, edit_data)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups.remove(group)
    new_groups.remove(edit_data)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        ui_assert_db_list = db.get_group_list()
        assert sorted(ui_assert_db_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)




