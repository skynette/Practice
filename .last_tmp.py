import sys

# understanding command line arguments
# by making a simple file searcher

# checks for a minimum of 3 command arguments

if len(sys.argv) < 3:
	sys.stderr.write("E: Usage " + sys.argv[0] + " <filename> <words>")
	sys.stderr.flush()
	exit(2)

else:
	filename = sys.argv[1]
	needle = sys.argv[2]

counter = 0

# opens a file in read mode
file_handler = open(filename)
for line in file_handler.readlines():	# read the lines in the file
	
	# seperate the words in each line on the space and save into a list sentence
	sentences = line.split(" ")			

	for word in sentences:				# go through the words in a sentence
		if word == sentences[-1]:		# take the last word
			word = word[:-1]			# eliminate the new line character
		if word == needle:				# find the needle
			counter += 1				# record the occurence

print (str(counter) + " times " + needle + " appears")