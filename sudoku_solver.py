#Sudoku Solver
# 1 -> Find empty spaces
# 2 -> Check Whther Guess is right [Check ROW, COLUMN, GRID]
# 3 -> Solve

from pprint import pprint

def find_empty(problem):
    for I in range(9):
        for J in range(9):
            if problem[I][J] == -1:
                return I, J
    return None, None  # No empty spaces

def right_guess(problem, Guess, R, C):
    R_Val = problem[R]
    if Guess in R_Val: #Eradicating duplicate numbers for ROW
        return False
    C_Val = []
    C_Val=[problem[I][C] for I in range(9)] #Eradicating duplicate numbers for COLUMN
    if Guess in C_Val:
        return False
    #Iterate over 3 rows and 3 columns -> one square grid
    R_Start=(R//3)*3 # 1//3 = 0, 5//3 = 1
    C_Start=(C//3)*3
    #Check whether in the 3x3 square the Guess number is there
    for K in range(R_Start, R_Start+3):
        for L in range(C_Start, C_Start+3):
            if problem[K][L]==Guess:
                return False
    return True

def sudoku_solver(problem):
    R,C = find_empty(problem)
    if R is None:
        return True # Solved problem nothing to fill

    #Make guess continuously
    for Guess in range(1, 10):
        #check validity
        if right_guess(problem, Guess, R, C): #Guess is correct
            #Put Guess on problem
            problem[R][C]=Guess
            if sudoku_solver(problem):
                return True
        #Backtracking if Guess wrong
        problem[R][C]=-1 #Resetting value to -1
    #No solution
    return False


# Type 1
'''
problem=[]
for I in range(1, 10):
    sub_list=[]
    for J in range(1, 10):
        print("Enter Row >", I, "Column >", J, "Value [-1 if empty]")
        UI=int(input(">>>"))
        sub_list.append(UI)
        if sub_list!=[] and len(sub_list)==9:
            problem.append(sub_list)
'''
        
# Type 2

problem=[
    [4, -1, 9,          -1, 2, -1,          -1, 7, 1],
    [5, -1, -1,         7, 8, -1,           9, 6, 3],
    [-1, 7, -1,         9, -1, -1,          -1, 4, 8],

    [-1, -1, -1,        -1, 9, -1,          -1, -1, -1],
    [-1, -1, 5,         2, 1, -1,           -1, -1, 4],
    [6, -1, 4,          -1, -1, -1,         -1, -1, -1],

    [-1, -1, -1,      5, -1, 2,      8, -1, -1],
    [-1, 6, -1,        -1, -1, -1,      -1, 5, -1],
    [9, -1, -1,        -1, 4, -1,      -1, -1, 7]
    ]
sudoku_solver(problem)
print("","_"*13, " "*7,"_"*13, " "*7,"_"*13)
R=0
for I in problem:
    R+=1
    C=-1
    print("|", end="  ")
    for J in I:
        C+=1
        if C!=0 and C%3==0 and C!=9:
            print("      |  ", end = "")
        if C==9:
            print("\n", end='')
        print(J, end = "  |  ")
    print()
    if R%3==0 and R!=0:
        print("","_"*13, " "*7,"_"*13, " "*7,"_"*13)
        print()
    if R!=9:
        print("","_"*13, " "*7,"_"*13, " "*7,"_"*13)
