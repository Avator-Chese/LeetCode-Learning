class Solution:
    def isValid(self,x: str) -> bool:
        d = {"}": "{", "]": "[", ")": "("}
        stack = []
        for i in x:
            if i not in d:
                stack.append(i)
            else:
                top_element=stack.pop() if bool(stack) else "#"
                if d[i] != top_element:
                    return False
        return not bool(stack)
        
a=Solution()
print(a.isValid("{(}}"))
