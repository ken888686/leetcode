"use strict";
// def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
class ListNode {
    constructor(val, next) {
        this.val = val;
        this.next = next;
    }
}
function addTwoNumbers(l1, l2) {
    var _a, _b, _c, _d;
    let sum = 0;
    const dummy = new ListNode(0);
    let tail = dummy;
    while (l1 || l2 || sum > 0) {
        sum += ((_a = l1 === null || l1 === void 0 ? void 0 : l1.val) !== null && _a !== void 0 ? _a : 0) + ((_b = l2 === null || l2 === void 0 ? void 0 : l2.val) !== null && _b !== void 0 ? _b : 0);
        tail.next = new ListNode(sum % 10);
        tail = tail.next;
        l1 = (_c = l1 === null || l1 === void 0 ? void 0 : l1.next) !== null && _c !== void 0 ? _c : undefined;
        l2 = (_d = l2 === null || l2 === void 0 ? void 0 : l2.next) !== null && _d !== void 0 ? _d : undefined;
        sum = Math.floor(sum / 10);
    }
    return dummy.next;
}
function main() {
    const l1 = new ListNode(9, new ListNode(9));
    const l2 = new ListNode(9, new ListNode(9, new ListNode(4, new ListNode(0, new ListNode(9)))));
    console.dir(addTwoNumbers(l1, l2));
}
main();
