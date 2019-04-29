import hashlib
import sys
'''
Cracking an MD5 Hash
Since MD5 is a method of encryption and is publicly available, it is possible to create a hash
collision by using common methods of cracking hashes. This in turn "cracks" the hash and
returns to you the value of the string before it had been put through the MD5 process. This
is achieved most commonly by a "dictionary" attack. This consists of running a list of words
through the MD5 encoding process and checking whether any of them are a match against
the MD5 hash you are trying to crack. This works because MD5 hashes are always the same if
the same word is hashed.
To start cracking the MD5 hashes, we need to load a file containing a list of words that
will be encrypted in MD5. This will allow us to loop through the hashes and check whether
we have a match:
'''

target = input("Please enter your hash here: ")
dictionary = input("Please enter the file name of your dictionary: ")
def main():
    with open(dictionary) as fileobj:
        for line in fileobj:
            line = line.strip()
            if hashlib.md5(line.encode()).hexdigest() == target:
                # im having trouble printing out the line
                print ("Hash was successfully cracked %s: The value is %s" %(target, line))
                sys.exit(0)
            else:
                print ("Password match not found")
                return ""
    print ("Failed to crack the file.")

if __name__ == "__main__":
    main()