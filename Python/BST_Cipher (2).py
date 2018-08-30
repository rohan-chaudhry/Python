# File: BST_Cipher.py

# Description: This file will attempt to create a simple encryption and decryption scheme using a binary search tree.

#  Student Name: Rohan Chaudhry

#  Student UT EID: rc43755

#  Partner Name: Daniel Snyder

#  Partner UT EID: djs3928

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 04/17/18

#  Date Last Modified: 04/20/18
######################################

class Node (object):
  def __init__ (self, data):
    self.rchild = None
    self.lchild = None
    self.data = data


class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encryptkey):
    self.rootnode = None
    for i in encryptkey:
      self.insert(i)

  def duplicate(self, character):
    currentnode = self.rootnode
    while (currentnode != None) and (currentnode.data != character):
      if character < currentnode.data:
        currentnode = currentnode.lchild
      else:
        currentnode = currentnode.rchild
    return currentnode

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
    if ch == " " or ch.isalpha():
      insertnode = Node(ch)
      if self.rootnode == None:
        self.rootnode = insertnode
      else:
        if not self.duplicate(ch):
          parentnode = self.rootnode
          currentnode = self.rootnode
          while currentnode != None:
            parentnode =  currentnode
            if ch < currentnode.data:
              currentnode = currentnode.lchild
            else:
              currentnode = currentnode.rchild
          if ch < parentnode.data:
            parentnode.lchild = insertnode
          else:
            parentnode.rchild = insertnode

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
    if not self.duplicate(ch):
      return ""
    else:
      currentnode = self.rootnode
      if ch == currentnode.data:
        return "*"
      else:
        returnstr = ""
        while (currentnode != None) and (currentnode.data != ch):
          if ch < currentnode.data:
            currentnode = currentnode.lchild
            returnstr += "<"
          else:
            currentnode = currentnode.rchild
            returnstr += ">"
        return returnstr



  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
    currentnode = self.rootnode
    if st == "*":
      return self.rootnode.data
    for i in st:
      if currentnode != None:
        if i == "<":
          currentnode = currentnode.lchild
        elif i == ">":
          currentnode = currentnode.rchild
      else:
        return ""
    return currentnode.data



  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
    findstr = ""
    st = st.lower()
    for i in st:
      if (i == " ") or i.isalpha():
        findstr += i
    returnstr = ""
    for i in findstr:
      encryptterm = self.search(i)
      returnstr += encryptterm + "!"

    return returnstr[0:-1]

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    newstr = ""
    for i in st:
      if i == "<" or i == ">" or i == "!" or i == "*":
        newstr += i
    list1 = newstr.split('!')
    returnstr = ""
    for i in list1:
      returnstr += self.traverse(i)
    return returnstr


def main():

    ################################################################################## likely corrected
  key = input("Enter encryption key: ")
  key = key.lower()
  treeforkey = Tree(key)
  print()


  encryptstring = input("Enter string to be encrypted: ")
  encryptstring = treeforkey.encrypt(encryptstring)
  print("Encrypted string:", encryptstring)
  print()
  

  decryptstring = input("Enter string to be decrypted: ")
  decryptstring = treeforkey.decrypt(decryptstring)
  print("Decrypted string:", decryptstring)

main()