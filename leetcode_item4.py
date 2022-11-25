from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_list = nums1 + nums2
        merge_list.sort()
        n =len(merge_list) // 2
        if len(merge_list) % 2 != 0 :
            median = merge_list[n]
            return median
        else:
            median = (merge_list[n-1] + merge_list[n]) / 2
            return median

Solution().findMedianSortedArrays([1,2],[3,4])

