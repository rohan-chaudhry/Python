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

####################################################

class Node (object):
    # constructor
    def __init__ (self, data):
        self.data = data
        self.l_child = None
        self.r_child = None

    # string representation
    def __str__ (self):
        return str(self.data)

class Tree (object):
    # the init function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__ (self, encrypt_str):
        self.root = None

        self.estr = encrypt_str
        self.estr = self.estr.lower()
        fixed_string = ''
        for i in range (len(self.estr)):
            if ('a' <= self.estr[i] and self.estr[i] <= 'z') or (self.estr[i] == ' '):
                fixed_string += self.estr[i]
        self.estr = fixed_string

        for i in range (len(self.estr)):
            self.insert(self.estr[i])

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert (self, ch):
        new_node = Node (ch)
        if (self.root == None):
            self.root = new_node
            return
        current = self.root
        parent = self.root
        while (current != None):
            if (current == new_node):
                break
            parent = current
            if (ch < current.data):
                current = current.l_child
            else:
                current = current.r_child
        if (current == new_node):
            pass
        elif (ch < parent.data):
            parent.l_child = new_node
        else:
            parent.r_child = new_node

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search (self, ch):
        if (ch == self.root.data):
            return '*'
        output_string = ''
        current = self.root
        while (current != None) and (current.data != ch):
            if (ch < current.data):
                output_string += '<'
                current = current.l_child
            else:
                output_string += '>'
                current = current.r_child
        if (current == None):
            return ''
        return output_string

    # the traverse() function will take a string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse (self, st):
        current = self.root
        if (st == '*'):
            return current.data
        for character in st:
            if (character == '<'):
                current = current.l_child
            if (character == '>'):
                current = current.r_child
        return current.data

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt (self, st):
        output_string = '' # encrypted string
        st = st.lower() # convert the input string to lowercase
        for character in st:
            output_string += self.search(character) + '!'
        output_string = output_string[:len(output_string) - 1]
        return output_string

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt (self, st):
        output_string = ''
        direction_list = st.split('!')
        for direction in direction_list:
            output_string += self.traverse(direction)
        return output_string

def main():
    print(" ")
    encryption_key = input('Enter encryption key: ')
    cipher_tree = Tree (encryption_key)
    print(" ")
    string_to_encrypt = input('Enter string to be encrypted: ')
    encrypted_string = cipher_tree.encrypt(string_to_encrypt)
    print('Encrypted string: ' + str(encrypted_string))
    print(" ")
    string_to_decrypt = input('Enter string to be decrypted: ')
    decrypted_string = cipher_tree.decrypt(string_to_decrypt)
    print('Decrypted string: ' + str(decrypted_string))
    print(" ")
main()
            
