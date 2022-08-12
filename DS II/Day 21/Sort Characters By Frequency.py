class Solution:
    def frequencySort(self, s: str) -> str:
        counter = {}
        
        for c in s:
            counter[c] = counter.get(c, 0) + 1
            
        priority_queue = []
        
        for key, value in counter.items():        
            heapq.heappush(priority_queue, (-value, key))
        
        results = ""
        for k in range(len(priority_queue)):      
            pair = heapq.heappop(priority_queue)

            for i in range(-pair[0]):
                results += pair[1]

        
        return results