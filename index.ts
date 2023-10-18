interface Transaction {
  Id: number;
  Size: number;
  Fee: number;
}

const transactions: Transaction[] = [
  { Id: 1, Size: 57247, Fee: 0.0887 },
  { Id: 2, Size: 98732, Fee: 0.1856 },
  { Id: 3, Size: 134928, Fee: 0.2307 },
  { Id: 4, Size: 77275, Fee: 0.1522 },
  { Id: 5, Size: 29240, Fee: 0.0532 },
  { Id: 6, Size: 15440, Fee: 0.025 },
  { Id: 7, Size: 70820, Fee: 0.1409 },
  { Id: 8, Size: 139603, Fee: 0.2541 },
  { Id: 9, Size: 63718, Fee: 0.1147 },
  { Id: 10, Size: 143807, Fee: 0.266 },
  { Id: 11, Size: 190457, Fee: 0.2933 },
  { Id: 12, Size: 40572, Fee: 0.0686 },
];

const blockSizeLimit = 1000000;
const reward = 12.5;

function getMaxReward(
  transactions: Transaction[],
  blockSizeLimit: number,
  reward: number
) {
  const sortedTransactions = transactions.sort((a, b) => b.Fee - a.Fee);
  let totalSize = 0;
  let totalFee = 0;
  for (const transaction of sortedTransactions) {
    if (totalSize + transaction.Size > blockSizeLimit) {
      continue;
    }
    totalSize += transaction.Size;
    totalFee += transaction.Fee;
  }
  return totalFee + reward;
}
console.log(getMaxReward(transactions, blockSizeLimit, reward));
