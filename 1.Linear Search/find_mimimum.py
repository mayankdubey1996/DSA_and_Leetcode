def find_minimum_number(arr):
    """
    Given array/list function finds the minimium element in an array.
    ARGS:
        arr  -> list
    RETURN:
        minm -> integer 
    """
    if len(arr)==0:
        return -1
    minm = arr[0]
    for i in range(1,len(arr)):
        if arr[i]<minm:
            minm = arr[i]
    return minm

if __name__ == "__main__":
    arr = [10,3,7,14,19,15,11,7]
    minm = find_minimum_number(arr)
    print(minm)
        