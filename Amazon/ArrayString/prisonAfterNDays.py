"""
The pattern repeats after every 14 days. So N = N % 14 and if N == 0 then set N = 14
Create a new array for every day and fill it based on the condition given in the question
"""

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        old = cells
        N = N % 14
        if N == 0: N = 14
        for i in range(N):
            new = [0 for _ in range(8)]

            for j in range(1, 7):
                if old[j - 1] == old[j + 1]:
                    new[j] = 1
            old = new

        return old
