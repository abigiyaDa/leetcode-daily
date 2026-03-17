class Solution {

    /**
     * @param Integer[][] $matches
     * @return Integer[][]
     */
    function findWinners($matches) {
        $checker = [];
        foreach($matches as $match){
            $winner = $match[0];
            $loser = $match[1];
            // check if the winner is in checker 
            if(!isset($checker[$winner])){
                $checker[$winner] = 0;
            }
            // check if loser is in checker 
            if(!isset($checker[$loser])){
                $checker[$loser] = 0;
            }

            $checker[$loser] += 1;
        }

        $res = [[],[]];
        foreach ($checker as $player => $losses){
            if ($losses == 0){
                $res[0][] = $player;
            }elseif ($losses == 1){
                $res[1][] = $player;
            }

        }
        sort($res[1]);
        sort($res[0]);

        return $res;
    }
}


