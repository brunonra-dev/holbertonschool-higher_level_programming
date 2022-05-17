#!/usr/bin/node
/*
prints the number of movies where the character “Wedge Antilles” is present
*/

const axios = require('axios').default;
const character = 'https://swapi-api.hbtn.io/api/people/18/';

axios.get(process.argv[2])
  .then((response) => {
    let count = 0;
    for (const movies in response.data.results) {
      if (response.data.results[movies].characters.includes(character)) {
        count = count + 1;
      }
    }
    console.log(count);
  })
  .catch(function (err) {
    console.log(err);
  });
