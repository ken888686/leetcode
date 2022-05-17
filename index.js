"use strict";
function lengthOfLongestSubstring(s) {
    let map = new Map();
    let result = 0;
    let start = 0;
    for (let i = 0; i < s.length; i++) {
        if (map.has(s[i])) {
            start = Math.max(map.get(s[i]) + 1, start);
        }
        result = Math.max(result, i - start + 1);
        map.set(s[i], i);
    }
    return result;
}
;
function main() {
    console.log(lengthOfLongestSubstring('dvdf'));
}
main();
