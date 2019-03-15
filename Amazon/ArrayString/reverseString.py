class Solution:
    def reverse(self, l, start, end):
        if start >= end:
            return

        l[start], l[end] = l[end], l[start]

        return self.reverse(l, start + 1, end - 1)

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s) - 1)
