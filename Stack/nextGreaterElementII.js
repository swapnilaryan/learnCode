/*
 Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

 Example 1:
 Input: [1,2,1]
 Output: [2,-1,2]
 Explanation: The first 1's next greater number is 2;
 The number 2 can't find next greater number;
 The second 1's next greater number needs to search circularly, which is also 2.
 Note: The length of given array won't exceed 10000.
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var nextGreaterElements = function(nums) {
	var nextGreaterElementsArray = [];

	if(!nums){
		return nextGreaterElementsArray;
	}else if(nums && nums.length===0){
		return nextGreaterElementsArray;
	}

	for(var i = 0; i<nums.length;i++){
		nextGreaterElementsArray.push(-1);
	}

	var stack = [];

	for(i=0;i<2 * nums.length - 1;i++){
		stack.push((i)%nums.length);
		while(stack.length && nums[stack[stack.length - 1]] < nums[(i + 1)%nums.length]){
			nextGreaterElementsArray[(stack.pop())%nums.length] = nums[(i + 1)%nums.length];
		}
	}

	return nextGreaterElementsArray;

};

arr1 = [1,2, 1];
arr2 = [5,4,3,2,1];
arr3 = [5,4,6,2,1];
console.log(nextGreaterElements(arr1));
console.log(nextGreaterElements(arr2));
console.log(nextGreaterElements(arr3));
