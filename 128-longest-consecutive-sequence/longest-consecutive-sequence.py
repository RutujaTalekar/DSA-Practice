class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Every number in the nums list can potentially be start of longest consecutive sequence
        So for brute force, we have to traverse each number and iterate over all the entire list
            to check if num+1 exists. This can take O(n square) time. If we dont use nums_set
            then it will take O(n cube) time
        
        To make it faster - use sets, so you are avoiding duplicate numbers and your lookups are O(1)
        This is still O(n square)
        Key is to avoid the numbers which are +1 larger than a number present in nums set, 
        because logically that num would be already a part of a larger sequence.
        This will be O(n)
        '''

        nums_set = set(nums)
        longest_seq = 0

        for num in nums_set:
            if num-1 not in nums_set:
                current_seq = 1
                current_num = num + 1
                while current_num in nums_set:
                    current_seq += 1
                    current_num += 1
                longest_seq = max(current_seq, longest_seq)
        
        print(longest_seq)
        return longest_seq
