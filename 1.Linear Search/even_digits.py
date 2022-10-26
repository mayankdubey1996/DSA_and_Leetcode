class Solution:
    def findNumbers(self, nums) -> int:
        """
        Given the array/number function returns how many of them
        contain an even number of digits.
        ARGS:
            nums  -> list
        RETURN
            count -> integer
        """
        count = 0
        for i in range(len(nums)):
            number = nums[i]
            len_number = 0
            while number>0:
                len_number+=1
                number = number//10
            if len_number%2==0:
                count+=1
        return count

if __name__ == "__main__":
    s = Solution()
    nums = [12,345,2,6,7896]
    count = s.findNumbers(nums)
    print(count)