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

def lottery_sort(segments, bets):

    segments = [(segments[2*i], segments[2*i + 1])
                        for i in range(len(segments) // 2)]

    s_open = [i[0] for i in segments]
    s_open.sort()
    s_close = [i[1] for i in segments]
    s_close.sort()

    bets = sorted([bet for bet in bets])

    res = []
    count = 0
    o = 0
    c = 0
    size = len(segments)
    for bet in bets:
        while o < size and s_open[o] <= bet:
            o += 1
            count += 1
        while c < size and s_close[c] < bet:
            c += 1
            count -= 1
        res.append(count)

    return sum(res)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    s = data[0]
    p = data[1]
    intervals = data[2:(s+1)*2]
    bets = data[(s+1)*2:]
    print(lottery_sort(intervals, bets))
