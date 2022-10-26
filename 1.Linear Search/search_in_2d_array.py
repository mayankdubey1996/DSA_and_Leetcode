def search_in_2d(arr,target):
    """
    Given 2D array this fucntion checks if target is in the array or not
    ARGS:
        arr    -> <list<list>>
        target -> integer
    RETURN
        found  -> tuple 

    """
    if len(arr)==0:
        return -1
    found = (-1,-1)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] ==  target:
                found = (i,j)
                return found
    return found

if __name__ == "__main__":
    arr = [[23,4,1],
          [18,12,3,9],
          [78,99,34,56]]
    
    target = 10
    idx = search_in_2d(arr,target)

    print("Element found at", idx)