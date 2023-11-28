# Mehraneh - 30062786
# Session2 - 08/02/2023
# AT2.2 Q1.
# Replace three different commonly misspelled words with the correct spelling within the String
# and print out the String variable contents afterwards. 

# takes input from the user and stores the input inside of a string 
input_phrase = input("Please enter your phrase which contains 3 words peeple, acheeve and risult:")

# replace misspelled word "peeple" with the correct spell of the "people"
input_phrase = input_phrase.replace("peeple", "people")

# replace misspelled word "acheeve" with the correct spell of the "achieve"
input_phrase = input_phrase.replace("acheeve", "achieve")

# replace misspelled word "risult" with the correct spell of the "result"
input_phrase = input_phrase.replace("risult", "result")

# print out the String variable contents   
print(input_phrase) 
