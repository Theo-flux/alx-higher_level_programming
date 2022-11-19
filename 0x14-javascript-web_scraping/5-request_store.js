#!/usr/bin/node
const request = require('request');
const { writeFileSync } = require('fs');

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    writeFileSync(process.argv[3], body, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
