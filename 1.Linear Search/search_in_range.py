def search_in_range(arr, target, start_idx, end_idx):
    """
    Given the array, target, start index and end index this function search in range
    between range from start to end if element is present or not.
    
    ARGS:
        arr       -> list
        target    -> integer
        start_idx -> integer
        end_idx   -> integer
    
    RETURN:
        i/-1     -> integer
    """
    if len(arr)==0 or end_idx>=len(arr) or start_idx<0:
        return -1
    for i in range(start_idx,end_idx,1):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    arr = [10,3,7,14,19,15,11,7]
    target = 19
    start_idx = 2
    end_idx = 5
    found_idx = search_in_range(arr, target, start_idx, end_idx)
    print(found_idx)
