class Solution {

    /**
     * @param Integer[][] $ranges
     * @param Integer $left
     * @param Integer $right
     * @return Boolean
     */
    function isCovered($ranges, $left, $right) {
        
        for ($i = $left; $i <= $right; $i++){
            $covered = false;
            foreach($ranges as $x) {
                if (($x[0] <= $i) and ($i <= $x[1])){
                    $covered = true;
                    break;
                }
            }
            if (!$covered) return false;
        }
        return true;
    }
}