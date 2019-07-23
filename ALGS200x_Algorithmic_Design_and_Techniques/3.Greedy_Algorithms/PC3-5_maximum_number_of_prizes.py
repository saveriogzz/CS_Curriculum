import sys


def max_prizes(candies):

    prizes = []

    while candies:

        next_prize = 1

        if next_prize < candies: prizes.append(next_prize)
        else:
            next_prize = candies
            prizes.append(next_prize)

        candies -= prizes[-1]

    return (len(prizes), prizes[-10:])



if __name__ == "__main__":
    candies = int(sys.stdin.read())
    print(max_prizes(candies))
