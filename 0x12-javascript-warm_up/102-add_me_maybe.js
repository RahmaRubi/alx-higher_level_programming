#!/usr/bin/node

exports.addMeMaybe = function (number, functionf) {
    number++; // Incrementing the number
    functionf(number); // Calling the provided function with the incremented number
}
