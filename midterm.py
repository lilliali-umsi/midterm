# SI 506 Midterm Exam - Practical Question 1

# The function <find_unique_words> should take one argument, <str_list> which is a list of strings.
# Then, the function should implement a nested loop.  The outer loop should iterate over the elements
# of <str_list>, and the inner loop should iterate over the words comprising each element in <str_list>.
# You need to fix the code below so that it executes the following operations successfully:
#
# 1. split each string encountered in the outer loop and return a list of words found in the split string
# 2. for each word in the words list, check if the unique_words list includes the word as an element.
# 3. if the word is not an element of unique_words, append it to the list; if appended previously skip.
# 4. return the unique_words list so that it has no duplicate elements

# After the function is defined, it is called with the <trees> list as a parameter, and its
# output is saved as <unique_tree_words> (we do this for you; you shouldn't change anything below
# the indicated line). <unique_tree_words> is then printed to the terminal.

# The correct terminal output from this code should be:
# ['english', 'yew', 'northern', 'red', 'maple', 'oak', 'sugar']

def find_unique_words(str_list):
    """
       This function takes as an argument a list of strings. It will return a
       list that contains all of the unique words found in the strings in str_list.
    """

    unique_words = []

    # # # # START CODING HERE # # # # # # # # # # # # # # # # # # # # #

    # Write a "for" loop that will loop over each element in <str_list>.
    # You will need to come up with a variable that contains the looped values from <str_list>
    for str in str_list:# <-- Write a "for" statement here.

        # Now, turn each string element into a list of words, using the "split" function.
        # You will need to come up with a new variable name for this list.
        all_trees = str.split(' ')# <-- Write a "split" statement here.

        # Now, write another "for" loop to loop through each word in your list of words.
        # You will need to come up with a variable that contains the looped values.
        for str in all_trees:# <-- Write another "for" statement here.

            # Now, write an "if" statement that will check if each word is already contained
            # within the list <unique_words>. This "if" statement should return True if the
            # word is NOT already contained within the list <unique_words>
            if str not in unique_words:# <-- Write the "if" statement here.

                # Finally, add the word to the list <unique_words>.
                unique_words.append(str)# <-- Write your code here.

    # # # # # STOP CODING HERE # # # # # # # # # # # # # # # # # # # # #
    # Don't change anything below this line!

    return unique_words

# Use the below lines to test your function.

trees = ['english yew','northern red maple','english oak','sugar maple','northern red oak','english maple']
unique_tree_words = find_unique_words(trees)
print(f"unique_tree_words = {unique_tree_words}")
