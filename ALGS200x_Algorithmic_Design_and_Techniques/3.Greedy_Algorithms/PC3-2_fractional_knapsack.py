# Uses python3
import sys

def get_optimal_value(capacity, weights, values):

    def get_loot_ordered(values, weights):
        '''Returns a list of tuples made by value,
        weight and density of the item; ordered by density.'''

        loot = []
        densities = [v/w for v,w in zip(values, weights)]

        for index in range(len(values)):
            loot.append((values[index], weights[index], densities[index]))

        return sorted(loot, key = lambda l: l[2], reverse = True)

    opt_value = 0.

    loot_ord = get_loot_ordered(values, weights)

    for item in loot_ord:
        if capacity == 0: return opt_value

        a = min(capacity, item[1])
        opt_value += a*(item[2])
        capacity -= a


    return opt_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
