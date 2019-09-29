import sys

class Solution:
    def getK(self, nums1: List[int], i: int, nums2: List[int], j: int, k: int) -> int:
        if(i == len(nums1)):
            return nums2[j + k - 1]
        if(j == len(nums2)):
            return nums1[i + k - 1]
        if(k == 1):
            return min(nums1[i], nums2[j])
        mid1 = nums1[i + k // 2 - 1] if (i + k // 2 -1 < len(nums1)) else sys.maxsize
        mid2 = nums2[j + k // 2 - 1] if (j + k // 2 -1 < len(nums2)) else sys.maxsize
        if(mid1 < mid2):
            return self.getK(nums1, i + k // 2, nums2, j, k - k // 2)
        else:
            return self.getK(nums1, i, nums2, j + k // 2, k - k // 2)
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        return (self.getK(nums1, 0, nums2, 0, (total + 1) // 2) + self.getK(nums1, 0, nums2, 0, (total + 2) // 2)) / 2
