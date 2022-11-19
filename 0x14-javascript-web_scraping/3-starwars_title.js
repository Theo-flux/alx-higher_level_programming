#!/usr/bin/node
// script that prints out the title corresponding to an id
const { argv } = require('process');
const request = require('request');

const URL = `https://swapi-api.hbtn.io/api/films/:${argv[2]}`;
request(URL, (err, res) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const body = JSON.parse(body);
    console.log(body.title);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
