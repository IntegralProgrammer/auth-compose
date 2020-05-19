FROM debian:10

RUN apt-get update
RUN apt-get -y install \
	nginx \
	openssl

COPY proxy.conf /etc/nginx/sites-enabled/default

COPY example.html /var/www/

COPY entrypoint.sh /
RUN chmod u+x /entrypoint.sh

ENTRYPOINT /entrypoint.sh
