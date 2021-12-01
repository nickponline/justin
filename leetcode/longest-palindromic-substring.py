class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        best_palindrone = None
        best_length = 0

        for i in range( len(s) ):

            # check odd length palindrones
            j = i - 1
            k = i + 1

            while j >= 0 and k < len(s) and s[j] == s[k]:
                j -= 1
                k += 1

            if (k - j + 1) > best_length:
                best_length = k - j + 1
                best_palindrone = s[j+1:k]

            # check even length palindrones
            j = i
            k = i + 1

            while j >= 0 and k < len(s) and s[j] == s[k]:
                j -= 1
                k += 1

            if (k - j + 1) > best_length:
                best_length = k - j + 1
                best_palindrone = s[j+1:k]

        return best_palindrone
