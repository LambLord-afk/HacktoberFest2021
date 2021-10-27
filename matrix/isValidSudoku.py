'''
FROM LEETCODE - 36

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
'''






class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        l=[]
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    s1="Row : "+str(i)+" "+str(board[i][j])                 #For checking in row
                    s2="Column : "+str(j)+" "+str(board[i][j])              #For checking in column
                    s3="Box : "+str((i//3)*3+(j//3))+" "+str(board[i][j])   #For checking in boxes (The number inside the str() function indicates the box no.)
                    if s1 in l:
                        return False
                    else:
                        l.append(s1)
                    if s2 in l:
                        return False
                    else:
                        l.append(s2)
                    if s3 in l:
                        return False
                    else:
                        l.append(s3)
                    
        return True


        
        '''
        This is a brute force approach, so the code is long and not really optimal 
        
        
        
        l=[]
        #Row-wise
        for i in range(len(board[0])):
            l=[]
            for j in range(len(board)):
                if board[i][j].isdigit() and board[i][j] in l:
                    return False
                elif board[i][j].isdigit() and board[i][j] not in l:
                    l.append(board[i][j])
        print(l)
        

        #Column-wise
        l=[]
        for i in range(len(board[0])):
            l=[]
            for j in range(len(board)):
                if board[j][i].isdigit() and board[j][i] in l:
                    return False
                    break
                elif board[j][i].isdigit() and board[j][i] not in l:
                    l.append(board[j][i])
        print(l)


        #For checking the 3*3 boxes
        i=0
        j=0
        k=0
        l=[]
        while(True):
            for i in range(k,k+3):
                for j in range(3):
                    if board[i][j].isdigit() and board[i][j] in l:
                        return False
                    elif board[i][j].isdigit() and board[i][j] not in l:
                        l.append(board[i][j])
            if i==2:
                k=3
                l=[]
            elif i==5:
                k=6
                l=[]
            elif i==8 and j==2:
                break

        i=0
        j=0
        k=0
        l=[]
        while(True):
            for i in range(k,k+3):
                for j in range(3,6):
                    if board[i][j].isdigit() and board[i][j] in l:
                        return False
                    elif board[i][j].isdigit() and board[i][j] not in l:
                        l.append(board[i][j])
            if i==2:
                k=3
                l=[]
            elif i==5:
                k=6
                l=[]
            elif i==8 and j==5:
                break

        i=0
        j=0
        k=0
        l=[]
        while(True):
            for i in range(k,k+3):
                for j in range(6,9):
                    if board[i][j].isdigit() and board[i][j] in l:
                        return False
                    elif board[i][j].isdigit() and board[i][j] not in l:
                        l.append(board[i][j])
            if i==2:
                k=3
                l=[]
            elif i==5:
                k=6
                l=[]
            elif i==8 and j==8:
                break

        return True
        '''