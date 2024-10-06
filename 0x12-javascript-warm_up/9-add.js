#!/usr/bin/node
function add (a, b) {
  return a + b;
}

console.log(add(Number(process.argv[2])), add(Number(process.argv[3])));
