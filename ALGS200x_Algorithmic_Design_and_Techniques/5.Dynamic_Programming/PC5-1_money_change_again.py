import sys

def RECchange(money, coins):

    if money == 0:
        return 0

    MinNumCoins = float("inf")

    for i in range(len(coins)):
        if money >= coins[i]:
            NumCoins = RECchange(money - coins[i], coins)
            if NumCoins + 1 < MinNumCoins:
                MinNumCoins = NumCoins + 1

    return MinNumCoins


def DPchange(money, coins):

    MinNumCoins = [0 for i in range(money + 1)]

    for m in range(1, money + 1):
        MinNumCoins[m] = float("inf")
        for i in range(len(coins)):
            if m >= coins[i]:
                NumCoins = MinNumCoins[m - coins[i]] + 1
                if NumCoins < MinNumCoins[m]:
                    MinNumCoins[m] = NumCoins

    return MinNumCoins[money]



if __name__ == "__main__":

    money = int(input())
    denominations = [1, 3, 4]

    print(DPchange(money, denominations))
