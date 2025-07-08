var rotate = function(nums, k) {
    k %= nums.length // for k greater then the length of the array
    function reverse(start,end){
        while (start < end) {
            let temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start +=1;
            end -=1;
        }
    }
    reverse(0,nums.length-1);
    reverse(0,k-1);
    reverse(k,nums.length-1);
    
};