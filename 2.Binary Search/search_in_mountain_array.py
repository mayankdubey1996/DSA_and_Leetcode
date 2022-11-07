# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def binary_search_L(self,l,r,target,mountain_arr):
        while r>=l:
            mid=(l+r)//2
            print(l,mid,r)
            if mountain_arr[mid]==target:
                return mid
            elif mountain_arr[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return -1
    
    def binary_search_R(self,l,r,target,mountain_arr):
        while r>=l:
            mid=(l+r)//2
            if mountain_arr[mid]==target:
                return mid
            elif mountain_arr[mid]<target:
                r=mid-1
            else:
                l=mid+1
        return -1

    def findInMountainArray(self, target: int, mountain_arr) -> int:
        L,R = 0, len(mountain_arr)-1
        while R>=L:
            mid = (R+L)//2

            if mountain_arr[mid]> mountain_arr[mid+1] and mountain_arr[mid]>mountain_arr[mid-1]:
                print(L,mid,R)
                l_idx = self.binary_search_L(0,mid,target,mountain_arr)
                if l_idx == -1:
                    return self.binary_search_R(mid+1,len(mountain_arr)-1,target,mountain_arr)
                return l_idx
            elif mountain_arr[mid]>mountain_arr[L]:
                L=mid
            else:
                R=mid-1
        return -1

if __name__=="__main__":
    s = Solution()
    mountain_arr = [0,1,2,4,2,1]
    target = 2
    
    idx = s.findInMountainArray(target,mountain_arr)
    print(idx)