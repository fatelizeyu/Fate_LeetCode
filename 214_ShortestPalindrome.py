


def shortestPalindrome(s):
	
	temp = s[::-1]
	for x in range(len(s)):
		if temp[x] == s[0]:
			break;

	flag = temp[:x]
	return flag+s


ss = shortestPalindrome("aacecaaa")
print(ss)