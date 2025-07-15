var canJump = function(nums) {
    var far =0
    for (var i=0;i<nums.length;i++){
        if (i>far){
            return false
        }
        far=Math.max(far, i+ nums[i])
        if (far >= nums.length-1){
            return true
        }
    }

    
};