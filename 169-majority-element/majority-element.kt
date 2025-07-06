class Solution {
    fun majorityElement(nums: IntArray): Int {
        var count = 0
        var x=0
        for (i in nums.indices){
            if (count == 0){
                x=nums[i]
            }
            if (x == nums[i]){
                count+=1
            }else{
                count-=1
            }
        }
        return x
    }
}