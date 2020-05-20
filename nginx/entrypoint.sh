#!/bin/bash

if [ ! -f /etc/ssl/private/cert.key ]
then
	#Setup a self-signed TLS certificate if no SSL cert/key pair is provided
	echo -ne '\n\n\n\n\n\n\n\n\n\n' | openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/cert.key -out /etc/ssl/certs/cert.crt
fi

nginx -g 'daemon off;'
