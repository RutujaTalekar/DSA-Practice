class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
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
