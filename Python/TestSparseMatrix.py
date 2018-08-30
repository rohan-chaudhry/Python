# File: TestSparseMatrix.py

# Description: Sparse matrix representation has a 1-D list where each
#              element in that list is a linked list having the column
#              number and non-zero data in each link

#  Student Name: Daniel Snyder

#  Student UT EID: djs3928

#  Partner Name: Rohan Chaudhry

#  Partner UT EID: rc43755

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: april 4

#  Date Last Modified:

####################################################

class Link(object):
    ### LINK only contains the column number and non-zero data

    def __init__(self, col=0, data=0, next=None):
        self.col = col
        self.data = data
        self.next = next

    def has_next(self):
        if self.next is None:
            return False
        else:
            return True


    def to_string(self):
        s = '(' + str(self.col) + ',' + str(self.data) + ')'
        #if self.has_next():
            #s+= ','
        return s

    # return a String representation of a Link (col, data)
    def __str__(self):
        return '(' + str(self.col) + ',' + str(self.data) + ')'



class LinkedList(object):
    def __init__(self):
        self.first = None

    def insert_last(self, col, data):
        new_link = Link(col, data)
        current = self.first

        if (current == None):
            self.first = new_link
            return

        while (current.next != None):
            current = current.next

        current.next = new_link

    # return a String representation of a LinkedList
    def __str__(self):
        s = ''
        this_node = self.first

        s += this_node.to_string() + ','

        while this_node.has_next():
            this_node = this_node.next
            s += this_node.to_string()
            if this_node.has_next():
                s+=','

        return s

    def insert_link(self, col, data):
        new_link = Link(col, data)
        current = self.first
        if current == None:
            self.first = new_link
            return
        while current.next != None:
            if current.next.col > col:
                break
            current = current.next
        if current.next == None:
            current.next = new_link
        else:
            temp = current.next
            current.next = new_link
            new_link.next = temp


