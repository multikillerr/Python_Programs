import ex25
import sys
sentence="This is what I have and here is when I start to hack"
words=[]
words=ex25.break_words(sentence)
for word in words:
    sys.stdout.write(word)
    sys.stdout.write(" ")
    sys.stdout.flush()
print '\n'
