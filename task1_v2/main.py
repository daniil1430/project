def max_subarray_v1(arr):
    if not arr:
        return 0

    best = arr[0]
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            cur_sum = 0
            for k in range(i, j + 1):
                cur_sum += arr[k]
            if cur_sum > best:
                best = cur_sum
    return best


if __name__ == "__main__":
    test_arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Массив: {test_arr}")
    print(f"O(n3): {max_subarray_v1(test_arr)}")