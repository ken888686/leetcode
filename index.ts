const maxChar = (str: string): string => {
  const charMap: { [key: string]: number } = {};
  let max = 0,
    maxChar = "";
  for (let x of str) {
    charMap[x] = x in charMap ? (charMap[x] += 1) : 1;
    if (charMap[x] > max) {
      max = charMap[x];
      maxChar = x;
    }
  }

  return maxChar;
};

const main = () => {
  console.log(maxChar("Hello World!"));
};

main();
