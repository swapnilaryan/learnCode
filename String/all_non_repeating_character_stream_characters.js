var all_non_repeating_character_stream_characters = function (str) {
	if(str == null || str.length<1){
		return str;
	}

	var dll = [];
	var repeated = new Array(256).fill(0);
	for(var i=0;i<str.length;i++){
		repeated[str.charCodeAt(i)] += 1;
		if(repeated[str.charCodeAt(i)]>1) {
			if(dll.includes(str[i])){
				dll = dll.filter(function(a){
					return (a != str[i]);
				})
			}
		}else if(repeated[str.charCodeAt(i)]==1) {
			dll.push(str[i]);
		}
	}
	console.log(dll);
};

all_non_repeating_character_stream_characters('geeksforgeeksandgeeksquizfor');
