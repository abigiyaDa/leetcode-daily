
var sortedSquares = function(nums) {
    var left = 0
    var right = nums.length -1
    let list1 = []
    while (left <= right) {
        if (Math.abs(nums[left]) < Math.abs(nums[right])){
            list1.push((nums[right]**2))
            right -=1
        }else {
            list1.push((nums[left]**2))
            left += 1
        }
    }  
    list1.reverse()
    return list1
};