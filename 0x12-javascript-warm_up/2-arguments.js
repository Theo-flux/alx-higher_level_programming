#!/usr/bin/node
const { argv } = require('node:process');

if (argv) {
  if (argv.length === 1) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
} else {
  console.log('No argument');
}
