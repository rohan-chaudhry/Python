#  File: TestLinkedList.py

#  Description: A10

#  Student Name: Rohan Chaudhry

#  Student UT EID: rc43755

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:  51335

#  Date Created: 26 march

#  Date Last Modified:


######################################################################



# using notes given in class
class Link(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


#############################

class LinkedList(object):

    #initialize
    def __init__(self):
        self.first = None


    # get number of links
    def get_num_links(self):
        return len(LinkedList.links())

    # add an item at the beginning of the list
    def insert_first(self, item):
        new_link = Link(item)
        new_link.next = self.first
        self.first = new_link

    # add an item at the end of a list
    def insert_last(self, item):
        new_link = Link(item)
        current = self.first

        if (current == None):
            self.first = new_link
            return

        while (current.next != None):
            current = current.next

        current.next = new_link


    # add an item in an ordered list in ascending order
    def insert_in_order(self, item):
        # hello
        return

    # search in an unordered list, return None if not found
    def find_unordered(self, item):
        return
    # Search in an ordered list, return None if not found
    def find_ordered(self, item):
        return

    # Delete and return Link from an unordered list or None if not found
    def delete_link(self, item):
        previous = self.first
        current = self.first

        if (current == None):
            return None

        while (current.data != item):
            if (current.next == None):
                return None
            else:
                previous = current
                current = current.next

        if (current == self.first):
            self.first = self.first.next
        else:
            previous.next = current.next


    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        temp = self.first
        count = 0
        while(temp):
            print(temp.data, end='  ')
            temp = temp.next
            count += 1
            if (count %10 ==0):
                print()



    # Copy the contents of a list and return new list
    def copy_list(self):
        return

    # Reverse the contents of a list and return new list
    def reverse_list(self):
        return

    # Sort the contents of a list in ascending order and return new list
    def sort_list(self):
        return

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        return

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        return

    # Merge two sorted lists and return new list in ascending order
    def merge_list(self, other):
        return

    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        return

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates(self):
        return


def main():

# Test methods insert_first() and __str__() by adding more than
# 10 items to a list and printing it.
    a = [1,2,3,4,5,6,7,8,9]
    b = [10,11,12,13]
    a = Link(a)
    b = Link(b)


    print(a)

# Test method insert_last()

# Test method insert_in_order()

# Test method get_num_links()

# Test method find_unordered()
# Consider two cases - item is there, item is not there

# Test method find_ordered()
# Consider two cases - item is there, item is not there

# Test method delete_link()
# Consider two cases - item is there, item is not there

# Test method copy_list()

# Test method reverse_list()

# Test method sort_list()

# Test method is_sorted()
# Consider two cases - list is sorted, list is not sorted

# Test method is_empty()

# Test method merge_list()

# Test method is_equal()
# Consider two cases - lists are equal, lists are not equal

# Test remove_duplicates()

main()
