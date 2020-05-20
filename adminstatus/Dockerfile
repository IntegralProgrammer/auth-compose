FROM debian:10

RUN apt-get update
RUN apt-get -y install \
	nodejs \
	node-express \
	python3 \
	python3-ldap

COPY delete_expired_users.py /
COPY delete_user.py /
COPY list_users.py /

COPY adminstatus.js /
ENTRYPOINT nodejs /adminstatus.js
