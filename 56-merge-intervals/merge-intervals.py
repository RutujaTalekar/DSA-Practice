class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 1:
            return intervals
        
        '''
        traverse through intervals and compare end to next start, if it overlaps merge
        '''

        output = []
        intervals.sort()

        prev_s, prev_e = intervals[0]
        output.append([prev_s, prev_e])
        for cur_s, cur_e in intervals[1:]:
            if prev_e >= cur_s:
                output.pop()
                output.append([prev_s, max(prev_e,cur_e)])
            else:
                output.append([cur_s, cur_e])
            prev_s, prev_e = output[-1]

        return output