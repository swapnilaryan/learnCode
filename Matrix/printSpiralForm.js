var spiralForm = function(matrix){
	if(matrix==null){
		return;
	}else if(matrix.length<1){
		return matrix;
	}
	var spiralMatrix = [];

	while (matrix.length){
		// Right
		var right = matrix.shift();
		if(right){
			spiralMatrix = spiralMatrix.concat(right);
		}

		//Down
		for(var i=0;i<matrix.length-1;i++){
			var temp = matrix[i].pop();
			if(temp){
				spiralMatrix.push(temp);
			}
		}

		//Bottom
		var left = matrix.pop();
		if(left){
			spiralMatrix = spiralMatrix.concat(left.reverse());
		}

		//Up
		for(i=matrix.length-1;i>0;i--){
			temp = matrix[i].shift();
			if(temp){
				spiralMatrix.push(temp);
			}
		}
		if(!right && !left){
			break;
		}
	}
	return spiralMatrix;
};

var arr = [[1,  2,  3,  4],
	[5,  6,  7,  8],
	[9,  10, 11, 12],
	[13, 14, 15, 16]];


var arr2 = [[1,  2,  3,  4],
	[5,   7,  8],
	[9,   12],
	[13, 14, 15, 16]];

var arr3= [ [1,2,3],
			[4,5,6],
			[7,8,9]];
console.log(spiralForm(arr2));