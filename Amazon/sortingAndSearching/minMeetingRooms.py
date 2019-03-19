"""
The idea is to first sort the intervals by start time.
Then use a min heap to store the end times of the intervals
If the rnd time of the top interval is smaller or equal to the start time of the interval,
then pop the top interval from the min heap
add the current intercval's end time to the heap
Finally, return the length of the heap
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda interval: interval.start)

        heap = []
        heapq.heappush(heap, intervals[0].end)

        for interval in intervals[1:]:
            if heap[0] <= interval.start:
                heapq.heappop(heap)

            heapq.heappush(heap, interval.end)

        return len(heap)
