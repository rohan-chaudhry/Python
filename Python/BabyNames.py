#  File: BabyNames.py

#  Description: A9

#  Student's Name: Rohan Chaudhry

#  Student's UT EID: rc43755

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: March 19

#  Date Last Modified: 24 march

###################################################################################
#######

# following the outline given on assignment page
import urllib.request  # the lib that handles the url stuff


# create empty dictionary to hold baby names, open TXT, read line and store data
def make_dict():
    baby_name_dict = {} # empty dict to hold names
    test_dict = {}

    # open file
    count = 0
    try:
        data = urllib.request.urlopen('http://cs.utexas.edu/~mitra/csSpring2018/cs313/assgn/names.txt')  # it's a file like object and works just like a file

    except:
        print("Data file cannot be found")

    for line in data:  # files are iterable
        line = str(line, encoding='utf8')
        name_data = line.split()
        name_numbers_str = name_data[1:]

        # convert counts to int, still a list
        name_numbers_int = list(map(int,name_numbers_str))

        test_dict[name_data[0]] = name_numbers_int

        name = name_data[0]

        count += 1

    return(test_dict)

#######################################################
# return true if name exists in dict, false otherwise
def ret_true(name):
    make_dict()
    return name in make_dict()

#######################################################
# return all rankings of a given name
def ret_ranks(name):
    dict = make_dict()

    if name in dict:
        return (dict[name])
    else:
        return(str(name) + ' does not appear in any decade')


#######################################################
# return list of names that have a rank in all the decades in sorted order by name

# if each entry in the value list is greater than 0, add the name key to a new list, then return that new list

def dec_names():
    dict = make_dict()
    names = [ ]
    for k,v in dict.items():
        if 0 not in v:
            names.append(k)


    return names

#######################################################
# display ALL the names that have a rank in a given decade in order of rank
# rank 1 is highest, 999 is lowest

# 0 decade is the leftmost one, 10 is the rightmost
def dec_ranks(decade):
    dict = make_dict()
    name_num = [ ]
    names = [ ]

    for k,v in dict.items():
        if v[decade] > 0:
            name_num.append([v[decade],k])
            name_num.sort()
    count = 0
    for i in name_num:
        sort_name = name_num[count][1]
        names.append(sort_name)
        count += 1

    #names.sort()
    return names

#######################################################
# display all names getting more popular every decade
# names must have a rank in all the decades to qualify
# sort output by name

def inc_pop():
    dict = make_dict()
    every_decade = [ ]
    names_every_decade = [ ]

    for k,v in dict.items(): #find names popular in each decade, make a new array
        if 0 not in v:
            if v == sorted(v):
                every_decade.append([k,v])
    count = 0
    for i in every_decade:
        names_every_decade.append(every_decade[count][0])
        count += 1

    return names_every_decade

#######################################################
# display all names getting more popular every decade
# names must have a rank in all the decades to qualify
# sort output by name

def dec_pop():
    dict = make_dict()
    every_decade = [ ]
    names_every_decade = [ ]

    for k,v in dict.items(): #find names popular in each decade, make a new array
        if 0 not in v:
            if v == sorted(v, reverse=True):
                every_decade.append([k,v])
    count = 0
    for i in every_decade:
        names_every_decade.append(every_decade[count][0])
        count += 1

    return names_every_decade

#######################################################
# return highest ranking decade of a name
def highest_rank(name):

    m = min(i for i in ret_ranks(name) if i > 0)
    idx = ret_ranks(name).index(m)
    decade = 10
    start = 1900
    max_dec = start + decade*idx

    return str(max_dec)

