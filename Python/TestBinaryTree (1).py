# File: TestBinaryTree.py

# Description: This assignment extends the Node and Tree classes to include functions like is_similar, get_height, and num_nodes of a Binary Search Tree.

#  Student Name: Rohan Chaudhry

#  Student UT EID: rc43755

#  Partner Name: Daniel Snyder

#  Partner UT EID: djs3928

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 04/13/18

#  Date Last Modified: 04/15/18




### CORRECTED USING LIST INPUT

####################################################

class Node (object):
  def __init__(self, data):
    self.rchild = None
    self.lchild = None
    self.data = data

class Tree (object):
  def __init__(self):
    self.rootnode = None

  #Searches tree to find and return node
  def search(self, key):
    current = self.rootnode
    while (current != None) and (current.data != key):
      if key < current.data :
        current = current.lchild
      else:
        current = current.rchild
    return current

  #inserts nodes into the tree based on comparison to left child/right child values
  def insert (self, data):
    insertednode = Node(data)
    if (self.rootnode == None):
      self.rootnode = insertednode
    else:
      parent = self.rootnode
      current = self.rootnode
      while (current != None):
        parent = current
        if (data < current.data):
          current = current.lchild
        else:
          current = current.rchild
      if (data < parent.data):
        parent.lchild = insertednode
      else:
        parent.rchild = insertednode

  def in_order (self, aNode):
    if (aNode != None):
      self.in_order (aNode.lchild)
      print(aNode.data)
      self.in_order(aNode.rchild)

  #Preorder function
  def pre_order (self, aNode):
    if (aNode != None):
      print(aNode.data)
      self.pre_order(aNode.lchild)
      self.pre_order(aNode.rchild)
  #Postorder function
  def post_order (self, aNode):
    if (aNode != None):
      print(aNode.data)
      self.post_order(aNode.lchild)
      self.post_order(aNode.rchild)
  def min_node(self):
    current = self.rootnode
    if current == None:
      return None
    while current.lchild != None:
      current = current.lchild
    return current

  def max_node(self):
    current = self.rootnode
    return current

  #deletes a node and its respective value from the tree
  def delete (self, key):
    delete_node = self.rootnode
    parent = self.rootnode
    is_left = False

    if (delete_node == None):
      return None

    while (delete_node != None) and (delete_node.data != key):
      parent = delete_node
      if key < delete_node.data:
        delete_node = delete_node.lchild
      else:
        delete_node = delete_node.rchild
        is_left = False

    if (delete_node == None):
      return None

    if (delete_node.lchild == None) and (delete_node.rchild == None):
      if (delete_node == self.rootnode):
        self.rootnode = None
      elif (is_left):
        parent.lchild = None
      else:
        parent.rchild = None

    elif (delete_node.rchild == None):
      if (delete_node == self.root):
        self.rootnode = delete_node.lchild
      elif (is_left):
        parent.lchild = delete_node.lchild
      else:
        parent.rchild = delete_node.lchild

    else:
      successor = delete_node.rchild
      successor_parent = delete_node

      while (successor.lchild != None):
        successor_parent = successor
        successor = successor.lchild

      if (delete_node == self.rootnode):
        self.rootnode = successor
      elif (is_left):
        parent.lchild = successor
      else:
        parent.rchild = successor

      successor.lchild = delete_node.lchild

      if successor != delete_node.rchild:
        successor_parent.lchild = successor.rchild
        successor.rchild = delete_node.rchild
      return delete_node

  #Recursive function - Checks to see if the content of one is the same as the content of the other 
  def isSimilar (self, rootnode1, rootnode2):
    current1 = rootnode1
    current2 = rootnode2
    if current1 == None and current2 == None:
      return True
    else:
      if current1 != None and current2 != None:
        return (current1.data == current2.data) and self.isSimilar(rootnode1.lchild, rootnode2.lchild) and self.isSimilar(rootnode1.rchild, rootnode2.rchild)

    return False

  #prints the content of each levele of the tree
  def print_level(self, level, branch, ct):
    newbranch = []
    if ct < level:
      for i in branch:
        if i.lchild:
          newbranch.append(i.lchild)
        if i.rchild:
          newbranch.append(i.rchild)
      self.print_level(level, newbranch, ct + 1)
    if ct == level:
      for i in branch:
        print(i.data)
      return True

  def get_height(self, rootnode1):
    current = rootnode1
    if current == None:
      return 0

    lheight = self.get_height(rootnode1.lchild)
    rheight = self.get_height(rootnode1.rchild)
    if (lheight > rheight):
      return lheight + 1
    else:
      return rheight + 1

  def num_nodes2(self, rootnode1):
    current = rootnode1
    if current == None:
      return 0
    else:
      return self.num_nodes2(rootnode1.lchild) + 1 + self.num_nodes2(rootnode1.rchild)

  #returns list of nodes
  def num_nodes(self, rootnode1):
    current = rootnode1
    if current == None:
      return 0
    else:
      a = []
      a.append(self.num_nodes2(rootnode1.lchild))
      a.append(self.num_nodes2(rootnode1.rchild))
      return a

  def numbranch (self, height, branch, ct):
    if ct < height:
      for i in branch:
        if i.lchild:
          branch.append(i.lchild)
        if i.rchild:
          branch.append(i.lchild)
        if i.rchild:
          branch.append(i.rchild)
      self.numbranch(height, branch, ct +1)
    if count == height:
      length = len(branch)
      print("countBranch =", length )
      return (int(length))

