import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Min heap
        heap = []
        current_max = float('-inf')
        
        # Step 1: Initialize heap with first element from each list
        for i in range(len(nums)):
            val = nums[i][0]
            heap.append((val, i, 0))  # (value, list_index, element_index)
            current_max = max(current_max, val)
        
        heapq.heapify(heap)
        
        # Best range
        best_range = [float('-inf'), float('inf')]
        
        while True:
            min_val, list_idx, elem_idx = heapq.heappop(heap)
            
            # Update best range if smaller
            if current_max - min_val < best_range[1] - best_range[0]:
                best_range = [min_val, current_max]
            
            # Move forward in the same list 
            if elem_idx + 1 == len(nums[list_idx]):
                break  # one list exhausted → stop
            
            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
            
            # Update current max
            current_max = max(current_max, next_val)
        
        return best_range
        