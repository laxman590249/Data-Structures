"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


"""
# The idea is to add ')' only after valid '('
# We use two integer variables left & right to see how many '(' & ')' are in the current string
# If left < n then we can add '(' to the current string
# If right < left then we can add ')' to the current string
# Python Code:

def generateParenthesis(self, n: int) :
	def dfs(left, right, s):
		if len(s) == n * 2:
			res.append(s)
			return

		if left < n:
			print(left, right, s)
			dfs(left + 1, right, s + '(')

		if right < left:
			print(left, right, s)
			dfs(left, right + 1, s + ')')

	res = []
	dfs(0, 0, '')
	return res
generateParenthesis(1, 3)


