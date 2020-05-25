const http = require('http');
const express = require('express');
const app = express();
const server = http.createServer(app);

app.get('*', function(req, res) {
	res.status(200);
	res.send("You have issued " +
	  req.method +
	  " to the mock endpoint "
	  + req.url
	  + " IF YOU ARE SEEING THIS WITHOUT HAVING AUTHENTICATED, SOMETHING \
	  HAS GONE HORRIBLY WRONG");
});

server.listen(3000, '0.0.0.0');
