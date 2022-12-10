const reverseInt = (n: number): number => {
  return (
    Number.parseInt(n.toString().split("").reverse().join("")) * Math.sign(n)
  );
};

const main = () => {
  console.log(reverseInt(-124123));
};

main();
