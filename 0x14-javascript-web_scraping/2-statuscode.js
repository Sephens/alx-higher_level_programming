#!/usr/bin/node
const request = require('request');
const url = process.argv[2].toString();
request(url, function (err, response, data) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
