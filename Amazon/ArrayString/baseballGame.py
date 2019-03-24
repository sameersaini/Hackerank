class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        score = 0
        for value in ops:
            if value == "+":
                temp = scores[-1] + scores[-2]
                score += temp
                scores.append(temp)
            elif value == 'D':
                temp = 2 * scores[-1]
                score += temp
                scores.append(temp)
            elif value == 'C':
                score -= scores[-1]
                scores.pop()
            else:
                score += int(value)
                scores.append(int(value))

        return score
