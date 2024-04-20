#!/usr/bin/node
args = process.argv.length;
if (args >= 3)
    console.log(process.argv[2]);
else
    console.log('No argument');
