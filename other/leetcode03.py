class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        DIRS = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
        def turn(_key, direction):
            return (direction + 3 + 2*_key) % 4

        def move(point, vector):
            return [coord+move for coord, move in zip(point, vector)]

        direction = 0
        point = [0, 0]
        points = []
        points.append(point)
        #max_distance = 0
        for com in commands:
            if com < 0:
                direction = turn(com, direction)
                continue
            for length in range(com):
                new_point = move(point, DIRS[direction])
                if new_point not in obstacles:
                    point = new_point
            points.append(point)
        distances = [x**2 + y**2 for x, y in points]
        return max(distances)

s = Solution()
s.robotSim(commands = [4,-1,3], obstacles = [])
