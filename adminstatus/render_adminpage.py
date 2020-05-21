#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import datetime
import json

import ldap
from jinja2 import Environment, FileSystemLoader

LDAP_SERVER = sys.argv[1]
output_filename = sys.argv[2]
output_filename = "test.txt"

def parse_expiration_config(s):
	s_split = s.split(' ')
	if len(s_split) != 2:
		raise Exception("Improper date format")
	if s_split[0] != "expires:":
		raise Exception("Improper date format")
	s_date = s_split[1].split('/')
	if len(s_date) != 3:
		raise Exception("Improper date format")
	s_year = int(s_date[0])
	s_month = int(s_date[1])
	s_day = int(s_date[2])
	return datetime.datetime(year=s_year, month=s_month, day=s_day)
	
con = ldap.initialize("ldap://" + LDAP_SERVER)
con.simple_bind_s("cn=admin,dc=example,dc=org", "admin")
res = con.search_s("dc=example,dc=org", ldap.SCOPE_SUBTREE, "uid=*")
exit_status = 0

def render_adminpage(output_filename):
    # load the adminpage template from the file system
    # not sure if this should go in function or not
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('adminpage.html')
    users = []
    # separate array created for user info to send in POST request
    users_to_send = []

    for r in res:
        user_name = r[1]['uid'][0].decode("utf-8")
        try:
            user_desc = r[1]['description'][0].decode("utf-8")
            user_expire = parse_expiration_config(user_desc)
            # find diff between current date and expiry date
            time_delta = (user_expire - datetime.datetime.now()).days
            # push style to class
            if time_delta < 0:
                user_status="danger"
            elif 0 <= time_delta < 7:
                user_status="warning"
            else:
                user_status="success"
        except:
            print("Improper configuration for user: {}".format(user_name))
            exit_status = 1
            continue
        user = dict(name=user_name, expire=user_expire, status=user_status)
        users.append(user)
        users_to_send.append([user_name, expire_string])

    # # to test html styling
    # for i in range(1, 9):
    #     i = str(i)
    #     user_name = "test" + i
    #     try:
    #         user_expire = parse_expiration_config("expires: 2020/0" + i + "/23")
    #         expire_string = user_expire.strftime("%Y-%m-%d %H:%M:%S")
    #         # find diff between current date and expiry date
    #         time_delta = (user_expire - datetime.datetime.now()).days
    #         # push style to class
    #         if time_delta < 0:
    #             user_status="danger"
    #         elif 0 <= time_delta < 7:
    #             user_status="warning"
    #         else:
    #             user_status="success"
    #     except:
    #         print("Improper configuration for user: {}".format(user_name))
    #         exit_status = 1
    #         continue
    #     user = dict(name=user_name, expire=user_expire, status=user_status)
    #     users.append(user)
    #     users_to_send.append([user_name, expire_string])

    # # end of testing html style

    output_from_parsed_template = template.render(users=users)
    # print(output_from_parsed_template)

    # save the results in output_filename
    with open(output_filename, "w") as fh:
        fh.write(output_from_parsed_template)
    
    # todo: how to use this json
    test = json.dumps(users_to_send)
    print(test)

def main():
    render_adminpage(output_filename)

if __name__ == "__main__":
    main()

if (exit_status != 0):
    print("There were improperly configured users")
sys.exit(exit_status)