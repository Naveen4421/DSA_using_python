def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [1] * n

    # left pass
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]

    # right pass
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]

    return result
