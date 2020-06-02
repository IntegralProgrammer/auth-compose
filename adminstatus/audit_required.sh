#!/bin/bash
cd /
# If there are improperly configured users, try again once every minute
# for the next 24 hours (1440 minutes)
for trial in `seq 1 1440`
do
	python3 /render_adminpage.py openldap /users_table.html 2>/dev/null >/dev/null && break
	sleep 60
done
touch /var/usersaudit/review_required
