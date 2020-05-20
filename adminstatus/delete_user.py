#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import ldap

LDAP_SERVER = sys.argv[1]

userid = str(input("User:"))
con = ldap.initialize("ldap://" + LDAP_SERVER)
con.simple_bind_s("cn=admin,dc=example,dc=org", "admin")
dn = "uid={},dc=example,dc=org".format(userid)
con.delete_s(dn)

print("Deleted the user {}.".format(userid))
