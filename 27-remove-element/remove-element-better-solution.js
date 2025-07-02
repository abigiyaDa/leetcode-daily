// using 2 pointers 
var removeElement = function(nums, val) {
    var write = 0

    for (var i = 0 ; i< nums.length; i++){
        if(nums[i] !== val){
            nums[write] = nums [i];
            write ++;
        }
    }
    return write
    
};