"""
This question is asked by Google. 
Given a string only containing the following characters 
(, ), {, }, [, and ] 
return whether or not the opening and closing 
characters are in a valid order.

Ex: Given the following strings...

"(){}[]", return true
"(({[]}))", return true
"{(})", return false
"""

s = "(({[]}))"

o, c = [], []

opening = ['(', '{', '[']

closing = [')', '}', ']']

for i, ele in enumerate(s):
	print(f"i: {i} ele: {ele}")
