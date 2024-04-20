#!/usr/bin/node
exports.callMeMoby = function (number, functionf)
{
    for(i = 0; i < number; i++)
    {
        functionf();
    }
}
