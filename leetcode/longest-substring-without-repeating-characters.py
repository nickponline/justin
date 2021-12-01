class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)

        max_length = -1
        char_window = ""

        for i in range(len(s)):

            # if we see a character we've seen then remove all characters
            # before it too
            if s[i] in char_window:
                char_window = char_window[char_window.index(s[i]) + 1:]
            char_window = char_window + s[i]
            max_length = max(max_length, len(char_window))

        return max_length


solution = Solution()
solution.lengthOfLongestSubstring("abcabcbb")
