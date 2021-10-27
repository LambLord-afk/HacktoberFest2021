'''
FROM LEETCODE - 55

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps 
to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2
'''



'''
Logic: The leftmost jump is looked for in each iteration. We have done i+nums[i]>=h as we intend to take single steps 
before taking a jump to the last index. For example, in our first example test case, the condition satisfies for 
1+3>=4. Thus here we are assuming that before taking a jump of three steps, we take a single step to nums[1], i.e. 3. 
After that, when we know that we have to reach nums[1] now instead of nums[4], we update the last index to 1. 
'''
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h=len(nums)-1
        c=0         #Keeps count of the jumps
        
        while(h!=0):
            for i in range(h):
                if i+nums[i]>=h:
                    c+=1
                    h=i
                    break
                    
        return c



        
        '''
        def rec(nums,j,l):
            if j==nums[-1]:
                l.append(j)
                if l not in self.jump:
                    self.jump.append(l)
                return
            l.append(j)
            for i in range(1,j+1):
                if (self.s+i)<len(nums):
                    rec(nums,nums[self.s+i],l)
            return    
                
        self.jump=[]
        self.s=0
        rec(nums,nums[self.s],[])
        self.jump.sort(key=len)
        return len(self.jump[0])-1
        '''        