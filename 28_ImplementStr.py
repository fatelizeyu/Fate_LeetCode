'''
	题目：实现strStr()
	给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
'''


def strStr(haystack, needle):
	if not needle:
		return 0
	else:
		if needle in haystack:
			for i in range(len(haystack)):
				if haystack[i:i+len(needle)] == needle:
					return i
		else:
			return -1


res = strStr('hello', 'll')
print(res)
