# File: TestDenseMatrix.py

# Description: Matrix is represented as 2-D list

#  Student Name: Rohan Chaudhry

#  Student UT EID: rc43755

#  Partner Name: Daniel Snyder

#  Partner UT EID: djs3928

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: apr 4

#  Date Last Modified: apr 4

#################################
'''

The first program that you will complete is TestDenseMatrix.py.
The program is almost complete. You will re-work the __str__() function
such that it will return a 2-D representation of the matrix with the numbers
in neat columns right justified. Assume that the numbers given will not be
greater than 2 digits and the products will not be greater than 4 digits.
Assume also that only positive integers will be given to you.

'''

class Matrix(object):
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col
        self.matrix = []

    # perform matrix addition
    def __add__(self, other):
        if ((self.row != other.row) or (self.col != other.col)):
            return None

        mat = Matrix(self.row, self.col)
        for i in range(self.row):
            new_row = []
            for j in range(self.col):
                new_row.append(self.matrix[i][j] + other.matrix[i][j])
            mat.matrix.append(new_row)


        return mat

    # perform a matrix multiplication
    def __mul__(self, other):
        if (self.col != other.row):
            return None

        mat = Matrix(self.row, other.col)
        for i in range(self.row):
            new_row = []
            for j in range(other.col):
                sum_mult = 0
                for k in range(other.row):
                    sum_mult += self.matrix[i][k] * other.matrix[k][j]
                new_row.append(sum_mult)
            mat.matrix.append(new_row)
        return mat

    # return a string representation of a matrix
    def __str__(self):
        # justification length is determined by length of longest number
        max_len = 1
        for i in range (self.row):
            for j in range (self.col):
                num_len = len(str(self.matrix[i][j]))
                if max_len < num_len:
                    max_len = num_len

        s = ''
        for i in range (self.row):
            for j in range (self.col):
                s+= str((self.matrix[i][j])).rjust(max_len) + ' '
            s+= '\n'


        return s


def read_matrix(in_file):
    line = in_file.readline().rstrip("\n").split()
    row = int(line[0])
    col = int(line[1])
    mat = Matrix(row, col)

    for i in range(row):
        line = in_file.readline().rstrip("\n").split()
        for j in range(col):
            line[j] = int(line[j])
        mat.matrix.append(line)
    line = in_file.readline()

    return mat


def main():
    in_file = open("./matrix.txt", "r")
    #in_file = open("./test_matrix.txt", "r")

    print("Test Matrix Addition")
    matA = read_matrix(in_file)
    print(matA)
    matB = read_matrix(in_file)
    print(matB)

    matC = matA + matB
    print(matC)

    print("\nTest Matrix Multiplication")
    matP = read_matrix(in_file)
    print(matP)
    matQ = read_matrix(in_file)
    print(matQ)

    matR = matP * matQ
    print(matR)
    in_file.close()


main()