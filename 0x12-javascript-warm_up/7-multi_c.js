#!/usr/bin/node
const len = process.argv[2];
const myVar = 'C is fun';

if (isNaN(Math.floor(Number(len)))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < len; i++) {
    console.log(myVar);
  }
}
