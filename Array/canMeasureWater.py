# Determines if water jug problem is solvable
class Solution:
    def findGcd(self, A, B):
        while A:
            A, B = B % A, A

        return B

    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x == 0 and y == 0 and z == 0:
            return True
        if x == 0 and y == 0:
            return False

        if z > (x + y):
            return False

        gcd = self.findGcd(x, y)

        return z / gcd == z // gcd
