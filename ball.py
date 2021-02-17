from headerfile import *
from paddle import *

class Ball:
    # def __init__(self,r,c):
    def __init__(self):
        self.__rownum = PADDLE_ROW - 1
        self.__colnum = (int)((Paddle().getColnum() + PADDLE_LENGTH)/2)
        self.__ball = Fore.RED + 'O'
        self.__xspeed = 1
        self.__yspeed = -1
    
    def placeBall(self,grid):
        grid[self.__rownum,self.__colnum] = self.__ball

    # def ballWallcollision(self,grid,temp_row,temp_col):
    #     if self.__colnum < 0 or  self.__colnum > WIDTH - 1:
    #         self.__xspeed = -1*(self.__xspeed)

    # outside this class

    def moveBall(self,grid):
        grid[self.__rownum,self.__colnum] = ' '
        temp_row = self.__rownum + self.__yspeed
        temp_col = self.__colnum + self.__xspeed
        
        ''' handling collision with wall'''
        if temp_col < 0 or temp_col > WIDTH -1:
            self.__xspeed = -1*(self.__xspeed)
        if temp_row < 0 or temp_row > HEIGHT -1:        # subject to change
            self.__yspeed = -1*(self.__yspeed)

        # ''' handle collision with slider'''



        # ballWallCollision(grid,temp_row,temp_col)
        self.__rownum += self.__yspeed
        self.__colnum += self.__xspeed
        grid[self.__rownum,self.__colnum] = self.__ball
    
        