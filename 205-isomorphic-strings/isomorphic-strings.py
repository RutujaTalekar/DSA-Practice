class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {char:[] for char in s}
        t_map = {char:[] for char in t}

        s_set = set(s)
        t_set = set(t)
        
        if len(s_set) != len(t_set):
            return False

        for idx, char in enumerate(s):
            if char in s_map:
                s_map[char].append(idx)
        
        for idx, char in enumerate(t):
            if char in t_map:
                t_map[char].append(idx)
            else:
                t_map[char] = [idx]
        

        return list(s_map.values()) == list(t_map.values())


        #paper -> title
        #paper -> ttile
        
        '''
        TRAVERSE S
        Store 
        P-> [0, 2]
        A -> [1]
        E -> [3]
        R -> [4]

        TRAVERSE T
        store
        T->[0, 2]
        I->[1]
        L -> [3]
        E -> [4]

        Extract the values and compare
        '''

        ##"foo", t = "bar"
        '''
        {f:[0], o:[1,2]}
        {b:[0], a:[1,2]}
        '''

        









        