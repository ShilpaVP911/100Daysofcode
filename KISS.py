text=input("Please enter some text: ")
count=0
word_count=len(text.split())
print("Number of words:", word_count)
for word in text.split():
    if len(word) > word_count:
        count=count+1


if count > 0:
    print("Some words are longer than the total number of words.")
else:
    print("All words are within the limit.")