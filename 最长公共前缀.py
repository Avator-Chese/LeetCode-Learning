class Solution:
    def fun(self, s: list) -> str:
        size = ""
        if len(s) == 0:
            return size
        for i in range(len(s[0])):
            sta = []
            for j in s:
                if i < len(j):
                    sta.append(j[i])
                else:
                    sta.append("0")
            if len(set(sta)) == 1:
                size += sta[0]
            else:
                break
        return size


a = Solution()
print(a.fun(["adw", "adw", "adc"]))
