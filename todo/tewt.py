def max_partitions_with_min_bottleneck(performance):
    partitions_count = 0
    current_and = -1  # Start with all bits set for bitwise AND

    for value in performance:
        if current_and == -1:
            current_and = value
        else:
            current_and &= value

        # If the current partition's AND result is 0, we can finalize this partition
        if current_and == 0:
            partitions_count += 1
            current_and = -1  # Reset for a new partition

    return partitions_count


# Example
n = 6
performance = [5, 2, 6, 1, 1, 4]
print("Maximum Partitions with Minimum Bottleneck Level:",
      max_partitions_with_min_bottleneck(performance))
