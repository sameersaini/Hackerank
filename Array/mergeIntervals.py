class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda elem: elem[0])

        i = 1
        ret = [intervals[0]]
        while i < len(intervals):
            first = ret[-1]
            second = intervals[i]

            diff = min(first[1], second[1]) - max(first[0], second[0])
            if diff >= 0:
                ret[-1] = [first[0], max(first[1], second[1])]
            else:
                ret.append(second)

            i += 1

        return ret
