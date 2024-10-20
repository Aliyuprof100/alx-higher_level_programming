#!/usr/bin/node
const message = 'Hello Prof';
const arg = process.argv.slice(2);
const x = parseInt(arg[0]);

if (isNaN(x)) {
  console.log('The number you are tring to put is not an interger');
} else {
  for (let i = 0; i < x; i++) {
    console.log(message);
  }
}
