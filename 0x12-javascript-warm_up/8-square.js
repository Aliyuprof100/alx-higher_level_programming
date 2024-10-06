#!/usr/bin/node
const arg = process.argv.slice(2);
const x = parseInt(arg[0]);
if (isNaN(x)) { // x represent size
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
