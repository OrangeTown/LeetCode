class Solution:
    def maxArea(self, height: List[int]) -> int:
        aMin = 0
        aMax = len(height) - 1
        areaMax = 0
        while(aMin < aMax):
            if(height[aMin] > height[aMax]):
                area = height[aMax] * (aMax - aMin)
                aMax -= 1
            else:
                area = height[aMin] * (aMax - aMin)
                aMin += 1
            if(area > areaMax):
                areaMax = area
        return areaMax
