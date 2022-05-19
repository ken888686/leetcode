
function climbStairs(n: number): number {
  let a = 1, b = 1;
  for (let i = 0; i < n; i++) {
    let temp = a;
    a = b;
    b += temp;
  }
  return a;
};

function main() {
  console.log(climbStairs(5));
}

main();
