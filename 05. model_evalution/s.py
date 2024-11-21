def find_longest_word(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Find the longest word using the max() function with the key as length of the word
    longest_word = max(words, key=len)

    return longest_word

# Test the function
sentence = "The quick brown fox jumped over the lazy dog"
longest_word = find_longest_word(sentence)
print("The longest word is:", longest_word)
