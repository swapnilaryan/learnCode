/**
 Next Greater Element
 Given an array, print the Next Greater Element (NGE) for every element.
 The Next greater Element for an element x is the first greater element on the right side of x in array.
 Elements for which no greater element exist, consider next greater element as -1.
 * @param {number[]} nums
 * @return {number[]}
 * Use stack to store only the values for which we don't have the NGE.
 */

var nextGreaterElements = function(nums) {
	var nextGreaterElementsArray = [];

	if(!nums){
		return nextGreaterElementsArray;
	}else if(nums && nums.length===0){
		return nextGreaterElementsArray;
	}

	for(var i =0; i<nums.length;i++){
		nextGreaterElementsArray.push(-1);
	}

	var stack = [];

	// for(i=0;i<nums.length - 1;i++){
	// 	stack.push(nums[i]);
	// 	while(stack.length && stack[stack.length - 1] < nums[i + 1]){
	// 		nextGreaterElementsArray[nums.indexOf(stack.pop())] = nums[i + 1];
	// 	}
	// }

	for(i=0;i<nums.length - 1;i++){
		stack.push(i);
		while(stack.length && nums[stack[stack.length - 1]] < nums[i + 1]){
			nextGreaterElementsArray[stack.pop()] = nums[i + 1];
		}
	}
	return nextGreaterElementsArray;
};

var printLineWise = function(arr1, arr2){
	for(var i=0;i<arr1.length;i++){
		console.log(arr1[i] + ' --> ' + arr2[i]);
	}
};

arr1 = [11, 13, 11,  21, 3];
arr2 = [11, 11, 11, 11, 11];
arr3 = [11, 12, 13, 14, 15];
arr4 = [1,1,1,1,1,1,1,2];

console.log(nextGreaterElements(arr4));
printLineWise(arr4, nextGreaterElements(arr4));
// console.log(nextGreaterElements(arr2));
// console.log(nextGreaterElements(arr3));
