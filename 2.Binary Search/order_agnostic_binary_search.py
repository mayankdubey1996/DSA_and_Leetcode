def binary_search_acs(arr, target):
    start_idx,end_idx = 0, len(arr)-1
    found_idx = -1
    while end_idx>=start_idx:
        mid_idx = (start_idx+end_idx) //2 #floor division
        if arr[mid_idx] == target:
            return mid_idx
        elif target>arr[mid_idx]:
            start_idx=mid_idx+1
        else:
            end_idx=mid_idx-1
    return found_idx

def binary_search_dsc(arr, target):
    start_idx,end_idx = 0, len(arr)-1
    found_idx = -1
    while end_idx>=start_idx:
        mid_idx = (start_idx+end_idx) //2 #floor division
        if arr[mid_idx] == target:
            return mid_idx
        elif target>arr[mid_idx]:
            end_idx=mid_idx-1
        else:
            start_idx=mid_idx+1
    return found_idx


def order_agnostic_binary_search(arr,target):
    start_idx, end_idx = 0,len(arr)-1
    if end_idx == 0:
        return -1
    if arr[end_idx]>arr[start_idx]:
        return binary_search_acs(arr, target)
    return binary_search_dsc(arr, target)

if __name__ == '__main__':
    #arr = [2,4,9,10,12,14,18,19]
    arr = [19,18,14,12,10,9,4,2]
    target = 18
    idx = order_agnostic_binary_search(arr,target)
    print("Target element is found at index", idx) #if idx = -1 then target not found.
