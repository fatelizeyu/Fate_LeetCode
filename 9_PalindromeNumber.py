'''
	问题：
		判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

	思路：
		这个和第7道题没有什么不同，非常简单就不说了
'''

def isPalindrome(x):

	if str(x) == str(x)[::-1]:
		return True
	else:
		return False


x = -121
print(isPalindrome(x))

