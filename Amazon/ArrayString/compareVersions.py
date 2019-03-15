class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split(".")))
        version2 = list(map(int, version2.split(".")))

        lenV1 = len(version1)
        lenV2 = len(version2)

        larger = max(lenV1, lenV2)

        for i in range(larger):
            if i >= lenV1:
                v1 = 0
            else:
                v1 = version1[i]

            if i >= lenV2:
                v2 = 0
            else:
                v2 = version2[i]

            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        return 0
