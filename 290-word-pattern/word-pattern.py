class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''
        pattern = "abba", s = "dog cat cat dog"

        extract words from s
        map with each letter in pattern
        
        '''
        s_list = s.split()
        pattern_map ={}

        if len(s_list) != len(pattern):
            return False
        
        if len(set(s_list)) != len(set(pattern)):
            return False
        

        for i in range(len(pattern)):
            char = pattern[i]
            if char in pattern_map:
                if pattern_map[char] != s_list[i]:
                    return False
                else:
                    continue
            else:
                pattern_map[char] = s_list[i]
        
        return True


        