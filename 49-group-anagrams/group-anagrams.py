class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_map = defaultdict(list)
        for char in strs:
            key = ''.join(sorted(char))
            dict_map[key].append(char)
        return list(dict_map.values())
        
        
        # res = []
        # strs_map = {idx:string for idx, string in enumerate(strs)}
        # sorted_strs = list()

        

        # for idx, string in enumerate(strs):
        #     sorted_chars = sorted(string)
        #     sorted_strs.append("".join(sorted_chars))        

        # keys = set(sorted_strs)

        # for key in keys:
        #     temp = []
        #     for idx in range(len(sorted_strs)):
        #         if key == sorted_strs[idx]:
        #             temp.append(strs_map[idx])
        #     res.append(temp)
        
        # print(strs_map)
        # print(sorted_strs)
        
        # return res
        
            

        









