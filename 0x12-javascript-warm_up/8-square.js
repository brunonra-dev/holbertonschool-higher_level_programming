#!/usr/bin/node
const args = process.argv.slice(2);

if (parseInt(args[0])) {
  for (let i = 0; i < parseInt(args[0]); i++) {
    for (let j = 0; j < parseInt(args[0]); j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} else console.log('Missing size');
