'''
Understanding the re module
'''

import re

'''
\b : word boundary
\B : not a word boundary
\r : carriage return
\t : tab
\v : vertical tab
\d : [0-9]  matches 0 to 9
\D : [^0-9] anything but 0 to 9
\w : [a-zA-Z0-9_] matches a to z upper and lower cases, o to 9 and undescore
\W : [^a-zA-Z0-9_]
\s : [\b\t\n\v] matches spaces
^  : begining of a string
$  : end of a string
[] : character set: matches characters in brackets
'''
# Nameage= '''
# Janie is 22 and Theon is 33
# Gabriel is 44 and Joey is 21
# '''
# ages = re.findall(r'\d{1,3}', Nameage)
# names = re.findall(r'[A-Z][a-z]*', Nameage)

# ageDict = {}
# x=0

# for eachname in names:
#     ageDict[eachname] = ages[x]
#     x+=1

# print(ageDict)

# finding strings
animals = 'rat, dog, mouse, elephant, pat, mat'
# looks for the string at
f_animals = re.findall('[a-zA-z]at', animals)

for anims in f_animals:
    print(anims, '\n')



# replacing strings
owl_food = 'rat cat cat cat mat pat pat'
regex = re.compile('[cr]at')
regex2 = re.compile(r'(\b\w+)\s+\1')    # \1 is back reference
print ('Matches found for back references: ', len(re.findall(regex2, owl_food)))
for i in re.findall(regex2, owl_food):
    print (i)


# sub replaces strings found in the regular expresion
owl_food = regex.sub('owl', owl_food)
print (owl_food, '\n')


# matching single characters like periods
org = 'F.B.I C.I.A M.I.6 MI5'
print ('Matches: ', len(re.findall('.\..\..', org)), '\n')

# matching white spaces
randStr = '''This is a long 
string that goes
on for many lines
'''
print(randStr)
regex = re.compile('\n')
randStr = regex.sub(' ', randStr)
print(randStr, '\n')


randNum = '1234567'
num = '123 1234 12345 123456'
print("Matches: ", len(re.findall('\d', randNum)))
print("Matches: ", len(re.findall('\d{3,5}', num)), '\n')

ph = '234-818-233-6574'


if re.search('\w{3}-\w{3}-\w{4}', ph):
    print (ph, 'is a phone number\n')
else:
    print ("Not a phone number\n")

pattern = re.compile(r'([\d]{3})-([\d]{3}-[\d]{3}-[\d]{4})')
randExp = re.sub(pattern, r'(\1)\2', ph)
print ('Formatted phone number:', randExp, '\n')

Email_list = 'joshua@gmail.com, emmamail.com, emma@.com, me@gmail, yahoo@.com, aiseluck@gmail.com'
for i in re.findall('[\w._%+-]{2,20}@[\w.-]{2,20}\.[a-zA-Z]{2,3}', Email_list):
    c=1
    print (i)
    c+=1
    
print (c, "Matches found!!!\n")

links = 'https://www.youtube.com http://uchess.com https://www.facebook.com http://www.ichess.net'
exp = re.compile(r'(https?://([\w.]+))')
res = re.sub(exp, r"<a href='\1'>\2</a>\n", links)
print (res)