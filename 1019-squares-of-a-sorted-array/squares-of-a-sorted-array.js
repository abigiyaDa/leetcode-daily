
var sortedSquares = function(nums) {
    var left = 0
    var right = nums.length -1
    let list1 = []
    while (left <= right) {
        if (Math.abs(nums[left]) < Math.abs(nums[right])){
            list1.unshift((nums[right]**2))
            right -=1
        }else {
            list1.unshift((nums[left]**2))
            left += 1
        }
    }  
    return list1
};