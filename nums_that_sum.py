'''
[1, 3, 8, 2], k = 10, return true (8 + 2)
[3, 9, 13, 7], k = 8, return false
[4, 2, 6, 5, 2], k = 4, return true (2 + 2)
'''

l = [3, 9, 13, 7]
k = 8

def nums_match_tot(a, b, tot):
	return a + b == tot


for idx, val in enumerate(l):
	for v2 in l[idx+1:]:
		print(val, v2)
		if nums_match_tot(val, v2, k):
			print(val, v2)

'''their sol is to use a hashmap
Instead of doing a linear scan to find a number 
to complement our current number, 
we can introduce a hash map 
to remember what numbers we have seen. 
Now for each number, we can ask the question, 
“have we seen a number that when added 
to our current number 
will give us a sum of k?” 

If we have, we can return true, 
and if we haven’t can simply 
add our current number to our hash map 
to remember for the future. 
Following below is the solution described here

public boolean twoSum(int[] nums, int k) {
    HashMap map = new HashMap();
    for(int i = 0; i return false;

}
'''