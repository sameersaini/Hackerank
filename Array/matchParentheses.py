class Solution:
    def isValid(self, s):
        if len(s) == 0:
            return True
        stack = []
        i = 0


        while i < len(s):
            if s[i] in ['{', '[', '(']:
                stack.append(s[i])
            elif s[i] in ['}', ']', ')']:
                stackSize = len(stack)
                if stackSize > 0:
                    if s[i] == '}' and stack[stackSize-1] == '{':
                        stack.pop()
                    elif s[i] == ']' and stack[stackSize-1] == '[':
                        stack.pop()
                    elif s[i] == ')' and stack[stackSize-1] == '(':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            i += 1

        if len(stack) == 0:
            return True
        else:
            return False