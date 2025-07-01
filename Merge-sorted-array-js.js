var merge = function(nums1, m, nums2, n) {
    var k = n+m-1
    var n1 = n-1
    var m1 = m-1

    while (n1 >= 0){
        if (m1 < 0){
            nums1[k] = nums2[n1];
            k-=1;
            n1-=1;
        }
        else if (nums1[m1] < nums2[n1]){
            nums1[k] = nums2[n1];
            k-=1;
            n1-=1;
        }else {
            nums1[k] = nums1[m1];
            k-=1;
            m1-=1;
        }


    }
};