'''
	题目：有效的括号
	给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
	有效字符串需满足：
		左括号必须用相同类型的右括号闭合。
		左括号必须以正确的顺序闭合。
		（注意空字符串可被认为是有效字符串。）

	思路：简单的匹配,主要想的东西就是怎么样能更好的匹配。
		  这里我是先将情况都放到列表里面，将字符串中的符号和情况列表来比，
		  然后在结果列表中处理。

'''

def isValid(s):
	
	dic = {'[':']', '{':'}', '(':')'}

	stack = []
	# 判断空字符串为有效字符串
	if not s:
		return True

	for i in s:
		if i in dic:
			stack.append(i)	# 将前括号全部压入栈内
		else:
			if not stack:	# 如果栈内为空，没有前括号
				return False
			elif dic[stack.pop()] != i:
				return False	# 如果栈定和下一个不符合，则顺序不对
	# 字符串括号为单数，有没有对齐的
	if stack:
		return False
	else:
		return True



res = isValid("([)]")
print(res)
