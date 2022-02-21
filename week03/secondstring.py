#user to enter sentence

Sentence = str(input("enter a sentence: "))

#make input backwards and only evey second letter
text = str(Sentence) [::-1] [::2]
print(text)