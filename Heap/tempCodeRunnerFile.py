    # run the loop until we cant divide the number by 2
    res = float('inf')
    while True:
        min_val = sorted_list[0]
        max_val = sorted_list[-1]

        diff = max_val - min_val

        res = min(res, diff)  # update the res

        # if the max val is even we can further divide by 2

        if max_val % 2 == 0:
            # remove the max val
            sorted_list.remove(max_val)
            # add the max val/2
            sorted_list.add(max_val//2)

        else:
            return res