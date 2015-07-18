
from model.contact import Contact
import random
import string
import jsonpickle
import os.path
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_number(maxlen):
    symbols = string.digits + " "*10 + "+" + "-"*4
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#def random_rus_symbols(maxlen):
    #rus_symbols = string.l
    #return "".join([random.choice(rus_symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="",nickname="", title="", company="", address="",
                    home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="",
                    byear="", ayear="", phone2="", address2="", notes="")] + [
    Contact(firstname = random_string("firstname", 10), middlename = random_string("middlename", 15), lastname = random_string("lastname", 15),
            nickname = random_string("nickname", 25), title = random_string("title", 20), company = random_string("company", 25),
            address = random_string("address", 40), home = random_number(30), mobile = random_number(25),
            work = random_number(30), fax = random_number(25),
            email = random_string("email", 20), email2 = random_string("email2", 20), email3 = random_string("email3", 15),
            byear="1991", ayear="1991",
            phone2 = random_number(30), address2 = random_string("address2", 40), notes = random_string("notes", 30))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))