class Solution:
    def strStr(self,haystack, needle):
        size = len(needle)
        size2=len(haystack)
        if size == 0:
            return 0
        if size2 == 0:
            return -1
        new_list = []
        i=0
        while i+size<=size2:
            new_list.append(haystack[i: i + size])
            if new_list[i] == needle:
                return i
                break
            i=i+1
        return -1
a=Solution()
print(a.strStr("hello","ll"))