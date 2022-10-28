### Find Numbers with Even Number of Digits

- Given an array nums of integers, return how many of them contain an even number of digits.

__example__ 

`nums = [12,345,2,6,7896]`	

`Output: 2`

- Only 12 and 7896 has even number of digits.  

![image](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/images/7.1even_digits.png)

- How to find given number has even number of digit or not?

  __Approach 1__: Convert each number to strinf and use __`len()`__ function to check
even or odd length of string.

  __Approach 2__: Another way is to check via __division method__.

![image](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/images/7.2even_digits.png)

- Divide (floor division) any number by 10.
- number of digits is number of steps it will take us to reach to 0.
- In above example it took 4 steps then we have 4 digits in it.


