import argparse

# i wanna turn this into a gp calculator

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("first", help="first number", type=float)
parser.add_argument("second", help="second number", type=float)
parser.add_argument("-o", "--output", help="output to a file", action="store_true")
parser.add_argument("operation", help="operation to carry out on numbers")

args = parser.parse_args()

num1 = args.first
num2 = args.second
result=None

if args.operation == "add":
    result = num1 + num2
elif args.operation == "subtract":
    result = num1 - num2
elif args.operation == "multiply":
    result = num1 * num2

if args.output:
    f = open("fib.txt", "a")
    f.write(str(result) + "\n")
    
if args.verbose:
    print("first number: " + str(args.first))
    print("second number: " + str(args.second))
    print("selected operation: " + str(args.operation))
    print ("result is " + str(result))

elif args.quiet:
    print (result)
else:
    print ("result is " + str(result))
