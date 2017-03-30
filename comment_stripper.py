

#The problem I was presented as a kata from codewars.com:
#solved in python 2.7

#Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
#Any whitespace at the end of the line should also be stripped out.
#
#Example:
#
#iven an input string of:
#
#apples, pears # and bananas
#grapes
#bananas !apples
#The output expected would be:
#
#apples, pears
#grapes
#bananas


def solution(string,markers):
	newString = ''
	flag = 0
	for i in string:
		if i in ''.join(markers):
			newString = newString.rstrip(" ")
			flag = 1
		elif i == '\n':
			newString = newString.rstrip(" ")
			flag = 0
		if flag == 0:
			newString += i
	return newString


		