class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def isCycle(course: int) -> bool:
            res = False

            if course in visited:
                return res
            
            if course not in adj:
                return False
            
            if course in visiting:
                return True
            
            visiting.add(course)
            for nei in adj[course]:
                if isCycle(nei):
                    return True
                else:
                    continue
            visited.add(course)
            return res
        
        # create an adjacency map of course -> prerequisites
        adj = {}
        visited = set()
        visiting = set()

        for course, pre in prerequisites:
            if course in adj:
                adj[course].append(pre)
            else:
                adj[course] = [pre]
        
        for course in adj:
            if isCycle(course):
                return False
            visited.add(course)
        
        
        
        
        
        
        '''
        '''
        visiting = set()
        visited = set()

        # adj list to visualize the graph
        courseGraph = defaultdict(list)

        for course, prereq in prerequisites:
            courseGraph[course].append(prereq)
        
        # helper function - return true is cycles detected
        def dfs(course):
            # edge cases - cycles. 
            if course in visiting:
                return True
            if course in visited:
                return False # base case for courses with no prereqs
            visiting.add(course)
            for prereq in courseGraph[course]:
                if dfs(prereq):
                    return True
            visiting.remove(course)
            visited.add(course)
            return False
        
        for crs in range(numCourses):
            if dfs(crs):
                return False
        return True
        