# 递归算法
def a_sum(arr):
    num = 0
    if arr == []:
        return 0
    else:
        # arr_sum = arr[0] + a_sum(arr[1:])
        num = arr[0] / arr[0] + a_sum(arr[1:])
    # return arr_sum
    return num


print(a_sum([1, 2, 3, 4, 5, 8]))
print(a_sum([]))
