"use strict";
class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }
}
function mergeTwoLists(list1, list2) {
    var _a, _b;
    const head = new ListNode(0);
    let tail = head;
    while (list1 && list2) {
        if (list1.val < list2.val) {
            tail.next = list1;
            list1 = (_a = list1.next) !== null && _a !== void 0 ? _a : null;
        }
        else {
            tail.next = list2;
            list2 = (_b = list2.next) !== null && _b !== void 0 ? _b : null;
        }
        tail = tail.next;
    }
    tail.next = list1 ? list1 : list2;
    return head.next;
}
;
function main() {
    const l1 = new ListNode(1, new ListNode(4));
    const l2 = new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(6, new ListNode(9)))));
    console.dir(mergeTwoLists(l1, l2));
}
main();
