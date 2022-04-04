#!/usr/bin/node
const args = process.argv.slice(2);

function fac (x) {
  if (!x) return 1;
  return x * fac(x - 1);
}

console.log(fac(args[0]));
