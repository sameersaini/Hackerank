#!/bin/python3

# Complete the largestRectangle function below.
# O(N) solution
def largestRectangle(h):
    maxArea = 0
    #to push the indices
    stack = []
    length = len(h)
    i = 0
    while i < length:
        if len(stack) == 0 or h[i] >= h[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            valueAtTop = h[top]
            if len(stack) == 0:
                value = i
            else:
                value = i - stack[-1] - 1
            currentArea = valueAtTop * value

            if currentArea > maxArea: maxArea = currentArea

    while len(stack) != 0:
        top = stack.pop()
        valueAtTop = h[top]
        if len(stack) == 0:
            value = i
        else:
            value = i - stack[-1] - 1
        currentArea = valueAtTop * value

        if currentArea > maxArea: maxArea = currentArea

    return maxArea


if __name__ == '__main__':
    n = int(input())
    h = list(map(int, input().rstrip().split()))
    result = largestRectangle(h)
    print(result)