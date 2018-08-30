#  File: Josephus.py

#  Description: A11

#  Student Name: Rohan Chaudhry

#  Student UT EID: rc43755

#  Partner Name: Daniel Snyder

#  Partner UT EID: djs3928

#  Course Name: CS 313E

#  Unique Number:  51335

#  Date Last Modified:

###################################

'''
read josephus.txt for 1- num soldiers, 2- starting soldier, 3- elimination number (n)
use circular linked list

'''


##################################
class Link(object):
    def __init__ (self, data):
        self.data = data
        self.next = None

    def to_string(self):
        return str(self.data)

    def has_next(self):
        if self.next is None:
            return False
        else:
            return True

    def __str__(self):
        return str(self.data)


class CircularList(object):
  # Constructor
  def __init__ ( self ):
      self.head = None

  # Insert an element (value) in the list
  # inserts at the "beginning"
  def insert ( self, item ):
      Link_1 = Link(item)
      temp = self.head

      Link_1.next = self.head

      if self.head is not None: # update the next of each link
          while(temp.next != self.head):
              temp = temp.next
          temp.next = Link_1
      else:
          Link_1.next = Link_1

      self.head = Link_1



  # Find the link with the given key (value)
  def find ( self, key ):
      return

  # Delete a link with a given key (value)
  def delete ( self, key ):
      return

  # Delete the nth link starting from the Link start
  # Return the next link from the deleted Link
  def delete_after ( self, start, n ):
      return

  # Return a string representation of a Circular List
  def __str__ ( self ):

      temp = self.head

      if self.head is not None:
          while(True):
              print(str(temp.data), end= ' ')
              #print (str((temp.data)))
              #print(type(temp.data),end=' ')
              temp = temp.next

              if temp == self.head :
                  break

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
      '''




def main():
    C_List = CircularList()
    L1 = 'A'
    L2 = 'B'
    L3 = 'C'


    C_List.insert(L1)
    C_List.insert(L2)
    C_List.insert(L3)
    print(C_List)


main()