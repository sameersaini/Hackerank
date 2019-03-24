"""
The idea is to first find a window and then try to remove chars from the left to see if we can
remove chars which are not required to find a smaller window.

So, here it goes:

Maintain 2 maps:
Tmap = stores the counter of the chars in T
Smap = keeps the track of counter of chars in the current window

left and right pointers keep track of the current widow,
then the task is to check if the current window contains all the chars of T ot not.

For every right element, updates its counter in Smap. If the counter for that element in Smap is
less than or equal to counter in T, the increase the matchCount.
If matchCount == len(t),
    then try removing elements from left to see if smaller window exits
    the condition to remove left element is that either left element should not be in Tmap
    or the counter of left in Smap is greater than the counter in Tmap

After this the size of the window is obtained using right-left+1.
The update the minWindow accordingly.
"""

from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""

        Tmap = Counter(t)
        Smap = {char: 0 for char in s}
        minWindow = len(s) + 1
        start_index = -1
        left, right = 0, 0
        matchCount = 0

        while right < len(s):
            Smap[s[right]] += 1

            if s[right] in Tmap and Smap[s[right]] <= Tmap[s[right]]:
                matchCount += 1

            if matchCount == len(t):
                while (s[left] not in Tmap) or (Smap[s[left]] > Tmap[s[left]]):
                    Smap[s[left]] -= 1
                    left += 1

                windowSize = right - left + 1

                if windowSize < minWindow:
                    minWindow = windowSize
                    start_index = left

            right += 1

        if start_index == -1:
            return ""
        else:
            return s[start_index: start_index + minWindow]