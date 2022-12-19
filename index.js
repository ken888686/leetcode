"use strict";
const maxChar = (str) => {
    const charMap = {};
    let max = 0, maxChar = "";
    for (let x of str) {
        charMap[x] = x in charMap ? (charMap[x] += 1) : 1;
        if (charMap[x] > max) {
            max = charMap[x];
            maxChar = x;
        }
    }
    // console.log(`${maxChar}: ${max}`);
    for (let x of str) {
        console.log(x);
    }
    for (let x in str.split("")) {
        console.log(x);
    }
    return "";
};
const main = () => {
    console.log(maxChar("Hello World!"));
};
main();
