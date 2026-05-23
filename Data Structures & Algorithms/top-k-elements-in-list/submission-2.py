class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1. get the freq of elements
        count = Counter(nums) #stores the dict

        #2. Build the heap form the sorted array
        min_heap = []
        for num , freq in count.items():
            
            heapq.heappush(min_heap , (freq , num))
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [item[1] for item in min_heap]