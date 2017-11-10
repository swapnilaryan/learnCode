/**
 * Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits
 * existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists,
 * you need to return -1.
 * @param {number} n
 * @return {number}
 */
var nextGreaterElement = function(n) {
	if (n==null){
		return -1;
	}else if(n < 10){
		return -1;
	}

	//	Check if n is in descending order e.g. 4321. Then -1 .Else if ascending order then swap last two and return.
	// var num = n.toString(10).split('').map(Number);
	var num = Array.from(n.toString()).map(Number);
	for(var i=num.length-1;i>0;i--){
		if(num[i] > num[i-1]){
			break;
		}
	}
	if (i==0){
		return -1;
	}

	smallest = i;
	x = num[i-1];


	for (var j=i+1;j<num.length;j++){
		if (num[j] > x && num[j] < num[smallest])
			smallest = j;
	}

	// Swap
	var temp = num[smallest];
	num[smallest] = x;
	num[i-1] = temp;

	var toSortArr = num.splice(i, num.length);
	temp = toSortArr.sort(function(a,b){
		return a-b;
	});


	num = num.concat(temp);

	return parseInt(num.join(""));
};

console.log(nextGreaterElement(172322));
console.log(nextGreaterElement(12443322));
