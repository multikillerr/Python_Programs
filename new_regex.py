import re
str="Sat,hat,mat,pat"
allstr=re.findall("[h-z]at",str)
for i in allstr:
    print i
