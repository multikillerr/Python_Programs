import re
NameAge="""
            Janice is 22 and Theon is 33
            Gabriel is 44 and Joey is 21
            """
ages=re.findall(r'\d{1,3}',NameAge)
names=re.findall(r'[A-Z][a-z]*',NameAge)
print ages
print names
