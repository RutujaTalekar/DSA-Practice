class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # Using min heap / priority queue
        intervals.sort(key = lambda x: x[0])

        # to store an retrieve min end times 
        heap = []

        for start, end in intervals:
            
            if heap and heap[0] <= start:
                heapq.heappop(heap)  # Reuse the room
            
            # Allocate a new room (or reuse the popped one)
            heapq.heappush(heap, end)
        
        # max number of rooms used at once will be length of heap
        return len(heap)








        # Break the intervals list into start time list and end time list
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        # Indices
        s, e = 0, 0
        # To store current need of meeting rooms
        count, res = 0, 0

        while (s < len(start)):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                e += 1
                count -= 1
            res = max (res, count)
        return res
            

        