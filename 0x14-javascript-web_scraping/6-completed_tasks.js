#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const dict = {};
request(url, function (err, request, body) {
  if (err) {
    console.log(err);
  } else {
    for (const i of JSON.parse(body)) {
      if (i.completed === true) {
        if (dict[i.userId]) {
          dict[i.userId]++;
        } else {
          dict[i.userId] = 1;
        }
      }
    }
    console.log(dict);
  }
});
