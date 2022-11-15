#!/usr/bin/node
const fs = require('fs');
const file = (process.argv[2].toString());
const content = (process.argv[3].toString());
fs.writeFile(file, content, function (err) {
  if (err) {
    return console.log(err);
  }
});
