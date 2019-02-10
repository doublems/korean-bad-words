giver  = open("./to_add.md", 'r', encoding = 'UTF8')
taker = open("./korean-bad-words.md", 'a+', encoding = 'UTF8')

words_to_add = set([line.rstrip() for line in giver])
existing_words= set([line.rstrip() for line in taker])

for word_to_add in words_to_add:
    if word_to_add not in existing_words:
        taker.write(word_to_add + '\n')
        print(word_to_add)

giver.close()
taker.close()