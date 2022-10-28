#### Find maximum:
- Given the array find the maximum number in the array

`arr=[10,3,7,14,19,15,11,7]`
`n -> len(arr)`

![image](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/images/4.1find_max.png)

- Initialize maxm with 0<sup>th</sup> element in the array. `maxm = arr[0]`, `maxm` = 10

![image](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/images/4.2find_max.png)

- Now go through every element in the array `[1,n)` and check if element is greater than `maxm`:

- __case 1:__ Element is greater than `maxm` then change the value of `maxm = arr[i]`

- __case 2:__ Element is less than `maxm` then no change.

![image](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/images/4.3find_max.png)





