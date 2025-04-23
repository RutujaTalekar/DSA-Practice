class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
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
            

        