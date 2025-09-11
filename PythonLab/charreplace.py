word="onion"
first=word[0]
rest=word[1:].replace(first,"$")
new_word=first+rest
print(new_word)