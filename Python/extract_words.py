# A Python script extract_words.py, which will generate three .txt files:
# allwords.txt, uniquewords.txt and wordfrequency.txt

# open novel file and generate a list containing ALL words in novel, including duplicates
# convert to lower case, remove non-alphabetic characters (no punctuation, no digits)

# findall --> a-z+ pattern, extract only characters

# allwords.txt == every word in the novel, lower case, no punctuation
# includes duplicates, each word on its own line

# unique words == every words that appears only once
# if occurance == 1, add to unique word list
# use a defaultdict; key is word, value is number ofoccurences

# wordfrequency == number of occurences for a given word
# FORMAT-   frequency: number of words with that frequency


# assumes that the book is clean, and that the txt file begins and ends with the proper novel
# as such, this implies that sections like the table of contents have been deleted


########################################################

word_dict = {} # global dictionary variable
def create_word_dict(): # creates a reference dictionary
    infile = open("words.txt", "r")
    for line in infile: # populate
        line = line.strip()
        word_dict[line] = "1"

    infile.close() # close

# Removes punctuation marks from a string
def parseString(st):
    # assumes that all strings eventually end with a period or some sort of punctuation

    s = "" # no space
    i = 0 # serves as index counter
    while (i < len(st)):
        if i == len(st) - 1:
            s += ""
            break
        # adds letters and spaces
        if (st[i].isalpha() or st[i].isspace()): #check if alphabetic char or a space
            s += st[i]
            i += 1
        # apostrophe cases
        elif st[i] == "'":
            # if apostrophe followed by a non 's' letter, include the apostraphe in word
            # essentially, contractions are treated as one word
            if (st[i + 1].isalpha() and st[i + 1] != "s"):
                s += st[i]
                i += 1
            # if apostrophe followed by a space, remove the apostraphe
            elif st[i + 1].isspace():
                i += 1
            # if apostrophe followed by an 's', remove apostraphe
            # possessives are treated as one word, the 's' is also dropped since it's redundant
            elif st[i + 1] == 's':
                i += 2
        # if character is not a letter or an apostrophe or space, remove punctuation
        else:
            s += " " #blank space
            i += 1

    return s


# Returns a dictionary of words and their frequencies
def getWordFreq(file):
####################
# Create all words

    word_freq_dict = {} #empty dictionary
    # read the book file and find each word
    infile = open(file, "r", encoding="utf8")
    allwords = open("allwords.txt", "w")
    for line in infile:
        line.strip()
        line = parseString(line)
        line = line.split()
        # create a count for each word in the book
        for word in line:
            word = word.lower()
            # increment count if word already present in word_freq_dict
            if word in word_freq_dict:
                word_freq_dict[word] = word_freq_dict[word] + 1
                allwords.write(word + '\n')

            # start count if word doesn't exist in word_freq_dict
            else:
                word_freq_dict[word] = 1
                allwords.write(word + '\n')
    infile.close()
    allwords.close()  # every single word used in the novel


#################

    #  create uniquewords.txt
    uniquewords = open("uniquewords.txt", "w")
    for word,freq in word_freq_dict.items(): # key is the word, value is occurence
        if freq == 1:
            uniquewords.write(word + '\n')
    uniquewords.close()

###############

    # create wordfrequency.txt -- map frequency to number of words with that frequency
    # FORMAT: freq: number of words with that freq
    wordfreq_out = open("wordfrequency.txt", "w")

    word_list = list(word_freq_dict.items())
    sorted_word_list = sorted(word_list)

    freq_val = 1
    num_words = 0

    limit = len(sorted_word_list)

    for i in range (limit):
        for item in sorted_word_list:

            if item[1] == freq_val:
                num_words += 1
                if item == sorted_word_list[-1]: #
                    wordfreq_out.write(str(freq_val) + ': ' + str(num_words) + '\n')

            elif item == sorted_word_list[-1]:
                if num_words > 0:
                    wordfreq_out.write(str(freq_val) + ': ' + str(num_words) + '\n')

            else:
                continue

        num_words = 0
        freq_val += 1

    wordfreq_out.close()
############
    # get just the top 10 frequencies and words
    top10_words = sorted(((value,key) for (key,value) in word_freq_dict.items()), reverse=True)
    top10_out = open("top_10_words.txt", "w")

    for i in range(10) :
        top10_out.write(str(top10_words[i][0]) + '\n' + str(top10_words[i][1] + '\n'))
    top10_out.close()

    return (word_freq_dict) #not alphabetized

#######################

def main():
    book1 = input("Enter name of first book: ")
    getWordFreq(book1)
    print('\ndone') #this will let you know when to check the .txt files

main()
