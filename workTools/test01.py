def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    res = ""
    a = ""
    b = list(s)
    for str in s:
        if str not in a:
            a.join(str)
        else:
            res = a
            a = ""
            a.join(str)
    print(a)


lengthOfLongestSubstring("abcabcbb")
