class Solution:
    def isValid(self, s: str) -> bool:
        ch=0
        stack =[]
        for ch in range (len(s)):
            if s[ch]=='(' or s[ch]=='{' or s[ch]=='[':
                stack.append(s[ch])
            else:
                if not stack:
                    return False
                top=stack.pop()
                if s[ch]==')'and  top!= '(':
                    return False
                elif s[ch]=='}'and  top!= '{':
                    return False
                elif s[ch]==']'and  top!= '[':
                    return False
        return len(stack)==0