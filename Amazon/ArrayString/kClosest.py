class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distances = []

        for point in points:
            x = point[0]
            y = point[1]

            distance = (x ** 2 + y ** 2)

            distances.append([distance, point])

        distances.sort(key=lambda x: x[0])

        return [point for distance, point in distances[:K]]

