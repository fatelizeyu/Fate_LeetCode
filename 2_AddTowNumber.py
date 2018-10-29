'''
	题目：两数相加
	给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
	你可以假设除了数字 0 之外，这两个数字都不会以零开头。	 

	思路：首先将l1, l2两个非空链表转换为普通数字，相加后再转为链表
		  要先判断一次numsum是否为0，否则while循环会跳过numsum为0的情况

'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_number(l):
	num = 0
	t = 1
	while l != None:
		l.val = l.next

def addTowNumber(l1, l2):
	

