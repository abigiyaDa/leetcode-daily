var twoSum = function(nums, target) {
    const x = {}; // to store the indices of the numbers
    // Iterate through the array
    for (let i = 0; i < nums.length; i++) {
        // Calculate the complement of the current number that would sum up to the target
        const z = target - nums[i];
        if (z in x) {
            // If the complement exists in the map, return the indices of the current number and the complement
            return [x[z], i];
        } else {
            // Otherwise, store the index of the current number
            x[nums[i]] = i;
        }
    }
    return [];  // in case no solution found, just for safety
};
