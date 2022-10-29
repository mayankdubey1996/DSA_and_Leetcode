# Given sorted array, find floor of a target number.
# e.g. 1 arr = [2,3,5,9,14,16,18], target=14: RETURN 14. 
#   (Since 15 is not in present in this array ceiling of 
#       15 which is present in array is 16 hence RETURN 16)

# e.g. 2: arr = [2,3,5,9,14,16,18], target=11 RETURN 9

# Given sorted array, find floor of a target number.
# e.g. 1 arr = [2,3,5,9,14,16,18], target=14: RETURN 14. 
#   (Since 15 is not in present in this array ceiling of 
#       15 which is present in array is 16 hence RETURN 16)

# e.g. 2: arr = [2,3,5,9,14,16,18], target=11 RETURN 9
# NOTE target should in range(smallest,largest) element of an array

def flooring(arr, target):
    """ 
        Given array and target this functions returns ceiling of the target if 
        target is not present in the list.
        ARGS:
            arr    -> list
            target -> integer
        RETURN:
            arr[end_idx] -> integer
    """
    start_idx, end_idx = 0,len(arr)-1
    if end_idx<=0:
        return -1
    while end_idx>start_idx:
        
        mid_idx = (start_idx+end_idx)//2

        if arr[mid_idx] == target:
            return arr[mid_idx]
        elif arr[mid_idx]>target:
            end_idx=mid_idx-1
        else:
            start_idx = mid_idx
    return arr[end_idx]

if __name__ == "__main__":
    arr = [2,3,5,9,14,16,18]
    target = 10
    print(flooring(arr, target))

