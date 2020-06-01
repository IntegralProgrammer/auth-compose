#!/bin/bash

#Get the domain name
echo "Enter the domain name:"
read DOMAIN_NAME
export DOMAIN_NAME

#Get the host IP address as viewed from inside a Docker container
echo "Enter Docker host IP:"
read DOCKER_HOST_IP
export DOCKER_HOST_IP

#Generate some secrets
export JWT_SECRET=$(cat /dev/urandom | head -c 32 | sha256sum - | head -c 64)
export SESSION_SECRET=$(cat /dev/urandom | head -c 32 | sha256sum - | head -c 64)

#These variables should not be substituted
export cookie_authelia_session='$cookie_authelia_session'

#Render template for configuration.yml
envsubst < configuration.yml.template > configuration.yml

#Render template for nginx/proxy.conf
envsubst < nginx/proxy.conf.template > nginx/proxy.conf
