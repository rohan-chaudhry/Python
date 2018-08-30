#  File: TestLinkedList.py

#  Description: This file includes a number of functionalities and test cases that are designed to extend the LinkedList Class we have been developing in class.

#  Student Name: Daniel Snyder

#  Student UT EID: djs3928

#  Partner Name: Rohan Chaudhry

#  Partner UT EID: rc43755

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 3/29/18

#  Date Last Modified: 3/30/18

##############################

class Link (object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

    def to_string(self):
        return str(self.data)

    def has_next(self):
        if self.next is None:
            return False
        else:
            return True

    def __str__(self):
        return str(self.data)

class LinkedList (object):
    def __init__ (self, data):
        self.data = None
        self.head = None
        self.next = None

    # get number of links 
    def get_num_links (self):
        temp = self.head
        count = 0
        while(temp):
            count+=1
            temp=temp.next
        return count
    
    # add an item at the beginning of the list
    def insert_first (self, item):
        new_link = Link (item)
        new_link.next = self.head
        self.head = new_link

    # add an item at the end of a list
    def insert_last (self, item):
        new_link = Link (item)

        current = self.head
        if (current == None):
            self.head = new_link
            return

        while (current.next != None):
            current = current.next

        current.next = new_link
          
    # add an item in an ordered list in ascending order
    # Piazza said not to return or print anything
    def insert_in_order (self, item):
        if self.head is None:
            item.next = self.head
            self.head = item
        elif int(self.head.data.to_string()) >= item.data:
            item.next = self.head
            self.head = item

        else:
            current = self.head
            while(current.next is not None and int(current.next.data.to_string()) < item.data):
                current = current.next
            item.next = current.next
            current.next = item



    # search in an unordered list, return None if not found
    def find_unordered (self, item):
        p = self.head
        count = 1

        if (p != None):
            while (p.next != None):

                if (p.data == item):
                    return p
                count += 1
                p = p.next

            if (p.data == item):
                return 'Link ' + str(count) + ': ' + str(p.to_string())



        return None

    # Search in an ordered list, return None if not found
    def find_ordered (self, item):
        current = self.head
        found = False
        stop = False
        count = 0 # Link value
        count_link = current
        while (current != None and not found and not stop):
            if (current.data == item):
                found = True

            else:
                if (int(current.data.to_string()) > int(item.to_string())):
                    stop = True

                else:
                    current = current.next
                    count_link = current
            count += 1

        # according to Piazza, return the first link whose data is item
        if found == False:
            return None
        else:
            return 'Link ' + str(count) + ': ' + count_link.to_string()


    # Delete and return Link from an unordered list or None if not found
    def delete_link (self, item):

        curr = self.head
        prev = None
        ans = curr
        while curr:
            if curr.data == item:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next

                return ans.to_string() # returns link value only

            prev = curr
            curr = curr.next
            ans = curr

        return None


    # String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        '''
        string = ''
        temp = self.head
        count = 1
        while (temp):
            string += str(temp.data)
            string += "  "
            temp = temp.next
            count += 1
            if (count % 10 == 0):
                string += "/n"
        return(string)
        '''

        this_node = self.head
        ret_str = ''
        ret_str += this_node.to_string() + '  '
        count = 1
        while this_node.has_next():
            this_node = this_node.next
            ret_str += this_node.to_string() + '  '
            count += 1
            if count % 10 == 0:
                ret_str += '\n'

        return ret_str

    # Copy the contents of a list and return new list
    def copy_list (self):
        result = LinkedList(0)
        buffer = self.head
        while (buffer.next != None):
            result.insert_last(buffer.data)
            buffer = buffer.next
        result.insert_last(buffer.data)
        return result

    # Reverse the contents of a list and return new list
    def reverse_list (self):
        previous = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous
        return (self)

    # Sort the contents of a list in ascending order and return new list
    def sort_list (self):
        '''
        link1 = self.Link(0)  # ascending
        link2 = self.Link(0)
        # split links into lists
        self.splitList(link1,link2)
        link1 = link1.next
        link2 = link2.next
        '''

        size = self.get_num_links()

        if size > 1 :
            newList = []
            current = self.head
            newList.append(int(current.to_string()))

            while (current.has_next()) :
                current = current.next
                newList.append(int(current.to_string()))
            newList = sorted(newList)
            new_LL = LinkedList(0)

            for link in newList:
                new_LL.insert_last(link)
            return new_LL
        return self




    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):
        a = self
        b = self.sort_list()

        a_str = a.__str__().strip()
        b_str = b.__str__().strip()

        #return is_equal(self.sort_list(), self)
        return a_str == b_str
        #return (self.sort_list() == self)
        # return (self.is_equal(self))


    # Return True if a list is empty or False otherwise
    def is_empty (self):
        return (self.get_num_links() == 0)

    # Merge two sorted lists and return new list in ascending order
    def merge_list (self, other):
        '''
        if self.head is None:
            return other
        if other.head is None:
            return self

        s = t = Link(0)

        while not (self.head is None or other.head is None):
            if int(self.current.data.to_string()) < int(other.current.data.to_string()):
                c = self.current
                self.current = self.current.next
            else:
                c = other.current
                other.current = other.current.next

            t.next = c
            t = t.next
        t.next = self.head or other.head
        return s.next
        '''

        L3 = Link(None, None)
        prev = L3
        curr_s = self.head
        curr_d = other.head

        while self != None and other != None:
            if (curr_s.data) <= int(curr_d.data.to_string()):
                prev.next = curr_s
                curr_s= self.next
            else:
                prev.next = curr_d
                curr_d = other.next
            prev = prev.next
        # append the ends
        if self == None:
            prev.next = curr_d
        elif other == None:
            prev.next = curr_s

        return L3.next

    # Test if two lists are equal, item by item and return True
    def is_equal (self, other):
        current1 = self.head
        current2 = other.head
        while (current1 != None and current2 != None):
            if (current1.data != current2.data):
                return False
            current1 = current1.next
            current2 = current2.next
        return (current1 == None and current2 == None)

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates (self):
        '''
        assert self.head is not None
        anchor = self.head

        while anchor is not None:
            iterator = anchor
            while iterator is not None:
                prev = iterator
                iterator = iterator.next
                if iterator is None:
                    break
                if iterator.data == anchor.data:
                    next = iterator.next
                    prev.next = next
                    
            anchor = anchor.next
        '''
        curr = self.head
        prev = None
        dups = LinkedList(0)
        d = dict() # duplicates

        while curr:
            if curr.data in d:
                # dont add if already found
                pass
            else:
                d[curr.data] = 1
                dups.insert_first(curr.data)
                prev = curr
            curr = prev.next
        return dups





    __repr__ = __str__

def main():
    L1 = Link(1)
    L2 = Link(2)
    L3 = Link(3)
    L4 = Link(4)
    L5 = Link(5)
    L6 = Link(6)
    L7 = Link(7)
    L8 = Link(8)
    L9 = Link(9)
    L10 = Link(10)

    link_array = [L1,L2,L3,L4,L5,L6,L7,L8,L9,L10]
    rev_link_array = link_array.reverse()

    newList = LinkedList(0)

    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    for i in link_array:
        newList.insert_first(i)
    print(newList)
    print()
    newList.insert_first(L4)
    print(newList)
    print()

    # Test method insert_last()
    newList.insert_last(L3)
    print(newList)
    print()


    # Test method insert_in_order()
    newerList = LinkedList(0)
    for i in link_array:
        newerList.insert_first(i)

    L11 = Link(11)
    newerList.insert_in_order(L11)
    print(newerList)
    print()




    # Test method get_num_links()

    print(newList.get_num_links())
    print(newerList.get_num_links())
    print()

    '''
    test4link3 = Link(5, None)
    test4link2 = Link(8, test4link3)
    test4link1 = Link(10, test4link2)

    test4list = LinkedList(test4link1)
    test4list.insert_first(test4link1)
    test4list.insert_first(test4link2)
    test4list.insert_first(test4link3)
    print(test4list.get_num_links())
    '''

    # Test method find_unordered()
    # Consider two cases - item is there, item is not there
    '''
    if(test4list.find_unordered(8)):
        print("True!")
    if(test4list.find_unordered(4)):
        print("o no !")
    '''
    alt_List = LinkedList(0)
    alt_List.insert_first(L5)
    alt_List.insert_first(L7)
    alt_List.insert_first(L2)
    alt_List.insert_first(L10)

    print(alt_List)
    print(alt_List.find_unordered(L5))
    print( alt_List.find_unordered(L6) )
    print()



    # Test method find_ordered() 
    # Consider two cases - item is there, item is not there

    alt_List = LinkedList(0)
    alt_List.insert_first(L5)
    alt_List.insert_first(L4)
    alt_List.insert_first(L2)
    alt_List.insert_first(L1)


    print(alt_List)
    print(alt_List.find_ordered(L5))
    print(alt_List.find_ordered(L4))
    print(alt_List.find_ordered(L3))
    print()


    #print(newList)



    # Test method delete_link()
    # Consider two cases - item is there, item is not there
    print(alt_List)
    print(alt_List.delete_link(L3))
    print(alt_List.delete_link(L2))

    print(alt_List)
    print()
    '''
    delete_link_test_list = test4list
    print(delete_link_test_list)
    print(delete_link_test_list.delete_link(5))
    '''



    # Test method copy_list()
    copied_alt = alt_List.copy_list()
    hello = newList.copy_list()
    print(alt_List)
    print(hello)
    print()
    print(copied_alt)
    print()
    '''
    copy_test_list = (test4list.copy_list())
    print(test4list)
    print(copy_test_list)
    '''

    # Test method reverse_list()

    print()
    print(alt_List)
    print(alt_List.reverse_list())
    print()
    '''
    print(test4list)
    reverse_test_list = (test4list.reverse_list())
    print(reverse_test_list)
    '''

    # Test method sort_list()

    sort_hello = hello.sort_list()
    print(hello)
    print()
    print(sort_hello)
    print()
    '''
    sort_list_test = test4list.sort_list()
    print(test4list)
    print(sort_list_test)
    '''
    

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    La = LinkedList(0)
    La.insert_first(L3)
    La.insert_first(L2)
    La.insert_first(L1)

    print(La.is_sorted())

    print(La)
    print()
    print(newList.is_sorted())
    print(newList)
    print()



    # Test method is_empty()
    print(La.is_empty())
    Le = LinkedList(0)
    print(Le.is_empty())

    '''
    test5link1 = Link(12, None)
    
    test5list = LinkedList(0)
    #test5list.insert_first(test5link1)
    print(test5list.get_num_links())
    if(test5list.is_empty()):
        print("True!")
    else:
        print("False!")
    '''

    # Test method merge_list()
    #merge_La_hello = sort_hello.merge_list( La)

    #print('merge')
    #print(merge_La_hello)
    '''
    test61link3 = Link(3, None)
    test61link2 = Link(4, test61link3)
    test61link1 = Link(5, test61link2)
    test6list1 = LinkedList()
    test6list1.insert_first(test61link3)
    test6list1.insert_first(test61link2)
    test6list1.insert_first(test61link1)

    test62link3 = Link(1, None)
    test62link2 = Link(2, test62link3)
    test62link1 = Link(6, test62link2)
    test6list2 = LinkedList()
    test6list2.insert_first(test62link3)
    test6list2.insert_first(test62link2)
    test6list2.insert_first(test62link1)

    print(test6list1)
    print(test6list2)
    merge_list_test = test6list1.merge_list(test6list2)
    print(merge_list_test)
    '''
    
    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    print()

    print(newList.is_equal(La))


    '''
    test71link3 = Link(8, None)
    test71link2 = Link(12, test71link3)
    test71link1 = Link(4, test71link2)
    test7list1 = LinkedList()
    test7list1.insert_first(test71link3)
    test7list1.insert_first(test71link2)
    test7list1.insert_first(test71link1)

    test72link3 = Link(8, None)
    test72link2 = Link(12, test72link3)
    test72link1 = Link(4, test72link2)
    test7list2 = LinkedList()
    test7list2.insert_first(test71link3)
    test7list2.insert_first(test71link2)
    test7list2.insert_first(test71link1)

    if(test7list1.is_equal(test7list2)):
        print("True!")
    else:
        print("False!")
    '''

    # Test remove_duplicates()
    print('rem')
    #print(newList)
    print(newList.remove_duplicates())
    '''
    test8link5 = Link(8, None)
    test8link4 = Link(8, test8link5)
    test8link3 = Link(12, test8link4)
    test8link2 = Link(12, test8link3)
    test8link1 = Link(4, test8link2)

    test8list = LinkedList()
    test8list.insert_first(test8link5)
    test8list.insert_first(test8link4)
    test8list.insert_first(test8link3)
    test8list.insert_first(test8link2)
    test8list.insert_first(test8link1)
    print(test8list)
    test8list.remove_duplicates()
    print(test8list)
    '''

if __name__ == "__main__":
    main()
