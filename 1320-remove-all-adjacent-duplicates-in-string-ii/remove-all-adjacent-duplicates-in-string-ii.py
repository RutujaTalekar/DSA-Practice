class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # instead, just store the tuple of char with its count in stack, and do the same solution as below
        # tuples are immutable, since we need to update counter use list of lists

        stack = []  # stack of [[char, count]]

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1           # increase the count as char is matched
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])     
        stack = [char*k for char, k in stack]
        return ''.join(stack)







        # this works but it O(n square), also using set to check if there are duplicates doesnt work 
        # well when we have a lage k. It takes more time
        stack = []

        if len(s) >= k and len(set(s)) == 1:
            return s[0]

        for char in s:
            if stack and stack[-1] == char and len(stack) >= k-1 :
                if len(set(stack[-k+1:])) == 1:
                    stack = stack[:-k+1]
                else:
                    stack.append(char)
            else:
                stack.append(char)

        
        return ''.join(stack)
        