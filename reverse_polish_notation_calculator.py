

#The problem I was presented as a kata from codewars.com:
#solved in python 2.7

#Your job is to create a calculator which evaluates expressions in Reverse Polish notation.
#
#For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.
#
#Note that for simplicity you may assume that there are always spaces between numbers and operations, e.g. 1 3 + expression is valid, but 1 3+ isn't.
#
#Empty expression should evaluate to 0.
#
#Valid operations are +, -, *, /.
#
#You may assume that there won't be exceptional situations (like stack underflow or division by zero).


def calc(expr):
	if len(expr) is 0:
		return 0
	else:
		stack = []
		sub = ''
		for i in expr + " ":
			if i != " ":
				sub += i
			elif is_number(sub):
				stack.append(float(sub))
				sub = ''
			elif sub == '+':
				a = stack.pop()
				b = stack.pop()
				stack.append(b+a)
				sub = ''
			elif sub == '-':
				a = stack.pop()
				b = stack.pop()
				stack.append(b-a)
				sub = ''
			elif sub == '*':
				a = stack.pop()
				b = stack.pop()
				stack.append(b*a)
				sub = ''
			elif sub == '/':
				a = stack.pop()
				b = stack.pop()
				stack.append(b/a)
				sub = ''
		return stack.pop()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False



		