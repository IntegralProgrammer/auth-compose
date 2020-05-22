const fs = require('fs');
const http = require('http');
const express = require('express');
const app = express();
const server = http.createServer(app);

app.get('/adminstatus', function(req, res) {
	res.status(200);
	res.type('html');
	res.send(fs.readFileSync("/users_table.html"));
});

app.post('/adminstatus/confirm', function(req, res) {
	var postData = "";
	req.on('data', function(d) {
		postData += d;
	});
	req.on('end', function() {
		console.log("Authorized Users: " + postData);
		res.status(200);
		res.send("Authorized users confirmed");
	});
});

server.listen(3000, '0.0.0.0');
