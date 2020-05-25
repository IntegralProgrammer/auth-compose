FROM debian:10

RUN apt-get update
RUN apt-get -y install \
	cron \
	nodejs \
	node-express \
	python3 \
	python3-ldap \
	python3-pip

RUN pip3 install jinja2
COPY delete_expired_users.py /
COPY delete_user.py /
COPY list_users.py /
COPY render_adminpage.py /
COPY templates /templates
COPY crontab /etc/cron.d/simple-cron
COPY audit_required.sh /

RUN chmod 0644 /etc/cron.d/simple-cron
RUN chmod +x /audit_required.sh
RUN mkdir /var/usersaudit

COPY adminstatus.js /
CMD cron && nodejs /adminstatus.js
