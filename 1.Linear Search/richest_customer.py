class Solution:
    def maximumWealth(self, accounts) -> int:
        """
        Given 2d array or list of list (matrix) this function returns maximum
        sum of row.
        ARGS:
            accounts -> <list><list>
        RETURN:
            maxm    -> maximum
        """
        maxm = 0
        for customer in accounts:
            money = sum(customer)
            maxm  = max(maxm, money)

        return maxm

if __name__ == '__main__':
    accounts = [[2,8,7],[7,1,3],[1,9,5]]
    s = Solution()
    maxm = s.maximumWealth(accounts)
    print(maxm)