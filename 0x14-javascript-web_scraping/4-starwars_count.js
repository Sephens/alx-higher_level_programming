#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let counter = 0;
request(url, function (err, request, body) {
  if (err) {
    console.log(err);
  } else {
    for (const movie of JSON.parse(body).results) {
      for (const character of movie.characters) {
        if (character.includes('18')) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
