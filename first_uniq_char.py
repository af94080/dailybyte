'''This question is asked by Microsoft. Given a string, return the index of its first unique character. If a unique character does not exist, return -1.

Ex: Given the following strings...

"abcabd", return 2
"thedailybyte", return 1
"developer", return 0
'''

s = 'developer'

# print(s.count('i'))

def first_uniq_char(s):
	for idx, char in enumerate(s):
		if s.count(char) == 1:
			return(idx, char)

# print(first_uniq_char(s))

# my variation : try second uniq char

d = {idx: char for idx, char in enumerate(s) \
	if s.count(char) == 1}

print(list(d.items())[1])






