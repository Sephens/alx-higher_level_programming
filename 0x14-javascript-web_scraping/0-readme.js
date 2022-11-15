#!/usr/bin/node
const fs = require('fs');
const file = (process.argv[2].toString());
fs.readFile(file, function read (err, data) {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
