#!/usr/bin/node
/*
gets the contents of a webpage and stores it in a file
*/

const axios = require('axios').default;

axios.get(process.argv[2])
  .then((response) => {
    const f = process.argv[3];
    const data = response.data;
    const fs = require('fs');
    fs.writeFile(f, data, (err) => {
      err && console.log(err);
    });
  });
