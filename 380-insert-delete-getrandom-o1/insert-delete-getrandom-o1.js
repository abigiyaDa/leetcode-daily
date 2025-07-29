
var RandomizedSet = function() {
    this.nums = []
    this.my_dict = new Map()
    
};

RandomizedSet.prototype.insert = function(val) {
    if (this.my_dict.has(val)) return false

    
    // insert to a map => map.set(key, value)
    this.my_dict.set(val,this.nums.length)
    this.nums.push(val)

    return true
};

RandomizedSet.prototype.remove = function(val) {
    if(!this.my_dict.has(val)) return false
    
    // get the last element in the list and the index of val 
    const index_of_val = this.my_dict.get(val)
    const last_element = this.nums[this.nums.length-1]

    //swap - put last element inplace of val
    this.nums[index_of_val] = last_element
    this.my_dict.set(last_element,index_of_val)
    
    // remove the last element from nums and remove val from the map
    this.nums.pop()
    this.my_dict.delete(val)
    return true
};

RandomizedSet.prototype.getRandom = function() {
    const rand_index = Math.floor(Math.random()*this.nums.length)
    return this.nums[rand_index]
};
