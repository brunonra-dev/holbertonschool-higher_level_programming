#!/usr/bin/node
const process = require('process');

const args = process.argv.slice(2);

console.log('My number: ' + parseInt(args[0]));
