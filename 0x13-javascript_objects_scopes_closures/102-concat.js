#!/usr/bin/node
const fs = require('fs');
const path = require('path');

process.argv.slice(2, -1).forEach((element) => {
  const filePath = path.join(__dirname, element.toString());

  fs.readFile(filePath, { encoding: 'utf-8' }, (err, data) => {
    if (!err) {
      fs.appendFile(process.argv.slice(-1).toString(), `${data}\n`, (err) => {
        if (err) {
          console.log(err);
        }
      });
    }
  });
});
