### Richest Customer Wealth

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.


`arr = [[1,2,3],[3,2,1]]`

`output = 6` 

__explanation:__

1st customer has wealth = 1 + 2 + 3 = 6<br>
2nd customer has wealth = 3 + 2 + 1 = 6<br>
Both customers are considered the richest with a wealth of 6 each, so return 6.<br>
 

![image](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/images/8.1rich_customer.png)

- we will take this example to understand the approach.

![image](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/images/8.2rich_customer.png)

- Initialise `max=0`, means we have 0 money.

![image](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/images/8.3rich_customer.png)

- Take 0<sup>th</sup> row and sum them all and check is it greater than `maxm`:
	
	- If YES then update `maxm`

![image](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/images/8.4rich_customer.png)

- Take 1<sup>St</sup> row and sum them all and check is it greater than `maxm`:
	
	- NO UPDATE `maxm` 

![image](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/images/8.5rich_customer.png)

- Take 0<sup>th</sup> row and sum them all and check is it greater than `maxm`:
	
	- NO UPDATE `maxm`

- __Return maxm = 17__
 




