var removeDuplicates = function(nums) {
    var a =0
    var b = a+1
    var c = nums.length -1
    while (b <= c){
        if (nums[a] !== nums[b]){
            nums[a+1] = nums[b]
            a+=1
        }
        b+=1
    }
    return a+1
};