''' 
	题目是：
	给定 nums = [2, 7, 11, 15], target = 9

	因为 nums[0] + nums[1] = 2 + 7 = 9
	所以返回 [0, 1]

	思路：暴力法
	由于是很短的数列，可以尝试用暴力解法，
	循环判断target-nums[i]的值是否存在在数组中，
	如果存在那么就把两个编号放在一个新的列表中返回去

	坑：
	写的时候没有注意x的范围，从第一个开始循环会导致两次循环的结果为[0,0,1]。
    要注意第二次循环是从i之后开始的。一旦找到两个数字就要跳出循环，不要再往后寻找

'''
def twoSum(nums, target):
	dic = []
	for i in range(0,len(nums)):
		temp = target-nums[i]
		if temp in nums[i+1:]:
			dic.append(i)
			for x in range(i+1,len(nums)):
				if nums[x] == temp:
					dic.append(x)
					break
			return dic

nums = [3, 3]
target = 6
print(twoSum(nums,target))

