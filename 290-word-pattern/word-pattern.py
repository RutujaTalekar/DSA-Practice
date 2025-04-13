class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''
        pattern = "abba", s = "dog cat cat dog"

        extract words from s
        map words with each letter in the pattern, store as KV in map
        if already exists, the cur word should be same as present in hashmap
        
        '''
        s_list = s.split()
        pattern_map ={}
        seen = set()

        if len(s_list) != len(pattern):
            return False
        

        for i in range(len(pattern)):
            char = pattern[i]
            if char in pattern_map:
                if pattern_map[char] != s_list[i]:
                    return False
            else:
                if s_list[i] in seen:
                    return False
                pattern_map[char] = s_list[i]
                seen.add(s_list[i])
        
        return True


        