'''
jewels = "abc", stones = "ac", return 2
jewels = "Af", stones = "AaaddfFf", return 3
jewels = "AYOPD", stones = "ayopd", return 0

Given a string representing your stones 
and another string representing a list of jewels, 
return the number of stones that you have 
that are also jewels. 
'''

def jewels_in_stones_v1(jewels, stones):
	nbr_of_jewels = 0
	for char in stones:
		if char in jewels:
			nbr_of_jewels += 1
	return nbr_of_jewels

def jewels_in_stones(jewels, stones):
	return sum(1 for char in stones if char in jewels)


jewels = "Af"
stones = "AaaddfFf"

result = jewels_in_stones(jewels, stones)
print(result)
