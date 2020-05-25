FROM debian:10

RUN apt-get update
RUN apt-get -y install \
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

COPY adminstatus.js /
ENTRYPOINT nodejs /adminstatus.js
