def getminmoves(price, k):
    hash = {}
    for p in price:
        if p in hash:
            hash[p] += 1
        else:
            hash[p] = 1
    # get the max pair
    pair = [(key, val) for key, val in hash.items()]
    pair.sort(key=lambda x: x[1])
    # max pair
    max_pair = pair[-1]
    diff = abs(max_pair[0]-k)

    return diff*max_pair[1]


print(getminmoves([1, 2, 3], 5))

from collections import Counter

def min_moves_to_median(price, k):
    # Count occurrences of each price
    price_counts = Counter(price)

    # Find current median and counts of prices smaller and greater than k
    current_median, smaller_count, greater_count = find_median_and_counts(price_counts)

    # Calculate the difference between the current median and target median
    diff = k - current_median

    # Calculate minimum moves required
    min_moves = 0

    if diff > 0:
        # Need to increase prices, add moves for smaller prices
        min_moves += count_moves_for_smaller(price_counts, k, smaller_count, diff)
    elif diff < 0:
        # Need to decrease prices, add moves for greater prices
        min_moves += count_moves_for_greater(price_counts, k, greater_count, -diff)

    return min_moves

def find_median_and_counts(price_counts):
    sorted_prices = sorted(price_counts.keys())
    n = len(sorted_prices)

    median_index = n // 2

    if n % 2 == 0:
        current_median = (sorted_prices[median_index - 1] + sorted_prices[median_index]) / 2
    else:
        current_median = sorted_prices[median_index]

    # Count prices smaller and greater than k
    smaller_count = sum(price_counts[p] for p in sorted_prices if p <)


print(min_moves_to_median([1, 2, 3], 5))
