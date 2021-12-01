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
            # push open brackets onto top of the stack
            if i in '({[':
                stack.append(i)
            # closed brackets should match top of stack
            else:
                # check for too many closed brackets
                if len(stack) == 0:
                    return False
                # pop most recent opening brack from top of stack
                top = stack.pop()
                # check closed bracket matches type
                if reversed[top] != i:
                    return False

        # check for too many open brackets
        return len(stack) == 0
