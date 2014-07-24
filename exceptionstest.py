#!/usr/bin/env python

from exceptions import BaseException

def throws():
	    raise RuntimeError('this is the error message')

def fun2(x):
	print "---"
	print x
	print "---"
	
	if x == 5 or x == 8:
		raise BaseException("Piatka lub Osemka")
	try:   
		#y = fun2(3)
		try:
			y = fun2(8)
		except:
			print x
			print "Inner try"
			raise
                else:
			val = 8
			print 
			print val
			return val
		finally:
			print "Clenup inner"
		
	except:
		print x
		print "Outer try"
		raise
	else:
		val = x + 5
		print val 
		return val
	finally:
		print "Cleanup"
'''
def fun(x):
	print "---"
	print x
	print "---"
	
	if x == 5 or x == 8:
		raise BaseException("Piatka lub Osemka")
	try:   
		y = fun(5)
	except:
		print x
		print "1111111111"
		try:

			y = fun(8)
		except:
			print x
			print "222222222"
			raise
                else:
			val = 8
			print val
			return val
		finally:
			print "Clenup inner"

	else:
		val = x + 5
		print val 
		return val
	finally:
		print "Cleanup"
'''
def main():
	print "++++++++++++++"
	try:
		fun2(0)
	except:
		print "END"


if __name__ == '__main__':
	main()

