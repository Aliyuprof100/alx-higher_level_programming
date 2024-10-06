#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const firstInteger = Math.floor(Number(process.argv[2])); // Convert the first argument to an integer
const secondInteger = Math.floor(Number(process.argv[3])); // Convert the second argument to an integer

if (isNaN(firstInteger) || isNaN(secondInteger)) {
  console.log('Missing parameters'); // Print if either argument is not a number
} else {
  const result = add(firstInteger, secondInteger); // Call the add function
  console.log(result); // Print the result of the addition
}