def main():
  # Create three trees - two are the same and the third is different
  '''
  tree1 = Tree()
  list1 = [50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 96]
  for i in list1:
    tree1.insert(int(i))
  tree2 = tree1
  
  tree3 = Tree()
  list2 = [20,14,76,84,12,32,54,23,12,65]
  for i in list2:
    tree3.insert(int(i))
  '''

  # use test cases

  tree1 = Tree()
  list1 = [14]
  for i in list1:
    tree1.insert(int(i))
  tree2 = Tree()
  list2 = [78, 100, 77, 46, 31, 77, 97, 64, 69, 75]
  for i in list2:
    tree2.insert(int(i))

  tree3 = Tree()
  list3 =  [94, 50, 64, 87, 99, 84, 54, 93, 80, 76, 90, 60, 95, 17, 38, 72, 15,
50, 55, 34, 15, 22, 100, 26, 36, 40, 28, 83, 11, 63, 17, 52, 67, 73, 52, 78, 45,
94, 30, 40, 8, 95, 25, 37, 23, 4, 73, 86, 49, 29, 8, 45, 95, 70, 30, 15, 70, 35,
58, 87, 67, 7, 40, 9, 87, 58, 64, 81, 83, 45, 80, 81, 55, 10, 39, 27, 24, 21, 62,
16, 89, 26, 57, 13, 73, 5, 54, 52, 36, 60, 15, 27, 80, 80, 30, 97, 33, 13, 5, 29]
  for i in list3:
    tree3.insert(int(i))





  # Test your method is_similar()

  print("\nTest is_similar() :")
  print("Tree 1:", list1)
  print("Tree 2:", list1)
  print("Tree 3:", list2)
  print()
  print("T/F: Tree 1 is similar to Tree 2:", tree1.isSimilar(tree1.rootnode, tree2.rootnode))
  print("T/F: Tree 1 is similar to Tree 3:", tree1.isSimilar(tree1.rootnode, tree3.rootnode))

  # Print the various levels of two of the trees that are different

  print("\nTest print_level() on Tree 1 :")
  tree1_rootnode = [tree1.rootnode]
  for i in range(1,5):
    if i == 1:
      print("Level", i, "includes Node:")
    else:
      print("Level", i, "includes Nodes: ")
    tree1.print_level(i,tree1_rootnode,1)
  print()
  print("Test print_level() on Tree 3:")
  tree3_rootnode = [tree3.rootnode]
  for i in range(1,6):
    if i == 1 or i == 5:
      print("Level", i, "includes Node:")
    else:
      print("Level", i, "includes Nodes:")
    tree3.print_level(i,tree3_rootnode,1)


  # Get the height of the two trees that are different
  print("\nTest get_height() :")
  print("Tree 1 Height: ", tree1.get_height(tree1.rootnode))
  print("Tree 3 Height: ", tree3.get_height(tree3.rootnode))

  # Get the total number of nodes a binary search tree
  print("\nNumber of nodes in Tree 1:", end =" ")
  tree1_rootnode = tree1.rootnode
  numnodes1 = 0
  for i in tree1.num_nodes(tree1_rootnode):
  	numnodes1 += int(i)
  print(numnodes1)
  print()
  tree3_rootnode = tree3.rootnode
  numnodes3 = 0
  for i in tree3.num_nodes(tree3_rootnode):
  	numnodes3 += int(i)
  print("Number of nodes in Tree 3:", end =" ")
  print(numnodes3)


main()











