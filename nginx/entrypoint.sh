#!/bin/bash

#Setup a self-signed TLS certificate
mkdir -p /etc/ssl/private
chmod 700 /etc/ssl/private
mkdir -p /etc/ssl/certs

echo -ne '\n\n\n\n\n\n\n\n\n\n' | openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/selfsigned.key -out /etc/ssl/certs/selfsigned.crt

nginx -g 'daemon off;'
