'''
	题目：罗马数组转整型
	思路：1 比较需要注意的一点在于，
	     实际上只可能有一个小数出现在大数前而不会存在多个的情况。
	     如IIV这种数字是不可能出现的，这就会方便很多了。

	     2 可以将 4 = IV = -I+V = -1 + 5，所以只要将数组中 a[i+1] > a[i]时的 a[i]取反按顺序加即可。 
		 值得注意的是，比较大小时 因为i+1要在数组范围内，故在计算合时少加了最后一位。 
		 计算sum时要加上a[-1]也就是最后一位。


'''


	
def romenToInt(s):
	# 将罗马数组和对应数值作为字典
	dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	# 为了方便循环将字符串倒序排列
	s = s[::-1]
	# 将第一个罗马数字作为结果初始值，因为最后一个数字是加上去的不是减去的
	num = dic[s[0]]
    # 将第一个罗马数字对应的整数作为记录
	temp = dic[s[0]]

	# 从第二个开始循环
	for c in s[1:]:
		if dic[c] < temp:
			num -= dic[c]  # 不用更新temp
		else:
			num += dic[c]
			temp = dic[c]
	return num
	
def romenToInt2(s):
	dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	num_list = []
	num = 0
	for i in range(len(s)-1):
		if dic[s[i]] < dic[s[i+1]] :
			num = -dic[s[i]]
			num_list.append(int(num))
		else:
			num_list.append(int(dic[s[i]]))
	return sum(num_list)+dic[s[-1]]

res = romenToInt2("III")
print(res)




