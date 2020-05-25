FROM debian:10

RUN apt-get update
RUN apt-get -y install \
	nginx \
	openssl \
	wget

WORKDIR /var/www/
RUN wget https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css
RUN wget https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js
RUN wget https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js
WORKDIR /

RUN mkdir -p /etc/ssl/private
RUN chmod 700 /etc/ssl/private
RUN mkdir -p /etc/ssl/certs

COPY proxy.conf /etc/nginx/sites-enabled/default
COPY example.html /var/www/

COPY entrypoint.sh /
RUN chmod u+x /entrypoint.sh

ENTRYPOINT /entrypoint.sh
