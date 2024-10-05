#!/usr/bin/node
// A script that shown diplay a messages 
// When number of Arguments passed

const args = process.argv.slice(2);
if (args.lengh === 0){
	console.log("No argument");
}else if (args.lengh === 1) {
	console.log("Argument found");
}else 	
	console.log("Arguments found");
