
var majorityElement = function(nums) {
    // Boyer-Moore Voting Algorithm 
    var count = 0
    var x = 0 
    for(var i = 0; i<nums.length ; i++){
        if(count == 0){
            x = nums[i]
        }
        if (nums[i] == x){
            count +=1
        }
        else {
            count-=1
        }
    
    }
    return x
};