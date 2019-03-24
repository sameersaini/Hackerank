"""
The idea is to create a stack and push all celebrities to the stack.
Then for every pair of celebrities, check knows(a,b)
if true then a knows b so a cannot be celebrity, so discard a and put b back coz b can be celebrity
else a does not know b, so b cannot be celebrity, so discard b and put a back coz a can be celebrity
Repeat this till only one celebrity remains in the stack

The for this celebrity, check if this celebrity does not anyone and everyone knows celebrity.
"""

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        celibrityStack = [i for i in range(n)]

        while len(celibrityStack) > 1:
            a = celibrityStack.pop()
            b = celibrityStack.pop()

            if knows(a, b):
                celibrityStack.append(b)
            else:
                celibrityStack.append(a)

        celibrity = celibrityStack[0]

        # if celebrity know anyone or anyone doesnot know celebrity then return -1
        for i in range(n):
            if i != celibrity and (knows(celibrity, i) or not knows(i, celibrity)):
                return -1
        else:
            return celibrity
