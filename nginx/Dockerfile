FROM debian:10

RUN apt-get update
RUN apt-get -y install \
	nginx \
	openssl

RUN mkdir -p /etc/ssl/private
RUN chmod 700 /etc/ssl/private
RUN mkdir -p /etc/ssl/certs

COPY proxy.conf /etc/nginx/sites-enabled/default

COPY example.html /var/www/

COPY entrypoint.sh /
RUN chmod u+x /entrypoint.sh

ENTRYPOINT /entrypoint.sh
