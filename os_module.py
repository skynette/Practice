'''
Understanding the OS module
'''

import os
import sys
import subprocess

# functions used with os
os.getcwd()								# current working dir
os.path.abspath('')						# absolute path, empty string means current working directory
os.path.abspath('..')					# relative path
os.listdir()							# listdir

# making directories
os.mkdir('bla')
os.makedirs('bla', 'sub-bla')			# im not so sure about this one

# deleting directories
os.rmdir("specific_dir")
os.removedirs("remove_tree")

# listing directories
os.walk()
# example
for dirpath, dirnames, filenames in os.walk('/Users/Konstantine/Desktop'):
	print ('current path: ', dirpath)
	print ('Directories: ', dirnames)
	print ('Files: ', filenames)
	print ()

os.chdir ('/Users/Konstantine/Desktop')

print(os.path.exists('/tmp/test.txt'))
print(os.path.isdir('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.dbaseame('/tmp/test.txt'))

# running shell commands from python scripts
os.system()
os.popen()


# subprocess.call() can be used in place of os.system() when some parameters are passed
subprocess.call('python helloshell.py')				# roughly like os.system()
subprocess.call('cmd /C "type helloshell.py"')		# built-in shell cmd
subprocess.call('type helloshell.py', shell=True) # alternative for built-ins
pipe = subprocess.Popen('python helloshell.py', stdout=subprocess.PIPE)



from subprocess import Popen, PIPE
Popen('python helloshell.py', stdout=PIPE).communicate()[0]
# b'The Meaning of Life\r\n'

import os
os.popen('python helloshell.py').read()
# 'The Meaning of Life\n'

# startfile
os.startfile("webpage.html") 		# open file in your web browser
os.startfile("document.doc") 		# open file in Microsoft Word
os.startfile("myscript.py") 		# run file with Python


# other os MOdule exports

os.environ()
# Fetches and sets shell environment variables

os.fork()
# Spawns a new child process on Unix-like systems

os.pipe()
# Communicates between programs

os.execlp()
# Starts new programs

os.spawnv()
# Starts new programs with lower-level control

os.open()
# Opens a low-level descriptor-based file

os.mkfifo()
# Creates a new named pipe

os.stat()
# Fetches low-level file information