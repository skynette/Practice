'''
Understanding the logging module
'''

import logging
logging.basicConfig(filename="log.txt", level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y 

ad=add(2,3)
logging.debug("answer is %f\n" %ad)

sb=subtract(4,5)
logging.debug("answer is %f\n" %sb)

m=multiply(8,3)
logging.debug("answer is %f\n" %m)

d=divide(100,3)
logging.debug("answer is %f\n" %d)
