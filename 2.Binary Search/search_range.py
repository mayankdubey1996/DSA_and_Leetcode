class Solution:
    def bin_search_s_m(self,nums, target,start_idx,mid_idx,ansL):
        self.start_idx = start_idx
        self.end_idx = mid_idx
        while self.end_idx>=self.start_idx:
            self.mid_idx = (self.start_idx+self.end_idx)//2
            if target==nums[self.mid_idx]:
                ansL = self.mid_idx
                self.end_idx = self.mid_idx-1
            elif target>nums[self.mid_idx]:
                self.start_idx=self.mid_idx+1
            else:
                self.end_idx=self.mid_idx-1
        return ansL

    def bin_search_m_r(self,nums, target,mid_idx,end_idx,ansR):
        self.start_idx = mid_idx
        self.end_idx = end_idx
        while self.end_idx>=self.start_idx:
            self.mid_idx = (self.start_idx+self.end_idx)//2
            if target==nums[self.mid_idx]:
                ansR = self.mid_idx
                self.start_idx=self.mid_idx+1
            elif target>nums[self.mid_idx]:
                self.start_idx=mid_idx+1
            else:
                self.end_idx=self.mid_idx-1
        return ansR

    def searchRange(self, nums, target: int):
        start_idx, end_idx = 0, len(nums)-1
        ansL=-1
        ansR=-1
        while end_idx>=start_idx:
            mid_idx = (start_idx+end_idx)//2
            if nums[mid_idx]==target:
                ansL = mid_idx
                ansR = mid_idx
                print("RUN")
                #search on left_side
                ansL = self.bin_search_s_m(nums, target,start_idx,mid_idx-1,ansL)
                #search on right_side
                ansR = self.bin_search_m_r(nums, target,mid_idx+1,end_idx,ansR)
                break
            elif target>nums[mid_idx]:
                start_idx=mid_idx+1
            else:
                end_idx=mid_idx-1
        return [ansL,ansR]

if __name__ =="__main__":
    
    nums = [1,8,8,8,8]
    target = 8
    s = Solution()
    x = s.searchRange(nums, target)
    print(x) 
            

        