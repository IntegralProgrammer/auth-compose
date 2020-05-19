FROM debian:10

RUN apt-get update
RUN apt-get -y install \
	nodejs \
	node-express

COPY adminstatus.js /
ENTRYPOINT nodejs /adminstatus.js
