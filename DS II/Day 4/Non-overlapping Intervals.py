class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        size = len(intervals)
        if size<=1: return 0
        intervals.sort(key=lambda x: x[1])
        first_end = intervals[0][1]
        res = 0
        for i in range(1,size):
            start, end = intervals[i]
            if start>=first_end:
                first_end=end
            else:
                res+=1
        return res
        