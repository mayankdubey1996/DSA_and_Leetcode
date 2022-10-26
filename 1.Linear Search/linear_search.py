def linear_search(arr, target):
    """
    Given the array and item this fucntion applies the linear search 
    and checks the item is present in the array or not.
    ARGS: 
        arr  -> list
        item -> integer
    RETURN:
        idx -> integer
        OR
        -1
    """
    if len(arr)==0:
        return -1
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__=='__main__':
    arr  =  [8,5,7,1,9,2]
    for i in range(2):
        print("Enter the element you want to search in arr: ", arr)
        target = int(input())
        idx = linear_search(arr,target)
        print(idx)
    

