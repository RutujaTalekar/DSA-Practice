class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # iterate through strs
        # sort alphabetically each string in strs
        # store in sorted_strs
        # use map to compare k:v k -> sorted key, v -> groups of strngs
        res = []

        strs_map = {idx:string for idx, string in enumerate(strs)}
        print(strs_map)
        sorted_strs = list()

        for idx, string in enumerate(strs):
            sorted_chars = sorted(string)
            sorted_strs.append("".join(sorted_chars))
        print(sorted_strs)
        

        keys = set(sorted_strs)
        print(keys)

        for key in keys:
            temp = []
            for idx in range(len(sorted_strs)):
                if key == sorted_strs[idx]:
                    temp.append(strs_map[idx])
                
            res.append(temp)
        
        return res
            

            
        # for sorted_str in sorted_strs:









