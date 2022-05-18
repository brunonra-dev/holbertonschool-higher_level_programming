#!/usr/bin/node
/*
computes the number of tasks completed by user id
*/

const axios = require('axios').default;

axios.get(process.argv[2])
  .then(function (response) {
    const tasks = {};
    for (const todo in response.data) {
      const user = response.data[todo].userId;
      const completed = response.data[todo].completed;
      if (isNaN(tasks[user]) && completed) {
        tasks[user] = 1;
      } else if (completed) {
        tasks[user] += 1;
      }
    }
    console.log(tasks);
  });
