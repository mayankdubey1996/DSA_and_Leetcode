## Linear Search
- Naive way to search the element in the list or string.
- Scan through the list and compare every element to the target element.

`arr = [8,5,7,1,9,2]` <br>
`target = 1`

#### Working:

1. When element exist in the array, **return index** where target is found.
<images>

2. When element does not exist in the array, **return -1.**
<images>
   
#### Pseudo code:
   ```py
   arr = [6,7,2,1,4,5]
   target = 4
   FUNCTION linear_search(arr,target):
      FOR i=0 to len(arr):
         IF arr[i]==target THEN:
            RETURN i #element found at ith index
      RETURN -1 #element not found
   ```

#### Time Complexity:
   | **Scenario**        | **Time Complexity** |         
   | :-------------: |:-------------:|
   | Best Case | O(1) |                        
   |Worst Case|O(n) |
  
n: size of an array

#### Explanation:

- **Best Case:**
   If the element which we are searching for is found at 0<sup>th</sup> index, then we will only make only 1 comparision hence time complexity is O(1).
- **Worst Case:**
If the element which we are searching for is not found, then we have to make scan all the elements and at the end we make the conclusion that element not found. In this scenario we are making `n` comparision hence time complexity is O(n).

#### Coding Questions [PDF](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/Notes/linear_search.pdf)
   | **Question**        | **Notes** |**Leetcode** |        
   | :------------- |:-------------:|:-------------:|
   |1. [Linear Search](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/linear_search.py)|[Notes](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/Notes/linear_search.md)|--|
   |2. [Search In String](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/search_in_string.py)|[Notes](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/Notes/search_in_string.md)|--|
   |3. [Search In Range](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/search_in_range.py)|[Notes](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/Notes/search_in_range.md)|--|
   |4. [Find Maximum Number](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/find_maximum.py)|[Notes](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/Notes/find_max.md)|--|
   |5. [Find Minimum Number](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/find_mimimum.py)|[Notes](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/Notes/find_min.md)|--|
   |6. [Search In 2D Array](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/search_in_2d_array.py)|[Notes](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/Notes/search_in_2d_array.md)|--|
   |7. [Find Numbers with Even Number of Digits](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/even_digits.py)|[Notes](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/Notes/find_even_numbers.md)|[LeetCode](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/)|
   |8. [Richest Customer Wealth](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/richest_customer.py)|[Notes](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/Notes/richest_customer.md)| [LeetCode](https://leetcode.com/problems/richest-customer-wealth/)|

