'''
	��Ŀ����������ת����
	˼·��1 �Ƚ���Ҫע���һ�����ڣ�
	     ʵ����ֻ������һ��С�������ڴ���ǰ��������ڶ���������
	     ��IIV���������ǲ����ܳ��ֵģ���ͻ᷽��ܶ��ˡ�

	     2 ���Խ� 4 = IV = -I+V = -1 + 5������ֻҪ�������� a[i+1] > a[i]ʱ�� a[i]ȡ����˳��Ӽ��ɡ� 
		 ֵ��ע����ǣ��Ƚϴ�Сʱ ��Ϊi+1Ҫ�����鷶Χ�ڣ����ڼ����ʱ�ټ������һλ�� 
		 ����sumʱҪ����a[-1]Ҳ�������һλ��


'''


	
def romenToInt(s):
	# ����������Ͷ�Ӧ��ֵ��Ϊ�ֵ�
	dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	# Ϊ�˷���ѭ�����ַ�����������
	s = s[::-1]
	# ����һ������������Ϊ�����ʼֵ����Ϊ���һ�������Ǽ���ȥ�Ĳ��Ǽ�ȥ��
	num = dic[s[0]]
    # ����һ���������ֶ�Ӧ��������Ϊ��¼
	temp = dic[s[0]]

	# �ӵڶ�����ʼѭ��
	for c in s[1:]:
		if dic[c] < temp:
			num -= dic[c]  # ���ø���temp
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