#######################################################
def main():
    # choice, if == 1 - 6, run specific step, else: quit

    choice = eval(input("Options:\nEnter 1 to search for names.\nEnter 2 to display data for one name\nEnter 3 to all names that appear in only one decade.\nEnter 4 to all names that appear in all decades.\nEnter 5 to all names that are more popular in every decade.\nEnter 6 to all names that are less popular in every decade.\nEnter 7 to quit.\n\nEnter choice: "))
    # assume correct input


    while( choice > 0 ):

        if choice == 1: # search for a name
            name = str(input("Enter a name: "))
            if ret_true(name) == True:
                print("\nThe matches with their highest ranking decade are:")
                high_rank_name = highest_rank(name)
                print(name + ' ' + high_rank_name)
                print()

            else:
                print('\n'+str(name)+ ' does not appear in any decade.')
                print()


        elif choice == 2: #display data for one name
            name = str(input("Enter a name: "))
            if ret_true(name) == True:
                ranks = ret_ranks(name)
                name_rank = ''
                idx = 0
                for val in ranks:
                    name_rank+= str(ranks[idx]) + ' '
                    idx += 1
                print('\n' + str(name)+ ': ' + str(name_rank)  )
                print(name)


                dec = 1900
                count = 0
                for decade in range(11):
                    print(str(dec + count) + ': ' + str(ranks[count//10]))
                    count += 10

                print()
            # create a FOR loop, from 1900 to 2000
            # show the rank of that decade
            else:
                print('\n' + str(name) + ' does not appear in any decade.')
                print()


        elif choice == 3: # display all names that appear in one decade
            decade = int(input("Enter a decade: "))

            if (decade>=1900) and (decade<=2000):
                print('The names are in order of rank: ')
                name_ranks = make_dict()
                ordered_ranks = [ ]

                for k,v in name_ranks.items():
                    name = str(k)
                    rank = v[(decade%100)//10]
                    if rank == 0:
                        rank = 1000

                    ordered_ranks.append([name,rank])
                    ordered_ranks = sorted(ordered_ranks,key=lambda x:x[1], reverse=False)

                for entry in ordered_ranks:
                    print(entry[0] + ': ' + str(entry[1]))

            else:
                print('not in range')

            print()

        elif choice == 4: # display all names that appear in ALL decades
            all_decade = dec_names()
            print(str(len(all_decade)) + ' names appear in every decade. The names are:')
            for name in all_decade:
                print(name)

            print()

        elif choice == 5: # ALL names that are popular in every decade
            popular = inc_pop()
            print(str(len(popular)) + ' names are more popular in every decade.')
            for name in popular:
                print(name)

            print()

        elif choice == 6: # ALL names that are less popular in every decade
            lame = dec_pop()
            print(str(len(lame)) + ' name are less popular in every decade.')
            for name in lame:
                print(name)
            print()

        elif (choice > 6):
            print("Goodbye")
            break

        choice = eval(input("Options:\nEnter 1 to search for names.\nEnter 2 to display data for one name\nEnter 3 to all names that appear in only one decade.\nEnter 4 to all names that appear in all decades.\nEnter 5 to all names that are more popular in every decade.\nEnter 6 to all names that are less popular in every decade.\nEnter 7 to quit.\n\nEnter choice: "))


main()






'''
    if choice == 1: # search for a name
        name = str(input("Enter a name: "))
        if ret_true(name) == True:
            print("\nThe matches with their highest ranking decade are:")
            high_rank_name = highest_rank(name)
            print(name + ' ' + high_rank_name)

        else:
            print('\n'+str(name)+ ' does not appear in any decade.')


    elif choice == 2: #display data for one name
        name = str(input("Enter a name: "))
        if ret_true(name) == True:
            ranks = ret_ranks(name)
            name_rank = ''
            idx = 0
            for val in ranks:
                name_rank+= str(ranks[idx]) + ' '
                idx += 1
            print('\n' + str(name)+ ': ' + str(name_rank)  )
            print(name)


            dec = 1900
            count = 0
            for decade in range(11):
                print(str(dec + count) + ': ' + str(ranks[count//10]))
                count += 10


            # create a FOR loop, from 1900 to 2000
            # show the rank of that decade
        else:
            print('\n' + str(name) + ' does not appear in any decade.')


    elif choice == 3: # display all names that appear in one decade
        decade = int(input("Enter a decade: "))

        if (decade>=1900) and (decade<=2000):
            print('The names are in order of rank: ')
            name_ranks = make_dict()
            ordered_ranks = [ ]

            for k,v in name_ranks.items():
                name = str(k)
                rank = v[(decade%100)//10]
                if rank == 0:
                    rank = 1000

                ordered_ranks.append([name,rank])
                ordered_ranks = sorted(ordered_ranks,key=lambda x:x[1], reverse=False)

            for entry in ordered_ranks:
                print(entry[0] + ': ' + str(entry[1]))

        else:
            print('not in range')
        print()

    elif choice == 4: # display all names that appear in ALL decades
        all_decade = dec_names()
        print(str(len(all_decade)) + ' names appear in every decade. The names are:')
        for name in all_decade:
            print(name)

        print()

    elif choice == 5: # ALL names that are popular in every decade
        popular = inc_pop()
        print(str(len(popular)) + ' names are more popular in every decade.')
        for name in popular:
            print(name)

        print()

    elif choice == 6: # ALL names that are less popular in every decade
        lame = dec_pop()
        print(str(len(lame)) + ' name are less popular in every decade.')
        for name in lame:
            print(name)

        print()

    else: #if input is 7 or anything else, quit
        print("Goodbye.")
'''










