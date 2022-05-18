#!/usr/bin/node

const axios = require('axios');

axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2])
  .then((response) => {
    for (const i in response.data.characters) {
      const character = response.data.characters[i];
      axios.get(character)
        .then((response) => {
          console.log(response.data.name);
        });
    }
  });
