class Solution:
    def compress(self, chars: List[str]) -> int:

        '''
        Tricky solution, understand the approach
        '''
        i = 0
        n = len(chars)
        insert_at = 0

        while i < n:
            char = chars[i]
            freq = 1

            while i+freq < n and char == chars[i+freq]:
                freq += 1
            
            chars[insert_at] = char
            insert_at += 1

            if freq > 1:
                chars[insert_at: insert_at + len(str(freq))] = list(str(freq))
                insert_at += len(str(freq))
            
            i+= freq
        
        chars = chars[:insert_at]
        return len(chars)


        