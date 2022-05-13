// def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

class ListNode {
  val?: number;
  next?: ListNode;

  constructor(val?: number, next?: ListNode) {
    this.val = val;
    this.next = next;
  }
}

function addTwoNumbers(l1?: ListNode, l2?: ListNode) {
  let sum = 0;
  const dummy = new ListNode(0);
  let tail = dummy;

  while (l1 || l2 || sum > 0) {
    sum += (l1?.val ?? 0) + (l2?.val ?? 0);
    tail.next = new ListNode(sum % 10);
    tail = tail.next;
    l1 = l1?.next ?? undefined;
    l2 = l2?.next ?? undefined;
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
