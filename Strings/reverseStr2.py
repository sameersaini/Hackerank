class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        length = len(s)
        Twok = 2 * k

        exacts = length // (Twok)
        lefts = length - exacts * (Twok)

        for i in range(exacts):
            start = Twok * i
            end = Twok * (i + 1) - 1

            s = s[:start] + s[start:start + k][::-1] + s[start + k:]

        if exacts == 0:
            end = 0
        else:
            end = end + 1

        if lefts < k:
            s = s[:end] + s[end:][::-1]
        elif lefts >= k:
            s = s[:end] + s[end:end + k][::-1] + s[end + k:]

        return s