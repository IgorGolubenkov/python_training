
from fixture.db import DbFixture
from fixture.orm import ORM_fixture
from model.group import Group
import re


db = ORM_fixture(host="127.0.0.1", name="addressbook", user="root", password="")

#try:
    #l = db.get_contacts_not_in_group(Group(id="80"))
    #for item in l:
        #print(item)
    #print(len(l))
#finally:
    #pass#db.destroy()


db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    contacts = db.get_contact_list_on_home_page()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()
    #groups = db.get_group_list()
    #for group in groups:
        #print(group)
    #print(len(groups))

def clear(s):
    return re.sub("[() -]", "", s)


def merge_all_list_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.id, contact.lastname, contact.firstname, contact.address,
                                        contact.email, contact.email2, contact.email3,
                                        contact.home, contact.mobile, contact.work, contact.phone2]))))
