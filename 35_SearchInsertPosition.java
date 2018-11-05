/*
	题目描述：
	给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
	你可以假设数组中无重复元素。

	示例 1:
	输入: [1,3,5,6], 5
	输出: 2

	示例 2:
	输入: [1,3,5,6], 2
	输出: 1

	示例 3:
	输入: [1,3,5,6], 7
	输出: 4

	示例 4:
	输入: [1,3,5,6], 0
	输出: 0
	
	解题思路：
	二分查找，当找不到时l=r+1,所以根据最后一次l和r的变动来判定应该插入的位置，如果最后一次是l=mid+1。
	说明应该插入到mid+1的位置，如果最后一次是r=mid-1，则说明应该插入到mid的位置。

 */

class SearchInsertPosition{

	public int searchInsertPosition(int[] nums, int target){
		int l = 0;
		int r = nums.length-1;
		int pos = 0;
		int mid;

		while(l <= r){
			mid = (l+r) >> 1;
			if(target == nums[mid])
				return mid;
			else if (target > nums[mid]) {
				l = mid+1;
				pos = mid+1;
			}else{
				r = mid-1;
				pos = mid;
			}
		}
		return pos;
	}


	public static void main(String[] args) {

		SearchInsertPosition s = new SearchInsertPosition();
		int[] arr = {1,3,5,6};
		int target = 5;
		System.out.println(s.searchInsertPosition(arr,target));
	}
}

