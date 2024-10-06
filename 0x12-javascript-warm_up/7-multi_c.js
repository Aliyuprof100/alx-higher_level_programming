#!/usr/bin/node
const message = 'C is fun';
const num = Math.floor(Number(process.argv[2])); // Step 1

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log(message);
  }
}
