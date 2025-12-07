class Solution:
    def reverseParentheses(self, s: str) -> str:
	# Use two stacks
        stack = []
        curr = []
        for c in s:
            if c == "(":
                stack.append(list(curr))
                curr = []
            elif c.islower():
                curr.append(c)
            else:
                curr_rev = reversed(curr)
                curr = stack.pop()
                curr += curr_rev
        return "".join(curr)
