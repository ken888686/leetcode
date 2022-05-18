"use strict";
function reverse(numberList, left, right) {
    while (left <= right) {
        let temp = numberList[left];
        numberList[left] = numberList[right];
        numberList[right] = temp;
        left++;
        right--;
    }
}
function rotate(numberList, k) {
    k %= numberList.length;
    reverse(numberList, 0, numberList.length - k - 1);
    reverse(numberList, numberList.length - k, numberList.length - 1);
    reverse(numberList, 0, numberList.length - 1);
    return numberList;
}
;
function main() {
    console.log(rotate([1, 2, 3], 44));
}
main();
