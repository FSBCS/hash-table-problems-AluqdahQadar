def count_subarrays_with_sum(arr, sum):
    n = len(arr)
    prefix_sum = 0
    count = 0
    sum_map = {}
    for i in range(n):
        prefix_sum += arr[i]
        if prefix_sum == sum:
            count += 1
        if prefix_sum - sum in sum_map:
            count += sum_map[prefix_sum - sum]
        if prefix_sum in sum_map:
            sum_map[prefix_sum] += 1
        else:
            sum_map[prefix_sum] = 1
    return count