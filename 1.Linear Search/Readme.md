## Linear Search
Given the array/list of the elements search if target exist in the array or not.
If value exist return the index, If value does not exist return -1

arr = [8,5,7,1,9,2]
target = 1

#### Working:

1. When element exist in the array.
<images>

2. When element does not exist in the array.
<images>

#### Time Complexity:

| Scenario | Time Complexity | 
| : --- : |      :---:      |
|Best Case |O(1)             |
|Worst Case|O(n)

n: size of the array

#### Explanation

- Best Case:
If the element which we are searching for is found at 0th index, then we will only make only 1 comparision hence time complexity is O(1).
- Worst Case:
If the element which we are searching for is not found, then we have to make scan all the elements and at the end we make the conclusion that element not found. In this scenario we are making `n` comparision hence time complexity is o(n).

#### Questions
1. Linear Search
2. Search In String
3. Search In Range
4. Find Maximum Number
5. Find Minimum Number
6. Search In 2D Array
7. Find Numbers with Even Number of Digits [LeetCode](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/))
8. Richest Customer Wealth [LeetCode](https://leetcode.com/problems/richest-customer-wealth/)

