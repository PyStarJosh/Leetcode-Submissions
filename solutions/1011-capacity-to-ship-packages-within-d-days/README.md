# 1011. Capacity to Ship Packages within D Days

**Difficulty:** Medium

**Topics:** Array, Binary Search

**Link:** https://leetcode.com/problems/capacity-to-ship-packages-within-d-days

## Problem Statement
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

# Intuition
- This problem asks for the minimum weight capacity needed of a ship that can transport the packages within D days.
- We can solve this problem using brute force (O(N*M)) by simply iterating from the max value in weights until we reach a weight capacity value that ships the packages within D days. 
- As we know, this is linear search which has a time complexity of O(N) when traversing an array or range. However, we also know if the range is sorted, we can implement binary search to achieve this same outcome in O(log n) time.
- The 3 key components to binary search algorithms are:
    1. The sorted range
    2. The algorithm to calculate this condition (if needed)
    3. The condition that you tighten your range upon
- So, let's find our range, we know the left most value has to be max value in weights as the ship cannot carry a singular value that is greater than it's capacity, so any value less than the max could never transport all the packages
- Now, let's find our right most value, the simplest way to find this value is to think of the smallest weight capacity that can transport these packages in 1 day as any element great than it would be useless for our problem. So, we can find this by getting the sum of all the elements in weights.
- We have our range, so we can move forward to determining our range resizing condition. This problem is based around the number of days to ship all the elements in weights, so we will base our condition around it because the range resizes dependent on the current number of days our current weight capacity takes to ship the packages.
- To further explain these cases:
    - if our weight capacity took more than D days given, we need to increase the smallest value in our range
    - if our weight capacity took the same or less than D days given, we will record this weight_capacity as the current minimum weight capacity followed by decreasing the largest value in our range in attempt to find a smaller value that can achieve this in D days.
-  To determine the amount of days the ship a X weight capacity would take, you track the cumulative weight while traversing weights until the value exceeds your ship weight. At this point, increment shipping days by 1 and set the current weight to the current package's weight.

# Approach
1. Initialize your range 
    ```python3
      left = max(weights)
      right = sum(weights)
    ```
2. Initialize your binary search while loop while setting the needed variables to calculate and store the range resizing condition
    ```python3
     while left <= right:
        cap = left + (right - left) // 2
        curr_weight = 0
        time = 1
    ```
3. Implement our condition calculation algorithm to determine the number of days this weight capacity would take to ship the packages
    ```python3
    for pck_weight in weights:
        curr_weight += pck_weight
        if curr_weight > cap:
            time += 1
            curr_weight = pck_weight
    ```
4. Our condition is set, so let's tighten our range based upon
    ```python3
    if time <= days:
        ans = cap
        right = cap - 1
    else:
        left = cap + 1
    ```
5. Finally, return your current minimum weight capacity after the while loop terminates
    ```python3
    return ans
    ```

# Complexity
- Time complexity:
O(N log M) -> Weights traversed (O(N)) each while loop iteration (O(log M)) and M represents sum(weights) - max(weights)

- Space complexity:
O(1) -> Only initialize constant space variables
