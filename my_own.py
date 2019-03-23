inp=raw_input("Enter the word")
list1=[]
list2=[]
for x in inp:
    w=ord(x)
    list1.append(w)
    list1.sort()
for let in list1:
    letter=chr(let)
    list2.append(letter)
print list1
print list2
