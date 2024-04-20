#!/usr/bin/node
args = process.argv;
if(!args[2] || !args[3])
{
    console.log('Nan');
}
else
{
a = args[2];
b = args[3];
function add(a, b)
{
    let x = (parseInt(a) + parseInt(b));
    console.log(x)
}
add(a, b);

}
