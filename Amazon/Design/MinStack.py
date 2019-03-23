class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mainStack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.mainStack.append(x)

        if len(self.minStack) == 0:
            self.minStack.append(x)
        else:
            self.minStack.append(min(self.minStack[-1], x))

    def pop(self):
        """
        :rtype: None
        """
        self.mainStack.pop()
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.mainStack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()