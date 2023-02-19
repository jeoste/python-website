sentence = 'New year new style'
print(len(sentence))

sentence_encoded = sentence.encode()
print(sentence_encoded)

sentence_upper = sentence.upper()
print(sentence_upper)

sentence_lower = sentence.lower()
print(sentence_lower)

# give the beginning of the occurrence found
sentence_find = sentence.find('e')
print(sentence_find)

sentence_replace = sentence.replace('style', 'me')
print(sentence_replace)

# return boolean value to check if exist or not. Case sensitive
sentence_exist = 'New' in sentence
print(sentence_exist)

# put uppercase on every words
sentence_title = sentence.title()
print(sentence_title)
