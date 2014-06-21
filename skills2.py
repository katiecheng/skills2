string = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]


def count_unique(string1):
    """
    Write a function that takes a string and produces a dictionary with
    all distinct elements as the keys, and the number of each element as
    the value
    Bonus: do the same for a file (i.e. twain.txt)
    """
    if type(iterable1) == str:
        new_list = iterable1.split() # split string on spaces to make list
    elif type(iterable1) == list:
        new_list = iterable1 
    count_dict = {} # initialize dict
    for item in new_list: # for item in list:
        if item in count_dict: # if in dictionary:
            count_dict[item] += 1 # increment value
        else: # else:
            count_dict[item] = 1 # set item =1
    return count_dict # return count_dict

def common_items(list1, list2):
    """
    Given two lists, (without using the keyword 'in' or the method 'index')
    return a list of all common items shared between both lists
    """
    common_list = [] 
    unique_common_list = [] # SHOULD HAVE USED SET!
    for item1 in list1:
        for item2 in list2: # compare each item in list1 to each item in list2
            if item1 == item2: # if the items are equal, append to common_list
                common_list.append(item1) # common_list may have duplicates
    for index in range(len(common_list)): # so, for each item in common_list
        already_in_list = False
        for another_index in range(len(unique_common_list)):
            if common_list[index] == unique_common_list[another_index]:
                already_in_list = True # check if it's already in unique list
        if not already_in_list: # if not, then append it to unique_common_list
            unique_common_list.append(common_list[index])
    return unique_common_list # return unique_common_list


def common_items2(list1, list2):
    """
    Given two lists, (without using the keyword 'in' or the method 'index')
    return a list of all common items shared between both lists. This time,
    use a dictionary as part of your solution.
    """
    # put each list in a count dictionary
    list1_count_dict = count_unique(list1) # dict1 of word:count
    list2_count_dict = count_unique(list2) # dict2 of word:count
    common_list = []
    for key1 in list1_count_dict.keys():
        for key2 in list2_count_dict.keys():
            if key1 == key2: # compare the keys   
                common_list.append(key1)
    return common_list

def sum_zero(list1):
    """
    Given a list of numbers, return list of number pairs that sum to zero
    """
    # in this prob, I just used dictionaries to store unique values
    # I still used lists to check if number pairs sum to zero
    unique_dict = {}
    pair_list = [] # initialize an empty pair_list

    # populate unique_dict with unique numbers in a list
    for item in list1:
        if item not in unique_dict:
            unique_dict[item] = True # add to dict

    keys_list = unique_dict.keys()

    for num1 in keys_list: # for each num1 in dict
        num1_index = keys_list.index(num1)
        other_list = keys_list[num1_index+1:]
        for num2 in other_list: # for every other num2 in dict
            if num1 + num2 == 0:
                pair_list.append((num1, num2)) # append a tuple to the pair_list

    return pair_list


def find_duplicates(words):
    """
    Given a list of words, return a list of words with duplicates removed
    """
    unique_dict = {}
    # put each word in dict as a key, and value as whatever (here, True)
    for item in words:
        if item not in unique_dict:
            unique_dict[item] = True # add to dict
    
    return unique_dict.keys()


def word_length(words):
    """
    Given a list of words, print the words in ascending order of length
    Bonus: do it on a file instead of the list provided
    Bonus: print the words in alphabetical order in ascending order of length
    """
    length_dict = {}
    unique_words = find_duplicates(words)
    # make a dictionary where length is the key
    # value is a list of words of that length
    for word in unique_words:
        length = len(word) # for each word, check len of word
        if length in length_dict: # if dict has length_key
            length_dict[length].append(word) # append word to value list
        else:
            length_dict[length] = [word] # else, create length_key = [word]
    
    # after populating the dict, for each key, sort value list alphabetically
    for key in length_dict:
        length_dict[key] = sorted(length_dict[key], key=str.lower)

    sorted_keys = sorted(length_dict.keys()) # make a list of sorted keys
    for key in sorted_keys: # for key in sorted_keys
        for word in length_dict[key]:
            print word # print each item in the value list

"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey
"""

pirate_dict = {
    'sir':'matey', 
    'hotel':'fleabag inn', 
    'student':'swabbie', 
    'boy':'matey', 
    'madam':'proud beauty', 
    'professor':'foul blaggart', 
    'restaurant':'galley', 
    'your':'yer', 
    'excuse':'arr', 
    'students':'swabbies', 
    'are':'be', 
    'lawyer':'foul blaggart', 
    'the':'th\'', 
    'restroom':'head', 
    'my':'me', 
    'hello':'avast', 
    'is':'be', 
    'man':'matey'
    }

def pirateize(string):
    """
    Write a program that asks the user to type in a sentence and then
    print the sentece translated to pirate.
    """
    # DOESN'T DEAL WITH PUNCTUATION
    new_list = string.split()
    pirate_string = ''
    for word in new_list:
        if word in pirate_dict:
            if pirate_string == '':
                pirate_string += pirate_dict[word]
            else:
                pirate_string += ' ' + pirate_dict[word]
        else:
            pirate_string += ' ' + word
    return pirate_string

