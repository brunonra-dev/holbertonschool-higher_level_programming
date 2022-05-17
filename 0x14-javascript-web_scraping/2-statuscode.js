#!/usr/bin/node
/*
display the status code of a GET request
*/

const axios = require('axios').default;

axios.get(process.argv[2])
  .then(function (response) {
    console.log('code:', response.status);
  })
  .catch(function (err) {
    console.log('code:', err.response.status);
  });
