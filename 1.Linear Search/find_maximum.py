def find_maximum_number(arr):
    """
    Given array/list function finds the maximum element in an array.
    ARGS:
        arr  -> list
    RETURN:
        maxm -> integer 
    """
    if len(arr)==0:
        return -1
    maxm = arr[0]
    for i in range(1,len(arr)):
        if arr[i]>maxm:
            maxm = arr[i]
    return maxm

if __name__ == "__main__":
    arr = [10,3,7,14,19,15,11,7]
    maxm = find_maximum_number(arr)
    print(maxm)
        