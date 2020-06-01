#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import datetime
import logging
import json
import base64
import ldap
from jinja2 import Environment, FileSystemLoader

AUDIT_LOGFILE_PATH = "/var/log/render_adminpage.log"
LDAP_SERVER = sys.argv[1]
output_filename = sys.argv[2]

logging.basicConfig(filename=AUDIT_LOGFILE_PATH, filemode='a', format='%(levelname)s: %(asctime)s - %(message)s', level=logging.INFO)

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

def render_adminpage(output_filename):
    exit_status = 0

    # load the adminpage template from the file system
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('adminpage.html')
    users = []
    # separate array created for user info to send in POST request
    users_to_send = []

    for r in res:
        user_name = r[1]['uid'][0].decode("utf-8")

        #default to error styling
        user_status="usererror"
        user_expire = expire_string ="Improperly Configured"

        try:
            user_desc = r[1]['description'][0].decode("utf-8")
            user_expire = parse_expiration_config(user_desc)
            expire_string = user_expire.strftime("%Y-%m-%d %H:%M:%S")
            
            # find diff between current date and expiry date
            time_delta = (user_expire - datetime.datetime.now()).days
            # push style to class
            if time_delta < 0:
                user_status="danger"
            elif 0 <= time_delta < 40:
                user_status="warning"
            else:
                user_status="success"
        except:
            print("Improper configuration for user: {}".format(user_name))
            exit_status = 1
            continue
        finally:
            user = dict(name=user_name, expire=user_expire, status=user_status)
            users.append(user)
            users_to_send.append([user_name, expire_string])

    # convert to JSON to bytes-like object to base64 bytes
    user_info_string = json.dumps(users_to_send)
    message_bytes = user_info_string.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    logging.info("Rendering a page with users: {}".format(users))
    if (exit_status != 0):
        on_error = dict(button_style="disabled", message="Warning: one or more users are improperly configured")
        output_from_parsed_template = template.render(users=users, user_info=base64_message, error=on_error)
    else:
        output_from_parsed_template = template.render(users=users, user_info=base64_message)
    
    # print(output_from_parsed_template)

    # save the results in output_filename
    with open(output_filename, "w") as fh:
        fh.write(output_from_parsed_template)
    
    if (exit_status != 0):
        print("There were improperly configured users")
    return exit_status
    
def main():
    exit_status = render_adminpage(output_filename)
    logging.shutdown()
    if exit_status is not None:
        sys.exit(exit_status)
    else:
        sys.exit(-1)

if __name__ == "__main__":
    main()
