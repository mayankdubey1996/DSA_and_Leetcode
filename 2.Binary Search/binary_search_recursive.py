def binary_search_recursive(arr,target,start_idx,end_idx):
    mid_idx = (start_idx+end_idx) //2 #floor division
    if arr[mid_idx] == target:
            return mid_idx
    elif target>arr[mid_idx]:
            start_idx=mid_idx+1
            return binary_search_recursive(arr,target,start_idx,end_idx)
    else:
        end_idx=mid_idx-1
        return binary_search_recursive(arr,target,start_idx,end_idx)
    return -1

if __name__ == '__main__':
    arr = [2,4,9,10,12,14,18,19]
    target = 18
    idx = binary_search_recursive(arr,target,start_idx=0,end_idx=len(arr)-1)
    print("Target element is found at index", idx) #if idx = -1 then target not found.
