'''
	问题：给定一个 32 位有符号整数，将整数中的数字进行反转。

	思路：弹出和推入数字 & 溢出前进行检查
		这个题非常简单主要是用取余运算和整除运算就可以获得，只要依次遍历就可以
		完成对这个数字的翻转。

	坑：python语法中的/是会对数字进行除法运算的，如果除不尽会有小数
		判断条件有点多，主要是对翻转后数字大小判断和对传入参数正负号判断
		代码太过麻烦，应该要简洁点
'''

def reverse(x):
	flag = 0
	dic = []
	sign = False
	result = 0

	if x == 0:
		return 0

	if x < 0:
		sign = True
		x = -x

	while x > 0:
		temp = x%10
		if temp == 0 and flag == 0:
			x = x//10
			continue
		dic.append(temp)
		x = x//10
		flag += 1

	for i in range(0,len(dic)):
		flag -= 1
		result += dic[i]*(10**flag)
	
	if sign:
		result = -result

	if result < -2**31 or result > 2**31-1:
		return 0
	return result	


'''
	优化方案：
	巧妙的构思，python中的语法确实简洁。
	[::-1]的意思是将字符串从列表结束位置到开始位置按照-1的进度打印一遍
	类似与[-1:-len(a)-1:-1]
'''

def reverse2(x):
	flag = 1
	if x < 0:flag = -1;x = -x
	# 将传入参数按照字符串反转输出并转换为int型
	result = int(str(x)[::-1]) 
	if result < -2**31 or result > 2**31-1:
		result = 0
	return result*flag
		



x = -123
print(reverse2(x))

