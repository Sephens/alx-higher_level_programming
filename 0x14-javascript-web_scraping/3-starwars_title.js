#!/usr/bin/node
const request = require('request');
const num = process.argv[2];
const url = (`https://swapi.co/api/films/${num}`);
request(url, function (err, response, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(data).title);
  }
});
