class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)==0:
            return 0
        vec = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        my_list = []
        count = 0
        for i in range(len(grid)): 
            for j in range(len(grid[0])):
                if vec[i][j]==0 and grid[i][j]=='1':
                    my_list.append((i,j))
                    while(my_list):
                        vec[my_list[0][0]][my_list[0][1]] = 1
                        if my_list[0][0]+1<len(grid) and vec[my_list[0][0]+1][my_list[0][1]]==0:
                            if grid[my_list[0][0]+1][my_list[0][1]]=='1':
                                vec[my_list[0][0]+1][my_list[0][1]] = 1
                                my_list.append((my_list[0][0]+1,my_list[0][1]))
                        if my_list[0][1]+1<len(grid[0]) and vec[my_list[0][0]][my_list[0][1]+1]==0:
                            if grid[my_list[0][0]][my_list[0][1]+1]=='1':
                                vec[my_list[0][0]][my_list[0][1]+1] = 1
                                my_list.append((my_list[0][0],my_list[0][1]+1))
                        if my_list[0][0]-1>=0 and vec[my_list[0][0]-1][my_list[0][1]]==0:
                            if grid[my_list[0][0]-1][my_list[0][1]]=='1':
                                vec[my_list[0][0]-1][my_list[0][1]] = 1
                                my_list.append((my_list[0][0]-1,my_list[0][1]))
                        if my_list[0][1]-1>=0 and vec[my_list[0][0]][my_list[0][1]-1]==0:
                            if grid[my_list[0][0]][my_list[0][1]-1]=='1':
                                vec[my_list[0][0]][my_list[0][1]-1] = 1
                                my_list.append((my_list[0][0],my_list[0][1]-1))
                        my_list.remove(my_list[0])
                        
                    count += 1
        return count
    