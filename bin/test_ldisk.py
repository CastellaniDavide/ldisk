"""Test ldisk file
"""
from ldisk import *

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2020-10-23"

def test():
	"""Tests the ldisk function in the ldisk class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert ldisk.ldisk() == "ldisk", "test failed"
	#assert ldisk.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
