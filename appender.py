ten_things="Apples Oranges Crows Telephone Light Sugar"
stuff=ten_things.split(" ")
more_stuff_line="Day Night Song Frisbee Corn"
more_stuff=more_stuff_line.split(' ')
while len(stuff)!=10:
    next_one=more_stuff.pop()
    print "Adding: ",next_one
    stuff.append(next_one)
    print "There are %d items in stuff now"% len(stuff)
print "There we go ",stuff
print "Let's do something to the stuff"
print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])
