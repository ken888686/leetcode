"use strict";
function solution(s) {
    let left = 0, right = s.length - 1;
    s = s.toLowerCase().replace(/[\W_]/g, "");
}
function main() {
    console.log(solution("0p"));
    console.log(solution(" "));
}
main();
