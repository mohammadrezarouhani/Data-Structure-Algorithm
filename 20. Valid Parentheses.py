# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        close_braket_idx={'{':'}','[':']','(':')'}
        st=[]

        for i in range(len(s)):
            if st and close_braket_idx.get(st[-1])==s[i]:
                st.pop()
            else:
                st.append(s[i])

        return False if st else True
    

s=Solution()

print(s.isValid('[()]{()}((()))'))