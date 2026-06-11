class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hashmap = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }          

        for char in s:
            if char not in hashmap:
                stack.append(char)
            else:
                if stack and hashmap[char] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
