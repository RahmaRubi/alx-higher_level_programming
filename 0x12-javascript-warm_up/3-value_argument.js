#!/usr/bin/node
args = process.argv;
if (args[2] != null)
    console.log(process.argv[2]);
else
    console.log('No argument');
