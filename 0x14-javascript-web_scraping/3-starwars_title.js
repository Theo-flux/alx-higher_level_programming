#!/usr/bin/node
// script that prints out the title corresponding to an id
const { argv } = require('process');
const request = require('request');

const URL = `https://swapi-api.hbtn.io/api/films/${argv[2]}`;
request(URL, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const bodyJSON = JSON.parse(body);
    console.log(bodyJSON.title);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
