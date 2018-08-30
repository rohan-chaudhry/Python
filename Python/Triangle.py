#  File: Triangle.py

#  Description: A8

#  Student's Name: Rohan Chaudhry

#  Student's UT EID: rc43755

#  Partner's Name: Daniel Snyder

#  Partner's UT EID: djs3928

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: March 3

#  Date Last Modified: march 9



###################################################


# following format given in assignment page

import time

#########################
# returns the greatest path sum using exhaustive search
def exhaustive_search (grid):
    b = []
    index = 0
    #print(search(grid,b,3,0,0))
    #print(search(grid,0,0))
    return search(grid,0,0)



''' 
def search(grid, b, idx1,idx2, index):
    # grid is the 2D array
    # idx1 and idx2 are indexes for a specific value in the array
    if idx1 == 0:
        print(idx1, idx2)
        return grid[idx1][idx2]
    else:
        print('\nstart func')
        print (idx1,idx2 )
        print(grid[idx1][idx2])
        print('hi')
        ans = grid[idx1][idx2] + search(grid,b,idx1-1,idx2,index)
        return ans
'''
''' 
def search(grid,r,c):
    current = grid[r][c]
    if r < len(grid) - 1:
        below_paths = search(grid, r+1, c) + search(grid, r+1, c+1)
        return [[current] + path for path in below_paths]

    else:
        return [[current]]
'''

def search(grid, i ,j):
    n = len(grid)
    if (i > n-1):
        return 0
    elif (j > i+1):
        pass
    else:
        t1 = search(grid,i+1, j)
        t2 = search(grid,i+1,j+1)
        t = max(t1,t2) + grid[i][j]
    return t

########################
# returns the greatest path sum using greedy approach
def greedy(greedy_grid):
    L = len(greedy_grid)
    new_grid = greedy_grid
    sum = greedy_grid[0][0]
    index = 0
    for i in range(1,L): # row count after first row
        # actual number in the row
        for j in range (index,index+1):
            portion = greedy_grid[i][index:index+2]
            if greedy_grid[i][index] > greedy_grid[i][index+1]:
                index = index
            else:
                index += 1

            maximum = max(portion)
            sum+= maximum

            #print(sum) # check
        ''' 
        print('actual sum') # check 
        print(sum)
        '''

    return sum

########################

# returns the greatest path sum using divide and conquer (recursive) approach

def rec_search_1 (grid,i,j): # triangle 1
    n = len(grid)
    if (i > n-1):
        return 0
    elif (j > i+1):
        pass
    else:
        t1 = search(grid,i+1, j)
        t2 = search(grid,i+1,j+1)
        t_s1 = max(t1,t2) + grid[i][j]
    return t_s1



def rec_search_2 (grid,i,j): # triangle 2
    n = len(grid)
    if (i > n-1):
        return 0
    elif (j > i+1):
        pass
    else:
        t1 = search(grid,i+1, j)
        t2 = search(grid,i+1,j+1)
        t_s2 = max(t1,t2) + grid[i][j]
    return t_s2

def rec_search(rec_grid):
    return rec_grid[0][0] + max(rec_search_1(rec_grid,1,0), rec_search_2(rec_grid,1,1))

''' 
def search(grid, i ,j):
    n = len(grid)
    if (i > n-1):
        return 0
    elif (j > i+1):
        pass 
    else:
        t1 = search(grid,i+1, j)
        t2 = search(grid,i+1,j+1)
        t = max(t1,t2) + grid[i][j]
    return t
'''


#######################

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (dyn_grid):
    # bottom up approach
    L = len(dyn_grid)
    alt_grid = dyn_grid

    for i in range(L-1, 0, -1):

        for j in range (0, i): # from first value in row to last
            if( dyn_grid[i][j] > dyn_grid[i][j+1] ):
                alt_grid[i-1][j] +=  dyn_grid[i][j]
            else:
                alt_grid[i-1][j] += dyn_grid[i][j+1]
    max_altsum = alt_grid[0][0]
    # print(max_sum)  #check
    return max_altsum #, alt_grid #, new_grid # return the max sum

########################


# reads the file and returns a 2-D list that represents the triangle
def read_file ():
    grid = []
    infile = open('triangle.txt',"r", encoding="utf8")
    # infile = open('test_tri2.txt', "r", encoding="utf8")
    num_lines = infile.readline() # read first line --> how many lines are in TXT file
    # create 2D list
    for line in infile:
        row = []
        line.strip()
        line = line.split()
        for num in line:
            num = int(num)
            row.append(num)
        grid.append(row)
        # print(grid) # check if returning 2D list
    #print (grid) # check if grid is correct
    return grid

##################################

def main():
    # read triangular grid from file
    grid = read_file()
    ex_grid = grid
    dyn_grid = grid
    greedy_grid = grid
    rec_grid = grid


######################################################################## EXHAUSTIVE SEARCH
    ti = time.perf_counter()
    # output greates path from exhaustive search
    tf = time.perf_counter()
    del_t = tf - ti
    # print time taken using exhaustive search

    print('\nThe greatest path sum through exhaustive search is ' + str(exhaustive_search(ex_grid)) + str('.'))
    print('The time taken for exhaustive search is ' + str(del_t) + ' seconds.')



######################################################################## GREEDY
    ti = time.perf_counter()
    # output greates path from greedy approach
    tf = time.perf_counter()
    del_t = tf - ti
    # print time taken using greedy approach
    print('\nThe greatest path sum through greedy search is ' + str(greedy(greedy_grid)) + str('.'))
    print('The time taken for dynamic programming is ' + str(del_t) + ' seconds.')

######################################################################## DIVIDE AND CONQUER

    ti = time.perf_counter()
    # output greates path from divide-and-conquer approach
    tf = time.perf_counter()
    del_t = tf - ti
    # print time taken using divide-and-conquer approach
    print('\nThe greatest path sum through recursive search is ' + str(rec_search(rec_grid)) + str('.'))
    print('The time taken for recursive search is ' + str(del_t) + ' seconds.')



######################################################################## DYNAMIC PROGRAMMING
    ti = time.perf_counter()
    # output greates path from dynamic programming
    tf = time.perf_counter()
    del_t = tf - ti
    # print time taken using dynamic programming
    # print only the max sum of dynamic
    #print('\nThe greatest path sum through dynamic programming is ' + str(dynamic_prog(dyn_grid)[0]) + str('.'))
    print('\nThe greatest path sum through dynamic programming is ' + str(dynamic_prog(dyn_grid)) + str('.'))
    print('The time taken for dynamic programming is ' + str(del_t) + ' seconds.')



if __name__ == "__main__":
    main()
