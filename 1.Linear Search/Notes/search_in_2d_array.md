### Search in 2d array:
- 2d array is nothing but list of list. 
- Given the 2d array search if item exist in the array or not: 
		If item exist return (row_idx,col_idx)
		Else return (-1,-1)

`arr=[[23,4,1],[18,12,3,9],[78,99,34,56]]`

`target=10`

![image](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/images/6.1search_in_2d.png)

#### Approcah

![image](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/images/6.2search_in_2d.png)

- Take 0<sup>th</sup> `row` and apply linear search. Search the element in every column of 0<sup>th</sup> row.

![image](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/images/6.3search_in_2d.png)

- Take 1<sup>st</sup> `row` and apply linear search. Search element in every column of 1<sup>st</sup> row.

!image](https://github.com/mayankdubey1996/DSA_and_Leetcode/blob/main/1.Linear%20Search/images/6.4search_in_2d.png)

- Take 2<sup>nd</sup> `row` and apply linear search. Search element in every column of 2<sup>nd</sup> row.

- __Return (-1,-1)__, since 10 is not in the matrix.
