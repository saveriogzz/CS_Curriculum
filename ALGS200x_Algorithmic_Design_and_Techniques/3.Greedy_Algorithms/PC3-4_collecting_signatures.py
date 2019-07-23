import sys
import intervals as I

def min_segments(data):
    intervals = sorted([I.closed(data[2*i], data[2*i + 1])
                            for i in range(len(data)//2)],
                        key = lambda l: l.upper)

     # or:
     # i = iter(data)
     # intervals = list(zip(i,i))

    count_visits = 0
    visits = []

    while intervals:

        visit = intervals[0].upper

        for interval in intervals[:]:
            if visit in interval:
                intervals.remove(interval)

        count_visits += 1
        visits.append(visit)

    return (count_visits, visits)


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    intervals = data[1:]
    print(min_segments(intervals))
