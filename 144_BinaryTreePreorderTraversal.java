/*
	题目描述：
	给定一个二叉树，返回它的 前序 遍历。

	示例:
	输入: [1,null,2,3]  
		1
		 \
		  2
		 /
		3 
	输出: [1,2,3]
	进阶: 递归算法很简单，你可以通过迭代算法完成吗？

	解题思路：	
	先根遍历二叉树，就是说，对二叉树中的每一个节点，先访问该节点，再访问其左子树，最后访问其右子树。用迭代的方式先根遍历二叉树，需要借助栈。具体步骤如下： 
	（1）将根结点入栈 
	（2）进入循环。先弹出栈顶元素，访问它，然后将该元素的右子树入栈，最后将该元素的左子树入栈。左子树后于右子树入栈保证了左子树先于右子树被访问。

 */

import java.util.*;


public class BinaryTreePreorderTraversal{

	public List<Integer> preorderTraversal(TreeNode root){

		List<Integer> result = new LinkedList<Integer>();
		if (root == null) {
			return result;
		}

		LinkedList<TreeNode> stack = new LinkedList<TreeNode>();
		stack.push(root);
		while(!stack.isEmpty()){
			TreeNode top = stack.pop();
			if (top != null) {
				
				result.add(top.value);
				stack.push(top.right);
				stack.push(top.left);
			}
		}

		return result;
	}

	public static void main(String[] args) {

		TreeNode root = new TreeNode(1);
		TreeNode l = new TreeNode(2);
		TreeNode r = new TreeNode(3);
		root.right = l;
		l.left = r;
		BinaryTreePreorderTraversal b = new BinaryTreePreorderTraversal();
		System.out.println(b.preorderTraversal(root));
	}
}


class TreeNode{

	public int value;
	public TreeNode left;
	public TreeNode right;

	public TreeNode(int x){
		value = x;
	}

}





