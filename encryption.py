'''
Understanding the basics of encryption
and encoding

we will be
[*] Generating an MD5 hash
[*] Generating an SHA 1/128/256 hash
[*] Implementing SHA and MD5 hashes together
[*] Implementing SHA in a real-world scenario
[*] Generating a Bcrypt hash
[*] Cracking an MD5 hash
[*] Encoding with Base64
[*] Encoding with ROT13
[*] Cracking a substitution cipher
[*] Cracking the Atbash cipher
[*] Attacking one-time pad reuse
[*] Predicting a linear congruential generator
[*] Identifying hashes
'''
import hashlib
import uuid
import sys
# i start with the md5 hash, the most commonly used hashes in web application
# message = input('Enter string to be hashed with md5: ')
# md5_hash = hashlib.md5()
# print (md5_hash.hexdigest()+'\n')

# '''
# SHA hashes are also extremely commonly used, alongside MD5 hashes. The early
# implementation of SHA hashes started with SHA1, which is less frequently used now
# due to the weakness of the hash. SHA1 was followed up with SHA128, which was then
# replaced by SHA256.
# '''
# message2 = input('Enter string to be hashed with sha1: ')
# sha1_hash = hashlib.sha1()
# print (sha1_hash.hexdigest()+'\n')

# message3 = input('Enter string to be hashed with sha256: ')
# sha256_hash = hashlib.sha256()
# print (sha256_hash.hexdigest()+'\n')

# message4 = input('Enter string to be hashed with sha512: ')
# sha512_hash = hashlib.sha512()
# print (sha512_hash.hexdigest()+'\n')


# imnplementing in real world scenario
# ''' First import needed libraries
# We then need to define the function that will hash the password. We start by creating a
# salt, using the uuid library. Once the salt has been generated, we use hashlib.sha256
# to string together the salt encode and the password encode and make it readable by using
# hexdigest and finally appending the salt to the end of it:
# '''
# def hash(password):
#     salt = uuid.uuid4().hex
#     return hashlib.sha512(salt.encode() + password.encode()).hexdigest() + ':' + salt

# '''
# Next, we move onto the check password function. This is what is going to confirm our original
# password is the same as the second one to ensure there were no mistakes. This is done by
# using the same method as before:
# '''
# def check(hashed, password2):
#     password, salt = hashed.split(':')
#     return password == hashlib.sha512(salt.encode() + password2.encode()).hexdigest()

# '''
# Once we have created the blocks of code that we need, we can then start asking the user
# for the required input. We start off by asking for the original password and using the hash_
# password function to create the hash. This then gets printed out to the user. After the first
# password has been done, we ask for the password again to ensure there has been no spelling
# mistakes. The check_password function then hashes the password again and compares the
# original to the new one. If they match, the user is informed that the password is correct; if not,
# the user is informed that the passwords do not match:
# '''

# password = input('Please enter a password: ')
# hashed = hash(password)
# print('The string to store in the database is: ' + hashed)
# re = input('Please re-enter your password: ')
# if check(hashed, re):
#     print('Password Match')
# else:
#     print('Password Mismatch')

# Generating a Bcrypt hash
# '''
# One of the less commonly used, yet more secure hash functions, is Bcrypt. Bcrypt hashes
# were designed to be slow when encrypting and decrypting hashes. This design was used to
# prevent hashes from being easily cracked if hashes got leaked to the public, for example
# from a database exposure.
# ensure v0.4 is installed
# '''
# import bcrypt
# # We can then request the input from the user by using the standard input method:
# new = input('Please enter a password: ')

# '''
# After we have the input, we can get down to the nitty gritty hashing methods. To begin with,
# we use the bcrypt.hashpw function to hash the input. We then give it the value of the
# inputted password and then also randomly generate a salt, using bcrypt.gensalt().
# This can be achieved by using:
# '''

# hashed = bcrypt.hashpw(new.encode(), bcrypt.gensalt())

# # We then print the hashed value out to the user, so they can see the hash that has
# # been generated:

# print ('The string about to be stored is: ' + str(hashed))


# # Now, we start the password confirmation. We have to prompt the user for the password
# # again so that we can confirm that they entered it correctly:
# plaintext = input('Please re-enter the password to check: ')
# # Once we have the password, we check whether both passwords match by using
# # the == feature within Python:

# if bcrypt.hashpw(plaintext.encode(), hashed) == hashed:
#     print ("[+] It\'s a match")
# else:
#     print ("[-] Password Mismatch, Please try again")
# '''
# Cracking an MD5 Hash
# Since MD5 is a method of encryption and is publicly available, it is possible to create a hash
# collision by using common methods of cracking hashes. This in turn "cracks" the hash and
# returns to you the value of the string before it had been put through the MD5 process. This
# is achieved most commonly by a "dictionary" attack. This consists of running a list of words
# through the MD5 encoding process and checking whether any of them are a match against
# the MD5 hash you are trying to crack. This works because MD5 hashes are always the same if
# the same word is hashed.
# To start cracking the MD5 hashes, we need to load a file containing a list of words that
# will be encrypted in MD5. This will allow us to loop through the hashes and check whether
# we have a match:
# '''

