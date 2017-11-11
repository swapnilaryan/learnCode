var spiralForm = function (matrix) {
	if (matrix == null) {
		return;
	} else if (matrix.length < 1) {
		return matrix;
	}
	var spiralMatrix = [];
	var rows = matrix.length;
	var cols = matrix[0].length;

	var T = 0;
	var R = cols - 1;
	var L = 0;
	var B = rows - 1;
	var dir = 0;
	var result = [];

	while (T <= B && L <= R) {
		if (dir === 0) {
			for (var i = L; i <= R; i++) {
				result.push(matrix[T][i])
			}
			T++;
			dir = 1;
		} else if (dir === 1) {
			for ( i = T; i <= B; i++) {
				result.push(matrix[i][R]);
			}
			R--;
			dir = 2
		} else if (dir === 2) {
			for ( i = R; i >= L; i--) {
				result.push(matrix[B][i]);
			}
			B--;
			dir = 3
		} else if (dir === 3) {
			for ( i = B; i >= T; i--) {
				result.push(matrix[i][L]);
			}
			L++;
			dir = 0
		}
	}
	return spiralMatrix;
};


var arr = [[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
	[13, 14, 15, 16]];

var arr2 = [[1,  2,  3,  4],
	[5,   7,  8],
	[9,   12],
	[13, 14, 15, 16]];

console.log(spiralForm(arr));