/* 
	题目描述：
	给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

	有效字符串需满足：

	左括号必须用相同类型的右括号闭合。
	左括号必须以正确的顺序闭合。
	注意空字符串可被认为是有效字符串。

	示例 1:

	输入: "()"
	输出: true
	
	示例 2:

	输入: "()[]{}"
	输出: true

	示例 3:

	输入: "(]"
	输出: false
	
	示例 4:

	输入: "([)]"
	输出: false
	
	示例 5:

	输入: "{[]}"
	输出: true

	解题思路：
	首先这道题目的要求是配对的顺序和类型要是对的，即当前遍历到的右括号必须要与最近的左括号类型相同。
	并且需要左括号和右括号的每个类型的数量要一样，看到这个样的特性，可以想到用Stack的特性来解决这个问题，
	左边的括号就直接压入Stack中，右边的括号就要和Stack中的第一个就行匹配如果可以配对就出栈。同时还得注意数量也要相对应。
	最后如果Stack是空的即验证成功

*/

import java.util.*;
class ValidParenthese{


	public boolean isValid(String s){
		
		Stack<Integer> stack = new Stack<>();
		char in[] = s.toCharArray();
		for (char c : in ) {
			if (c == '(') {
				stack.push(0);
			}else if (c == '[') {
				stack.push(1);
			}else if (c == '{') {
				stack.push(2);
			}else if (stack.isEmpty()) {
				return false;
			}else if (c == ')' && stack.pop()!=0) {
				return false;
			}else if (c == ']' && stack.pop()!=1) {
				return false;
			}else if (c == '}' && stack.pop()!=2) {
				return false;
			}

		}
			return stack.isEmpty();

	}

	public static void main(String[] args) {
		
		ValidParenthese v = new ValidParenthese();
		System.out.println(v.isValid("{}{}()"));
	}


}