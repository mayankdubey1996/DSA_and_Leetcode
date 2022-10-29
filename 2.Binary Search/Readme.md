### Binary Search
- Divide and Conquer approach.
- Optimized way to search the element in __sorted array.__
- __It require the given array to be sorted.__

- `arr1 = [2,4,9,10,12,14,18,19]` -> sorted array in Ascending order
- `arr2 = [19,12,6,5,3,-1,-7,-8]` -> sorted array in Descending order

- Let's say we want to search 18 `target=18` in `arr1` we can certainly apply linear search but
worst case time complexity of linear search is O(n).

- Can we do better? given that array is sorted.

``` py
FUNCTION binary_search(array,target)
	- Initialize start_idx = 0, end_idx = len(arr)-1
	- while end_idx>=start_idx:
		1. Calculate mid:
			mid_idx = (start_idx+ end_idx)//2 #floor division
		2. IF array[mid_idx]==target:
			return mid_idx OR True
		3. IF  array[mid_idx]<target:
			Update: start_idx = mid+1
		4. ELSE:
			Update end_idx = mid-1
	- return -1 OR FALSE #target element Not found
```
- __While loop will stop executing when start_idx become greater then end_idx, In that case element is not in the array and we return -1__

### Time Complexity:
   | **Scenario**        | **Time Complexity** |         
   | :-------------: |:-------------:|
   | Best Case | O(1) |                        
   |Worst Case|O(log n) |

### When to use Binary Search?
- Before jumping on questions, let's understand when to use binary search?
	1. Given array is sorted.
	2. Searching problem which has some sort of pattern (square root of number)

### Coding Questions
 | **Question**        | **Notes** |**Leetcode** |        
   | :------------- |:-------------:|:-------------:|
   |1. [Iterative Binary Search](link)|[Notes](link)|--|
   |2. [Recursive Binary Search](link)|[Notes](link)|--|
   |3. [Order Agnostic Binary Search](link)|[Notes](link)|--|
   |4. [Ceiling of a Number](link)|[Notes]()|--|
   |5. [floor of a Number](link)|[Notes]()|--|
   |6. [Find Smallest Letter Greater Than Target](link)|[Notes]()|[Leetcode](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)|


