#!/usr/bin/node
/*
Prints the title of a Star Wars movie where
the episode number matches a given integer
*/

const axios = require('axios').default;
const character = 'https://swapi-api.hbtn.io/api/people/18/';

axios.get(process.argv[2])
  .then(function (response) {
    let count = 0;
    for (let movie of response.data.results) {
      if (response.data.results[movie].characters.includes(character)) {
        count = count + 1;
      }
    }
    console.log(count);
  })
  .catch(function (err) {
    console.log(err);
  });
