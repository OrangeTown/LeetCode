class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        le = len(nums)
        if nums == None or le < 3:
            return ans
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i - 1]:
                continue
            l = i + 1
            r = le - 1
            while(l < r):
                sum = num + nums[l] + nums[r]
                if(sum == 0):
                    ans.append([num, nums[l], nums[r]])
                    while(l < r and nums[l] == nums[l+1]):
                        l+=1
                    while(l < r and nums[r] == nums[r-1]):
                        r-=1
                    l+=1
                    r-=1
                elif(sum < 0):
                    l+=1
                elif(sum > 0):
                    r-=1
        return ans
