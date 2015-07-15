
from model.group import Group
import random
import string


testdata = [
    Group(name="name1", footer="footer1", header="header1"),
    Group(name="name2", footer="footer2", header="header2")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


editdata = [
Group(name = random_string("name", 15), header = random_string("header", 20), footer = random_string("footer",20))
for i in range(1)
]
