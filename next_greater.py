"""
This question is asked by Amazon. Given two arrays of numbers, where the first array is a subset of the second array, return an array containing all the next greater elements for each element in the first array, in the second array. If there is no greater element for any element, output -1 for that number.

Ex: Given the following arrays…

nums1 = [4,1,2], nums2 = [1,3,4,2], return [-1, 3, -1] because no element in nums2 is greater than 4, 3 is the first number in nums2 greater than 1, and no element in nums2 is greater than 2.
nums1 = [2,4], nums2 = [1,2,3,4], return [3, -1] because 3 is the first greater element that occurs in nums2 after 2 and no element is greater than 4.
"""

nums1 = [1,2,3,4]
nums2 = [2,4]

def next_greater_element(n1, n2):
	if len(n1) < len(n2):
		smaller, bigger = n1, n2 
	else:
		smaller, bigger = n2, n1

	out = []
	for ele in smaller:
		right_list = bigger[bigger.index(ele)+1:]
		next_gt_ele = next((x for x in right_list if x > ele), -1)
		out.append(next_gt_ele)
	return out

print(next_greater_element(nums1, nums2))
