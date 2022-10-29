def binary_search_iterative(arr,target):
    start_idx,end_idx = 0, len(arr)-1
    if end_idx<0:
        return -1
    while end_idx>=start_idx:
        mid_idx = (start_idx+end_idx) //2 #floor division
        if arr[mid_idx] == target:
            return mid_idx
        elif target>arr[mid_idx]:
            start_idx=mid_idx+1
        else:
            end_idx=mid_idx-1
    return -1

if __name__ == '__main__':
    arr = [2,4,9,10,12,14,18,19]
    target = 18
    idx = binary_search_iterative(arr,target)
    print("Target element is found at index", idx) #if idx = -1 then target not found.
