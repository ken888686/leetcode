SELECT u.NAME, b.BALANCE
FROM Users u JOIN
  (
    SELECT account, SUM(amount) AS balance
    FROM Transactions
    GROUP BY account
    HAVING SUM(amount) > 10000
  ) b ON u.account = b.account;
