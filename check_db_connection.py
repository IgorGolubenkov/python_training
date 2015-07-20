
from fixture.db import DbFixture
from fixture.orm import ORM_fixture
from model.group import Group



db = ORM_fixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contacts_not_in_group(Group(id="80"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass#db.destroy()


#db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

#try:
    #contacts = db.get_contact_list()
    #for contact in contacts:
        #print(contact)
    #print(len(contacts))
    #groups = db.get_group_list()
    #for group in groups:
        #print(group)
    #print(len(groups))
#finally:
    #db.destroy()

