class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        reversed = {
            '[' : ']',
            '(' : ')',
            '{' : '}',
        }
        stack = []
        for i in s:
            # open brackets
            if i in '({[':
                stack.append(i)
            # close brackets
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if reversed[top] != i:
                    return False

        return len(stack) == 0