# target = input("Please enter your hash here: ")
# dictionary = input("Please enter the file name of your dictionary: ")
# def main():
#     with open(dictionary) as fileobj:
#         for line in fileobj:
#             line = line.strip()
#             if hashlib.md5(line.encode()).hexdigest() == target:
#                 # im having trouble printing out the line
#                 print ("Hash was successfully cracked %s: The value is %s" %(target, line))
#                 sys.exit(0)
#             else:
#                 print ("Password match not found")
#                 return ""
#     print ("Failed to crack the file.")

# if __name__ == "__main__":
#     main()

# '''
# Encoding with Base64
# Base64 is an encoding method that is used frequently to this day. It is very easily encoded
# and decoded, which makes it both extremely useful and also dangerous. Base64 is not used
# as commonly anymore to encode sensitive data, but there was a time where it was.
# '''

# i guess it doesnt work with python 3
# msg = input('Please enter the string to encode: ')
# print ("Your B64 encoded string is: " + msg.encode('base64'))
# '''
# Encoding with ROT13
# ROT13 encoding is definitely not the most secure method of encoding anything. Typically,
# ROT13 was used many years ago to hide offensive jokes on forums as a kind of Not Safe For
# Work (NSFW) tag so people wouldn't instantly see the remark. These days, it's mostly used
# within Capture The Flag (CTF) challenges, and you'll find out why.
# '''
# # works with python 2.7
# # from string import maketrans, lowercase, uppercase
# import string

# def rot13(message):
#     lower = str.maketrans(lowercase, lowercase[13:] + lowercase[:13])
#     upper = str.maketrans(uppercase, uppercase[13:] + uppercase[:13])
#     return message.translate(lower).translate(upper)

# message = input('Enter :')
# print (rot13(message))

# '''
# Cracking a substitution cipher
# The following is an example of a real-life scenario that was recently encountered. A substitution
# cipher is when letters are replaced by other letters to form a new, hidden message. During a CTF
# that was hosted by "NullCon" we came across a challenge that looked like a substitution cipher.
# The challenge was:
# Find the key:
#     TaPoGeTaBiGePoHfTmGeYbAtPtHoPoTaAuPtGeAuYbGeBiHoTaTmPtHoTmGePoAuGe
#     ErTaBiHoAuRnTmPbGePoHfTmGeTmRaTaBiPoTmPtHoTmGeAuYbGeTbGeLuTmPtTm
#     PbTbOsGePbTmTaLuPtGeAuYbGeAuPbErTmPbGeTaPtGePtTbPoAtPbTmGeTbPtEr
#     GePoAuGeYbTaPtErGePoHfTmGeHoTbAtBiTmBiGeLuAuRnTmPbPtTaPtLuGePoHf
#     TaBiGeAuPbErTmPbPdGeTbPtErGePoHfTaBiGePbTmYbTmPbBiGeTaPtGeTmTlAt
#     TbOsGeIrTmTbBiAtPbTmGePoAuGePoHfTmGePbTmOsTbPoTaAuPtBiGeAuYbGeIr
#     TbPtGeRhGeBiAuHoTaTbOsGeTbPtErGeHgAuOsTaPoTaHoTbOsGeRhGeTbPtErGe
#     PoAuGePoHfTmGeTmPtPoTaPbTmGeAtPtTaRnTmPbBiTmGeTbBiGeTbGeFrHfAuOs
#     TmPd
# '''
# string = 'TaPoGeTaBiGePoHfTmGeYbAtPtHoPoTaAuPtGeAuYbGeBiHoTaTmPtHoTmGePoAuGeErTaBiHoAuRnTmPbGePoHfTmGeTmRaTaBiPoTmPtHoTmGeAuYbGeTbGeLuTmPtTmPbTbOsGePbTmTaLuPtGeAuYbGeAuPbErTmPbGeTaPtGePtTbPoAtPbTmGeTbPtErGePoAuGeYbTaPtErGePoHfTmGeHoTbAtBiTmBiGeLuAuRnTmPbPtTaPtLuGePoHfTaBiGeAuPbErTmPbPdGeTbPtErGePoHfTaBiGePbTmYbTmPbBiGeTaPtGeTmTlAtTbOsGeIrTmTbBiAtPbTmGePoAuGePoHfTmGePbTmOsTbPoTaAuPtBiGeAuYbGeIrTbPtGeRhGeBiAuHoTaTbOsGeTbPtErGeHgAuOsTaPoTaHoTbOsGeRhGeTbPtErGePoAuGePoHfTmGeTmPtPoTaPbTmGeAtPtTaRnTmPbBiTmGeTbBiGeTbGeFrHfAuOsTmPd'

# # To start this script off, we first defined the key string within the script. The n variable was then
# # defined as 2 for later use and two empty lists were created— list and answer:
# n=2
# list = []
# answer = []
# [list.append(string[i:i+n]) for i in range(0, len(string), n)]
# # print(list)
# print (set(list))

# periodic = {"Pb": 82, "Tl": 81, "Tb": 65, "Ta": 73, "Po": 84, "Ge":
# 32, "Bi": 83, "Hf": 72, "Tm": 69, "Yb": 70, "At": 85, "Pt": 78,
# "Ho": 67, "Au": 79, "Er": 68, "Rn": 86, "Ra": 88, "Lu": 71,
# "Os": 76, "Tl": 81, "Pd": 46, "Rh": 45, "Fr": 87, "Hg": 80,
# "Ir": 77}
# for value in list:
#     # if value in periodic:
#         answer.append(chr(periodic[value]))

# lastanswer = ''.join(answer)
# print (lastanswer)
