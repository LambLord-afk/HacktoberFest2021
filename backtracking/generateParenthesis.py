'''
FROM LEETCODE - 22

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
'''




class Solution(object):

    def parentheses(self,s,op,cl):      #op keeps track of the number of opening brackets while cl keeps track of the no. of closing brackets
        if op==0 and cl==0:
            if s not in self.ans:
                self.ans.append(s)
            return
        if op==-1 or cl==-1:
            return
        if op>cl:
            return
        self.parentheses(s+"(",op-1,cl)
        self.parentheses(s+")",op,cl-1)
        return
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==1:
            return ["()"]
        op=n-1              #Since we are starting with an opening bracket. So n-1 for op.
        cl=n
        self.ans=[]
        self.parentheses("(",op,cl)
        return self.ans
