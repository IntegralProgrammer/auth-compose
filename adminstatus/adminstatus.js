const fs = require('fs');
const http = require('http');
const express = require('express');
const querystring = require('querystring');

const app = express();
const server = http.createServer(app);

app.get('/adminstatus', function(req, res) {
	//Is a authorized users review required?
	if (fs.existsSync('/var/usersaudit/review_required')) {
		res.status(200);
		res.type('html');
		res.send(fs.readFileSync("/users_table.html"));
	}
	else {
		res.redirect('/');
	}
});

app.post('/adminstatus/confirm', function(req, res) {
	var postData = "";
	req.on('data', function(d) {
		postData += d;
	});
	req.on('end', function() {
		var urlDecoded = querystring.decode(postData);
		var listBuffer = new Buffer(urlDecoded.users, 'base64');
		var postDataJson = JSON.parse(listBuffer.toString('ascii'));
		var logMessage = "[";
		logMessage += new Date().toString();
		logMessage += "] ";
		logMessage += JSON.stringify(postDataJson);
		logMessage += "\n";
		fs.appendFileSync('/var/log/adminstatus.log', logMessage);
		res.status(200);
		res.send("Authorized users confirmed");
		fs.unlinkSync('/var/usersaudit/review_required');
	});
});

server.listen(3000, '0.0.0.0');
