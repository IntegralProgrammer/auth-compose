#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import datetime

import ldap
from jinja2 import Environment, FileSystemLoader


# LDAP_SERVER = sys.argv[1]

# def parse_expiration_config(s):
# 	s_split = s.split(' ')
# 	if len(s_split) != 2:
# 		raise Exception("Improper date format")
# 	if s_split[0] != "expires:":
# 		raise Exception("Improper date format")
# 	s_date = s_split[1].split('/')
# 	if len(s_date) != 3:
# 		raise Exception("Improper date format")
# 	s_year = int(s_date[0])
# 	s_month = int(s_date[1])
# 	s_day = int(s_date[2])
# 	return datetime.datetime(year=s_year, month=s_month, day=s_day)
	
	

# con = ldap.initialize("ldap://" + LDAP_SERVER)
# con.simple_bind_s("cn=admin,dc=example,dc=org", "admin")
# res = con.search_s("dc=example,dc=org", ldap.SCOPE_SUBTREE, "uid=*")
exit_status = 0

# load the adminpage template from the file system
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('adminpage.html')

# todo: take in variable output_filename
def render_adminpage():
    users = []

    # for r in res:
    #     user_name = r[1]['uid'][0].decode("utf-8")
    #     try:
    #         user_desc = r[1]['description'][0].decode("utf-8")
    #         user_expire = parse_expiration_config(user_desc)
    #         # todo: find diff between current date and expiry date --> push to classname
    #         # user_diff = user_expire - datetime.datetime.now()
    #     except:
    #         print("Improper configuration for user: {}".format(user_name))
    #         exit_status = 1
    #         continue
    #     user = dict(name=user_name, expire=user_expire)
    #     users.append(user)

    # to test html styling
    for i in range(1, 9):
        i = str(i)
        user_name = "test" + i
        try:
            user_expire = "2020-05-31 00:00:0" + i
            # todo: find diff between current date and expiry date --> push to classname
            # user_diff = user_expire - datetime.datetime.now()
        except:
            print("Improper configuration for user: {}".format(user_name))
            # exit_status = 1
            continue
        user = dict(name=user_name, expire=user_expire)
        users.append(user)

    output_from_parsed_template = template.render(users=users)
    # print(output_from_parsed_template)

    # to save the results
    # todo: write to variable output_filename
    with open("test.html", "w") as fh:
        fh.write(output_from_parsed_template)


# if (exit_status != 0):
#     print("There were improperly configured users")
# sys.exit(exit_status)