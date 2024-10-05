#!/usr/bin/node
//A script that display a message.

const arg = process.argv[2];
if (arg === undefined) {
  console.log(“No argument”)
} else {
  console.log(arg)}
