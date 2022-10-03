#!/usr/bin/node
const { argv0 } = require('node:process');

if (argv0) {
  console.log(argv0);
} else {
  console.log('No argument');
}
