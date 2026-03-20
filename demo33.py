# fruit_list1 = ['apple', 'banana', 'cherry' , 'papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'

# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
# print(sum)


# def plusMinus(arr):
#     positive = 0
#     negative = 0
#     zero = 0
#     for i in arr:
#         if i > 0:
#             positive += 1
#         elif i < 0:
#             negative += 1
#         else:
#             zero += 1
#     print("{:.6f}".format(positive / len(arr)))
#     print("{:.6f}".format(negative / len(arr)))
#     print("{:.6f}".format(zero / len(arr)))

# def f(i, values = []):
#     values.append(i)
#     print(values)
    
# f(1)
# f(2)
# f(3)    

# def func(value, values):
#     var = 1
#     values[0] = 44
    
# t = 3
# v = [1, 2, 3]
# func(t, v)
# print(t, v[0])

# dict = {'b ': 2, 'a': 1, 'c': 3}
# for _ in sorted(dict):
#     print(dict[_])
    
# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit [index] = 1

# addone('apple')
# addone('banana')
# addone('Apple')
# print(len(fruit))

# product of array except self sample input : [1,2,3,4] expected output : [24,12,8,6]
# def productExceptSelf(nums):
#     result = [1] * len(nums) 
#     left = 1
#     for i in range(len(nums)):
#         result[i] *= left
#         left *= nums[i]
#     right = 1
#     for i in range(len(nums) - 1, -1, -1):
#         result[i] *= right
#         right *= nums[i]
#     return result

# simple code to find two sum in an array

from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j