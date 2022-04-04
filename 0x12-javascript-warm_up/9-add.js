#!/usr/bin/node
const args = process.argv.slice(2);

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

console.log(add(args[0], args[1]));
