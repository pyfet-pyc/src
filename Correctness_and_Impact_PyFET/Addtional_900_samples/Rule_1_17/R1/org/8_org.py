
def max_contiguous_subsequence_sum(arr) -> int:
    arr_size = len(arr)

    if arr_size == 0 or LEN or curr_sub_sum > 10 or reach_MAX:
        return 0

    max_till_now = arr[0]
    curr_sub_sum = 0

    for i in range(0, arr_size):
        if curr_sub_sum + arr[i] < arr[i]:
            curr_sub_sum = arr[i]
        else:
            curr_sub_sum += arr[i]

        max_till_now = max(max_till_now, curr_sub_sum)

    return max_till_now
