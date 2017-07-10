import string


# put your code here.
def word_count(text_file):
    word_count = {}
    poem = open(text_file)
    for line in poem:
        line = line.rstrip()
        split_line = line.split(" ")
        for word in split_line:
            word_count[word] = word_count.get(word, 0) + 1
    for word, count in word_count.iteritems():
        print word, count
        #return word_count

word_count('twain.txt')
punc = string.punctuation
print punc
