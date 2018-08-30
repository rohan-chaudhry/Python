# File: Boxes.py

# Description: This file will attempt to determine the largest subset of nested boxes, given an original set of n-number three-dimensional boxes.

# Student Name: Daniel Snyder

# Student UT EID: djs3928

# Partner Name: Rohan Chaudry

# Partner UT EID: rc43755 

# Course Name: CS 313E

# Unique Number: 51335

# Date Created: 02/20/18

# Date Last Modified: 02/24/18

##################

def does_fit (box1, box2):
    return ((box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2]))

def subsets (a, b, all_subsets, lo):
    hi = len(a)
    if (lo == hi):
        all_subsets.append(b)
        return
    else:
        c = b[:]
        b.append (a[lo])
        subsets (a, b, all_subsets, lo+1)
        subsets (a, c, all_subsets, lo+1)

def main():
    #print ("Largest Subset of Nesting Boxes")
    # open file for reading
    in_file = open("boxes.txt", "r")

    # read the number of boxes
    line = in_file.readline()
    line = line.strip()
    num_boxes = int(line)

    # create an empty list of boxes
    box_list = []

    # read the list of boxes from the file
    for i in range (num_boxes):
        line = in_file.readline()
        line = line.strip()
        box = line.split()
        for i in range (len(box)):
            box[i] = int(box[i])
        box.sort()
        box_list.append(box)

    # close the file
    in_file.close()

    # sort the box list
    box_list.sort()
    #print(box_list)

    # get all subsets of boxes
    subset = []
    all_subsets = []
    subsets (box_list, subset, all_subsets, 0)
    #print(all_subsets)

    # check if all the boxes in a given subset fit
    nested_subsets_only = []
    for subset in all_subsets:
        all_boxes_nest = True
        for i in range(len(subset)-1):
            if (does_fit(subset[i], subset[i+1])):
                pass
            else:
                all_boxes_nest = False
                break
        if (all_boxes_nest):
                nested_subsets_only.append(subset)
        else:
            pass
                
    # keep track of it (ie. produce a list of all subsets that 'fit')
    #print (nested_subsets_only)

    # print all the largest subsets of boxes
    largest_subsets = []
    length_of_largest_subsets = 0
    for subset in nested_subsets_only:
        subset_length = len(subset)
        if (subset_length > length_of_largest_subsets):
            largest_subsets = []
            length_of_largest_subsets = subset_length
            largest_subsets.append(subset)
        elif (subset_length == length_of_largest_subsets):
            largest_subsets.append(subset)
        else:
            pass
    if (len(largest_subsets) == 0):
        print("No Nesting Boxes")
    else:
        print("Largest Subset of Nesting Boxes")
        for subset in largest_subsets:
            for box in subset:
                print (box)
            print(" ")

main()
        
