from model.address import Address
import string
import random
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/address.json"

for o,a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits+ string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(prefix, maxlen):
    symbols = string.digits+" "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
        Address(first_name="", midle_name="", last_name= "", nick_name="", company="", addrs="") ] + [
        Address(first_name=random_string("first_name", 10), midle_name=random_string("midle_name", 10), last_name=random_string("last_name", 20),
                company=random_string("company", 10), addrs=random_string("address",10), home=random_number("1",20), mobile=random_number("1", 30),
                work=random_number("1", 30), fax=random_number("1",20), email=random_string("e@", 10), secondaryphone=random_number("8913", 13))
        for i in range(5)]



file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file,"w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))