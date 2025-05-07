class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # start visiting rooms starting from 0, use stack -> dfs so we can detect cycles quickly
        stack = [0]
        visited = set()

        while stack:
            room = stack.pop()
            keys = rooms[room]  # get keys at 0 and mark it visited
            visited.add(room)
            for key in keys:
                if key not in visited:
                    stack.append(key)   # add the keys so you visit other rooms
            
        return len(visited) == len(rooms)
            

                    






