#### Find minoimum:
- Given the array find the minimum number in the array.

`arr=[10,3,7,14,19,15,11,7]`
`n -> len(arr)`

![image]()

- Initialize minm with 0<sup>th</sup> element in the array. `minm = arr[0]`, `minm` = 10

![image]()

- Now go through every element in the array `[1,n)` and check if element is less than `minm`:

- __case 1:__ Element is less than `minm` then change the value of `minm = arr[i]`

- __case 2:__ Element is greater than `minm` then no change.

![image]()





