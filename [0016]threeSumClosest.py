class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = len(nums)
        ans = nums[0] + nums[1] + nums[count-1]
        for i in range(count - 2):
            l = i + 1
            r = count - 1
            while(l < r):
                sums = nums[i] + nums[l] + nums[r]
                if(abs(sums-target) < abs(ans-target)):
                    ans = sums
                if(sums > target):
                    r-=1
                elif(sums < target):
                    l+=1
                else:
                    return ans
        return ans
