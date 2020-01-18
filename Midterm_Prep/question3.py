"""
Given a list of words stored in the variable List_words, output the longest word and the length of the longest
word (assume that there will be only 1 word of the longest length). Output may look like:
The longest word ‘champions’ has 9 characters.
"""

# Assuming this list is given to the program, 
# but I'm writing it out for demo purposes:
list_words = ["word1", "word2", "word", "word3", "word4", "word5", "longestword"]
#								  ^ This is the smallest word

longestWord = "" # String to hold the longest word
lenLongest = 0 # The length of the longest word
for word in list_words: # Iterate by $word through the list $list_words
	if len(word) > lenLongest: # If the length of the the current word $word is longer than $lenLongest
		longestWord = word # Make the new longestWord the current word $word
		lenLongest = len(word) # Make the new lenLongest the length of the current word $word

# Print the answer
print("The longest word '" + longestWord + "' has " + str(lenLongest) + " characters")