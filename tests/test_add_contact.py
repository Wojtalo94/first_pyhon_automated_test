# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                home_phone="", mobile_phone="", work_phone="", fax="", email="", email2="", email3="", homepage="",
                bday="-", bmonth="-", byear="", aday="-", amonth="-", ayear="", address2="", phone2="", notes="")] + [
        Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                title=random_string("title", 10), company=random_string("company", 10),
                address=random_string("address", 10), home_phone=random_string("home_phone", 10),
                mobile_phone=random_string("mobile_phone", 10), work_phone=random_string("work_phone", 10),
                fax=random_string("fax", 10), email=random_string("email", 15), email2=random_string("email2", 20),
                email3=random_string("email3", 20), homepage=random_string("homepage", 20),
                bday=str(random.randrange(1, 32)), bmonth=random.choice(months), byear=str(random.randrange(1, 2050)),
                aday=str(random.randrange(1, 32)), amonth=random.choice(months), ayear=str(random.randrange(1, 2050)),
                address2=random_string("address2", 30), phone2=random_string("phone2", 10),
                notes=random_string("notes", 30))
        for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
