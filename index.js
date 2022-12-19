"use strict";
const chunk = (arr, n) => {
    const result = [], temp = [];
    for (let x of arr) {
        if (temp.length === n) {
            result.push([...temp]);
            temp.length = 0;
        }
        temp.push(x);
    }
    result.push(temp);
    return result;
};
const main = () => {
    console.log(chunk([1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 2], 3));
};
main();
