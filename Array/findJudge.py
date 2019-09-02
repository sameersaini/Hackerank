class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        """
        create the trust map for every person
        iterate over trust map and 
        for every person who is trusted by everyone else
        check if this person is not in any other persons map.
        """
        trustMap = {}
        if N <= 1:
            return 1

        for a, b in trust:
            trustMap[a] = []
            trustMap[b] = []

        for a, b in trust:
            trustMap[b].append(a)

        for person in trustMap:
            if len(trustMap[person]) == N - 1:
                for person1 in trustMap:
                    if person in trustMap[person1]:
                        break
                else:
                    return person
        else:
            return -1
