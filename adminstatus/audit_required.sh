#!/bin/bash
cd /
python3 /render_adminpage.py openldap /users_table.html 2>/dev/null >/dev/null
touch /var/usersaudit/review_required
