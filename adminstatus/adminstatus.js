const http = require('http');
const express = require('express');
const app = express();
const server = http.createServer(app);

app.get('/', function(req, res) {
	res.status(200);
	res.send("This is the status page for the admin");
});

server.listen(3000, '0.0.0.0');
