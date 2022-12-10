function palindrome(s: string): boolean {
  let result = true,
    left = 0,
    right = s.length - 1;
  while (left < right) {
    if (s[left] !== s[right]) {
      result = false;
      break;
    }
    left++;
    right--;
  }
  return result;
  // return s.split("").every((curr, i) => {
  //   return curr === s[s.length - i - 1];
  // });
}

function main() {
  console.log(palindrome("aba"));
}

main();
