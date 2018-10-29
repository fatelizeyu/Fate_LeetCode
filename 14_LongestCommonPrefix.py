'''
	题目：寻找最长前缀
		 编写一个函数来查找字符串数组中的最长公共前缀。
		 如果不存在公共前缀，返回空字符串 ""。

    思路：就是比较，首先肯定要跟最短的比，所以先找到最短的字符串。
         其次，有很多特殊情况要先考虑，比如数组为空返回空，列表中存在空，
    	 那么一定没有共同前缀也返回空，列表中只有一个字符串，那么返回其自身。
'''

def longestCommonPrefix(s):

	# 如果数组为空或者数组中有空，肯定没有共同前缀
	if '' in s or s == []:
		return ''
	elif len(s) == 1:
		return s[0]  # 如果长度为1，那么最长的就是数组里的
	else:
		min_lens = min(len(x) for x in s) # 寻找最短字符串。简洁的写法！！！！
		flag = 0
		# 两个两个循环，只比较最短的字符长度，查找最长相同前缀
		while flag < min_lens:
			for i in range(len(s)-1):
				if s[i][flag] != s[i-1][flag] :
					return s[0][:flag]
			flag += 1	
		
		return s[0][:flag]


str = ["dog","racecar","car"]
res = longestCommonPrefix(str)
print(res)


	