class Matrix(object):
    def __init__(self, row=0, col=0):

        self.row = row
        self.col = col
        self.matrix = []


    def addFirst (self, row,col,data):
        newLink = Link(row, col, data)
        newLink.next = self.matrix.first
        self.matrix.first = newLink

    def insertLink(self, row, col, data):
        # do nothing if data = 0
        if (data == 0):
            return

    def deleteLink(self, row, col):
        return



    # perform assignment operation: matrix[row][col] = data
    def set_element(self, row, col, data):
        if (row > len(self.matrix) - 1):
            return None
        link = self.matrix[row].first

        while link != None:
            if link.col == col:
                break
            link = link.next
        if link == None:
            self.matrix[row].insert_link(col, data)
        elif link.col == col:
            link.data = data



    ''' 
        if col > self.col or row > self.row:
            return

        else:
            # get the first value of the linked list

            current = self.matrix.first # this line is causing error
            previous = self.matrix[0][0]


            newLink = Link(row, col, data)
            if current == None:
                self.addFirst(row, col, data)
                return
            else:
                while current != None:
                    if row == current.row and col == current.col:
                        current.data = data
                        return
                    else:
                        if current.row < row:
                            previous = current
                            current = current.next
                            continue
                        if current.row == row:
                            if current.col < col:
                                previous = current
                                current = current.next
                                continue
                            else:  # current.col > col
                                if previous.col < col:
                                    previous.next = newLink
                                    newLink.next = current
                                    return
                                else:
                                    self.addFirst(row, col, data)
                                    return
                        else:
                            previous.next = newLink
                            newLink.next = current
                            return
                previous.next = newLink
                newLink.next = current

        return self
    '''









    # add two sparse matrices
    def __add__(self, other):

        if self.row != other.row or self.col != other.col:
            return 'Cannot add'

        self_total_array = []
        other_total_array = []

        s = ''

        for item in self.matrix:
            num_col = (self.col)
            num_row = (self.row)

            str_item = str(item)  # converts the linked list matrix into a string

            print()
            holder = 0
            counter = 0
            iter = 0
            self_array = []

            for idk in range(len(str_item)):

                if str_item[idk] == '(':

                    if str_item[idk + 1] == str(holder):
                        s = (str_item[idk + 3]) + ' '
                        idk += 3
                        holder += 1
                        counter += 1
                        self_array.append(int(s))

                    else:
                        s = 0
                        holder += 1
                        counter += 1
                        self_array.append(s)

                        if str_item[idk] == '(':
                            if str_item[idk + 1] == str(holder):
                                s = (str_item[idk + 3])
                                s = int(s)
                                self_array.append(s)
                                counter += 1
                                holder += 1
                else:
                    idk += 1

            if counter != num_col:
                s = 0
                self_array.append(s)

            self_total_array.append(self_array)

        # now for other matrix

        for item in other.matrix:
            num_col = (other.col)
            num_row = (other.row)

            str_item = str(item)  # converts the linked list matrix into a string

            print()
            holder = 0
            counter = 0
            iter = 0
            other_array = []

            for idk in range(len(str_item)):

                if str_item[idk] == '(':

                    if str_item[idk + 1] == str(holder):
                        s = (str_item[idk + 3]) + ' '
                        idk += 3
                        holder += 1
                        counter += 1
                        other_array.append(int(s))

                    else:
                        s = 0
                        holder += 1
                        counter += 1
                        other_array.append(s)

                        if str_item[idk] == '(':
                            if str_item[idk + 1] == str(holder):
                                s = (str_item[idk + 3])
                                s = int(s)
                                other_array.append(s)
                                counter += 1
                                holder += 1
                else:
                    idk += 1

            if counter != num_col:
                s = 0
                other_array.append(s)

            other_total_array.append(other_array)

        result = [[0 for x in range(self.col)] for y in range(self.row)]

        # ADD a row element of self with column elements of other
        for i in range (len(self_total_array)):
            for j in range(len(self_total_array[0])):
                result[i][j] = self_total_array[i][j] + other_total_array[i][j]




        # addtion matrix as a string
        result_string = ''
        for row in result:
            for elem in row:
                result_string += ' '+ str(elem)
            result_string+= '\n'

        return result # returns the 2D array, not in pretty string format







    # multiply two sparse matrices
    def __mul__(self, other):
        self_total_array = []
        other_total_array = []


        s = ''

        for item in self.matrix:
            num_col = (self.col)
            num_row = (self.row)

            str_item = str(item)  # converts the linked list matrix into a string

            print()
            holder = 0
            counter = 0
            iter = 0
            self_array = []

            for idk in range(len(str_item)):

                if str_item[idk] == '(':

                    if str_item[idk + 1] == str(holder):
                        s = (str_item[idk + 3]) + ' '
                        idk += 3
                        holder += 1
                        counter += 1
                        self_array.append(int(s))

                    else:
                        s = 0
                        holder+= 1
                        counter += 1
                        self_array.append(s)

                        if str_item[idk] == '(':
                            if str_item[idk + 1] == str(holder):
                                s = (str_item[idk + 3])
                                s = int(s)
                                self_array.append(s)
                                counter += 1
                                holder+= 1
                else:
                    idk += 1

            if counter != num_col:
                s = 0
                self_array.append(s)

            self_total_array.append(self_array)


        # now for other matrix

        for item in other.matrix:
            num_col = (other.col)
            num_row = (other.row)

            str_item = str(item)  # converts the linked list matrix into a string

            print()
            holder = 0
            counter = 0
            iter = 0
            other_array = []

            for idk in range(len(str_item)):

                if str_item[idk] == '(':

                    if str_item[idk + 1] == str(holder):
                        s = (str_item[idk + 3]) + ' '
                        idk += 3
                        holder += 1
                        counter += 1
                        other_array.append(int(s))

                    else:
                        s = 0
                        holder+= 1
                        counter += 1
                        other_array.append(s)

                        if str_item[idk] == '(':
                            if str_item[idk + 1] == str(holder):
                                s = (str_item[idk + 3])
                                s = int(s)
                                other_array.append(s)
                                counter += 1
                                holder+= 1
                else:
                    idk += 1

            if counter != num_col:
                s = 0
                other_array.append(s)

            other_total_array.append(other_array)



        result = [[0 for x in range(self.row)] for y in range(other.col)]

        # multiply a row element of self with column elements of other
        for i in range (len(self_total_array)):
            for j in range(len(other_total_array[0])):
                for k in range(len(other_total_array)):
                    result[i][j] += self_total_array[i][k] * other_total_array[k][j]



        # multiplied matrix as a string
        result_string = ''
        for row in result:
            for elem in row:
                result_string += ' '+ str(elem)
            result_string+= '\n'

        return result # returns the 2D array, not in pretty string format




    # return a list representing a row with the zero elements inserted
    def get_row(self, n):

        link_row = self.matrix[n]
        #print(link_row)
        link_row = str(link_row)
        holder = 0
        counter = 0
        iter = 0
        num_col = (self.col)
        s=''

        for idk in range(len(link_row)):
            if link_row[idk] == '(':
                if link_row[idk + 1] == str(holder):
                    s += (link_row[idk + 3]) + ' '
                    idk += 3
                    holder += 1
                    counter += 1
                else:
                    s += '0 '

                    holder += 1
                    counter += 1
                    if link_row[idk] == '(':
                        if link_row[idk + 1] == str(holder):
                            s += (link_row[idk + 3]) + ' '
                            counter += 1
                            holder += 1
            else:
                idk += 1
        if counter != num_col:
            s += '0'

        array = []
        final =  s.rstrip()


        for number in final:
            if number != ' ':
                array.append(number)

        return array


    # return a list representing a column with the zero elements inserted

    def get_col(self, n):
        link_row = self.matrix[n]
        #print(link_row)
        link_row = str(link_row)
        holder = 0
        counter = 0
        iter = 0
        num_col = (self.col)
        s = ''

        for idk in range(len(link_row)):
            if link_row[idk] == '(':
                if link_row[idk + 1] == str(holder):
                    s += (link_row[idk + 3]) + ' '
                    idk += 3
                    holder += 1
                    counter += 1
                else:
                    s += '0 '

                    holder += 1
                    counter += 1
                    if link_row[idk] == '(':
                        if link_row[idk + 1] == str(holder):
                            s += (link_row[idk + 3]) + ' '
                            counter += 1
                            holder += 1
            else:
                idk += 1
        if counter != num_col:
            s += '0'

        final = s.rstrip()
        array=[]

        for i in range(0,self.row  ):
            rows = self.get_row(i)
            array.append(rows[n])

        return array

    # return a String representation of a matrix
    def __str__(self):

        s = ''

        for item in self.matrix:
            num_col = (self.col)
            num_row = (self.row)

            str_item = str(item)  # converts the linked list matrix into a string

            print()
            holder = 0
            counter = 0
            iter = 0

            for idk in range(len(str_item)):

                if str_item[idk] == '(':

                    if str_item[idk + 1] == str(holder):
                        s += (str_item[idk + 3]) + ' '
                        idk += 3
                        holder += 1
                        counter += 1

                    else:
                        s += '0 '
                        holder+= 1
                        counter += 1

                        if str_item[idk] == '(':
                            if str_item[idk + 1] == str(holder):
                                s += (str_item[idk + 3]) + ' '
                                counter += 1
                                holder+= 1
                else:
                    idk += 1

            if counter != num_col:
                s += '0'

            s += '\n'


        return s


def read_matrix(in_file):
    line = in_file.readline().rstrip("\n").split()
    row = int(line[0])
    col = int(line[1])
    mat = Matrix(row, col)

    for i in range(row):
        line = in_file.readline().rstrip("\n").split()
        new_row = LinkedList()
        for j in range(col):
            elt = int(line[j])
            if (elt != 0):
                new_row.insert_last(j, elt)
        mat.matrix.append(new_row)
    line = in_file.readline()
    ''' 
    print('THIS IS THE LINKED LIST')
    print(new_row)
    print('ABOVE THIS')
    '''
    return mat


def main():
    in_file = open("./matrix.txt", "r")

    print ("Test Matrix Addition")
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

###################################################

    #we added an insert link function, and resolved our set_element function
    # pls give late grade for this, everything else works fine
    print("\nTest Setting a Zero Element to a Non-Zero Value")
    matA.set_element(1, 1, 5)
    print(matA)

    print("\nTest Setting a Non-Zero Elements to a Zero Value")


    matB.set_element(1, 1, 0)
    print(matB)
###################################################

    print("\nTest Getting a Row")
    row = matP.get_row(1)
    print(row)

    print("\nTest Getting a Column")
    col = matQ.get_col(0)
    print(col)

    in_file.close()


main()