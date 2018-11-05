/*

 	题目描述：
	给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
	说明：本题中，我们将空字符串定义为有效的回文串。
	示例 1:

	输入: "A man, a plan, a canal: Panama"
	输出: true
	示例 2:

	输入: "race a car"
	输出: false

	解题思路：
	设置两个指针，一个在字符串头部，一个在字符串尾部，分别向中间移动，
	遇到非字母或数字则继续向中间移动，如两个都为字母或者数字，那么则比较两者是否相同。

 */

class ValidPalindrome{

	/*
	超时是什么鬼？
	 public boolean isPalindrome(String s){

		int i = 0;
		int j = s.length()-1;
		char head,tail;

		if (j < 0) {
			return true;
		}

		while(i < j){
			head = s.charAt(i);
			tail = s.charAt(j);
			if (!Character.isLetterOrDigit(head)) {
				i++;
			}
			if (!Character.isLetterOrDigit(tail)) {
				j--;
			}
			if(Character.isLetterOrDigit(head) && Character.isLetterOrDigit(tail)){
				if (Character.toLowerCase(head) != Character.toLowerCase(tail)) {
					return false;
				}
				i++;
				j--;
			}
		}
		return true;
	}
	*/

	 public boolean isPalindrome(String s){

		 if(s==null||s.length()<2){
    	   return true;
       }
       int p2=s.length()-1;
       char c1,c2;
       for(int i=0;i<s.length()-1;i++){
    	   if(!isvalid(s.charAt(i))){
    		   continue;
    	   }
    	   c1=s.charAt(i);
    	   while(p2>=0&&!isvalid(s.charAt(p2))){
    		   p2--;
    	   }
    	   c2=s.charAt(p2);
    	   if(!issame(c1,c2)) return false;
    	   else p2--;
       }
       return true;

	}

	private static boolean isvalid(char c){
		if(c>='a'&&c<='z'||c>='A'&&c<='Z'||c>='0'&&c<='9')
			return true;
		else
			return false;
	}
	private static boolean issame(char a,char b){
		if(a<65||b<65){
			if(a==b) return true;
			else	return false;
		}else{
			if(a==b||Math.abs(a-b)==32)	return true;
			else return false;
		}
	}

	public static void main(String[] args) {
		
		ValidPalindrome v = new ValidPalindrome();
		System.out.println(v.isPalindrome("A man, a plan, a canal: Panama"));
	}
}