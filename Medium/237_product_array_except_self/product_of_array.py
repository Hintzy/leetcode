from ds_templates import test_series as ts
from test_cases import tests

"""
The problem asks us to return an array equal to length of the original nums array.  Each entry in the new array is to 
be the the product of rest of the numbers in the array aside from it.

Cases:
- Array w/ two numbers
    - One of which is zero
    - Non zero examples
- Array w/ three numbers
    - One of which is zero
    - Nonzero examples
- Array w/ ten numbers
    - One of which is none
    - Nonzero examples

Solution:
    Store last index (len(nums)-1) as variable "end".
    Iterate forward through array to get products of array from index 1 to end and store in a hashmap. 
    The key will be [index following end of multiplication, end] = product.  Each iteration will add one to index 
    following start of multiplication in the key, and will mutliple that index by the preceding key that was determined.
    
    The same will be done going backwards through the 'nums' array.  This will store all the multiplication values that 
    are needed to determine will the elements of the array.  The keys in this hashmap will be [start, index preceding 
    multiplication]
    
    Once the forward and backward iterations are complete, an iteration will be done going straight through the array 
    multiplying the [start, index before] by the [index after, end], through.
    
    Each of the forward, backward, and final pass through the array will be O(n) in time complexity. Resulting in a 
    total O(3n), which reduces to O(n) complexity overall.    
"""


def product_of_array_1(nums: list[int]) -> list[int]:
    # set up a variable to define the last index of the nums array, for clarity
    end = len(nums) - 1

    # set boundary conditions for the hashmap. Since the hashmap is populated by existing values in the hashmap, you
    # need an initial condition to work off of.  One for working forward, one for working backward
    prods = {
        (0, 0): nums[0],
        (end, end): nums[end]
    }

    # populate results array with blank values so that indices can be referenced for assignment when iterating
    res = [0] * len(nums)

    # perform forwards population of the hashmap
    for i in range(1, len(nums)-1):
        prods[(0, i)] = prods[0, i - 1] * nums[i]

    # perform backwards population of the hashmap
    for i in range(len(nums)-2, 0, -1):
        prods[(i, end)] = prods[i + 1, end] * nums[i]

    # assign values to the first/last indices of the results array
    res[0], res[end] = prods[(1, end)], prods[(0, end-1)]

    # perform forwards iteration filling in all intermediate results array values using the precalculated values from
    # the hashmap
    for i in range(1, end):
        res[i] = prods[(0, i-1)] * prods[(i+1, end)]

    return res

"""
The following is an alternate solution that performs the same idea as the solution above, but instead of solving for 
all the products beforehand, the products are calculated during each iteration through the array. This results in a
time complexity of O(n^2) instead of O(n), since for each index position in the results array you must iterate through 
(n-1) values to obtain the product for that array index (n * (n-1)) = (n^2 - n) -> O(n^2).

The tradeoff is that the space complexity is O(1), instead of O(2n) (which reduces to O(n)).  The previous solution uses
O(2n) space since you must store (2 * (n-1)) values in the hashmap for quick calculation.  Whereas, this alternate 
solution only uses a single variable 'prod' to keep track of the current product for the calculation that's being 
performed.  
"""


def product_of_array_2(nums: list[int]) -> list[int]:
    res = [0] * len(nums)
    prod, end = 1, len(nums) - 1

    # solve for the first array position by iterating through all other values
    for i in range(1, end + 1):
        prod *= nums[i]
    res[0] = prod

    # reset the current product counter and solve for the last array position
    prod = 1
    for i in range (0, end):
        prod *= nums[i]
    res[end] = prod

    # iterate through all intermediate array indices, resetting the product counter each time
    for i in range(1, end):
        prod = 1
        for n in range(0, i):
            prod *= nums[n]
        for n in range(i+1, end+1):
            prod *= nums[n]
        res[i] = prod

    return res


ts.test_series(product_of_array_1, tests)
ts.test_series(product_of_array_2, tests)

# ts.compare_runtimes(tests, product_of_array_1, product_of_array_2)


