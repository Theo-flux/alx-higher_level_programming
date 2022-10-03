#!/usr/bin/node
console.log(
  typeof process.argv === 'undefined' ? 'No argument' : process.argv[2]
);
