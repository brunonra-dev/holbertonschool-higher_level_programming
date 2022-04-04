#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length < 2) console.log(0);
else {
  const ord = args.sort(function (a, b) { return b - a; });
  console.log(parseInt(ord[1]));
}
