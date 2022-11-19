#!/usr/bin/node
// script that prints out the body.title from a  GET request

const request = require('request');
const episodeNum = process.argv[2];
const API_URL = `https://swapi-api.hbtn.io/api/films/${episodeNum}`;

request(API_URL, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const bodyJSON = JSON.parse(body);
    console.log(bodyJSON.title);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
