num_of_sentences=int(input("Enter number of sentences: "))
word_count_dict={}
for i in range(num_of_sentences):
    sentence=input("Enter sentence {}: ".format(i+1))
    words=sentence.split()
    for word in words:
        word=word.lower().strip('.,!?;"\'()[]{}')  # Normalize the word
        if word:
            if word in word_count_dict:
                word_count_dict[word]+=1
            else:
                word_count_dict[word]=1
print("Word Count Dictionary:")
for word, count in word_count_dict.items():
    print("'{}': {}".format(word, count))
