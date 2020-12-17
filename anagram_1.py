'''This question is asked by Facebook. 
Given two strings s and t 
return whether or not s is an anagram of t.
Note: An anagram is a word formed by 
reordering the letters of another word.

Ex: Given the following strings...

s = "cat", t = "tac", return true
s = "listen", t = "silent", return true
s = "program", t = "function", return false'''

def is_anagram(s1, s2):
	return sorted(s1) == sorted(s2)

s = 'program'
t = 'function'

print(is_anagram(s, t))


