#!/usr/bin/node
args = process.argv.length;
// console.log(args); path to node - path to script - arguments....
if (args === 2)
{
    console.log('No argument');
}
else if (args == 3)
{
    console.log('Argument found');
}
else
{
    console.log('Arguments found');
}
