import sys

def maxProfit(prices):
  maxP=0
  minprice=float('inf')
  for i in range(len(prices)):
    minprice=min(minprice,prices[i])
    maxP=max(maxP,prices[i]-minprice)
  return maxP



prices = [7,1,5,3,6,4]
profit=maxProfit(prices)
print(profit)