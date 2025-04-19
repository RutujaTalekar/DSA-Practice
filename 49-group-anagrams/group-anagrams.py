class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # O(n * m)
        '''
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count_temp = ord(c) - ord("a")
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())
        '''

        # O(n * m * log m)
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())
        


        # Draft 1 solution
        '''
        dict_map = defaultdict(list)
        for char in strs:
            key = ''.join(sorted(char))
            dict_map[key].append(char)
        return list(dict_map.values())
        '''
        
        
            

        









