# n = [2, 7, 11, 15]
# t = 6
#
# n = [3, 2, 4]
# t = 6

n = [3, 3, 17, 22, 40, 46, 52, 69]
t = 72


"""
Solution method: put the first element in a hash table with key value pair of <num: index>
Iterate through the list, starting with the second element, at each step:
    - Calculate the complement (target - current value)
    - See if complement is hash map, if so, populate the answer indeces with 
    value, and index of current answer
    - If complement not in hash map, add current key, value pair and move on
    - If all elements exhausted return 
"""


def twoSum(nums, target):
    visited = {nums[0]: 0}
    answer = []
    for i, num in enumerate(nums[1:]):
        complement = target - num
        try:
            bool(visited[complement])
        except KeyError:
            visited[num] = i + 1
        else:
            answer.append(visited[complement])
            answer.append(i + 1)
            return answer
    print('No solution possible.')
    return -1


twoSum(n, t)
