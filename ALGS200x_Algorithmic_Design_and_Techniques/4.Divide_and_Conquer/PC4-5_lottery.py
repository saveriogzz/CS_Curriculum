import sys
import intervals as I

def lottery_naive(intervals, bets):

    intervals = [I.closed(intervals[2*i], intervals[2*i + 1])
                        for i in range(len(intervals) // 2)]

    bets = sorted([bet for bet in bets])

    count = 0

    for bet in bets:
        for interval in intervals:
            if bet in interval: count += 1

    return count





if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    s = data[0]
    p = data[1]
    intervals = data[2:(s+1)*2]
    bets = data[(s+1)*2:]
    print(lottery_naive(intervals, bets))
