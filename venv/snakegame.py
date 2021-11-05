import random

class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction

    def takestep(self, posistion):
        self.body = self.body[1:]+[posistion]

    def next_pos(self,direction):
        zipped = zip(self.body[-1],direction)
        zipped = (list(zipped))
        new_pos = tuple([sum(x) for x in zipped])
        #print(new_pos)

        return new_pos

    def set_direction(self,direction):
        self.direction = direction
        return self.direction

    def head(self):
        return self.body[-1]


class Apple:
    def __init__(self):
        self

    def generate_apple(self,height,width):
        apple_x = random.randint(0, width-1)
        apple_y = random.randint(0, height-1)
        return (apple_y,apple_x)

class Game:
    UP = (-1,0)
    DOWN = (1,0)
    RIGHT = (0,1)
    LEFT = (0,-1)
    move_dic = {'W':UP, 'A':LEFT, 'S':DOWN, 'D':RIGHT}
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.snake = Snake([(0, 0), (1, 0), (2, 0), (3, 0)], self.UP)
        self.apple = self.check_apple(height,width,self.snake)

    def check_apple(self,height,width,snake):
        while True:
            apple = Apple.generate_apple(self,height,width)
            if apple not in snake.body:
                 return apple

    def increase_size(self,snake,height,width):
        last_segment = snake.body[0]
        second_last_segment = snake.body[1]
        direction = snake.direction
        next_segment = (last_segment[0] , last_segment[1])
        while next_segment in snake.body and next_segment
        #TODO: create new function that checks if new segment in and out of bounds
        #TODO: two loops in while, first two increase y, then to increase x



        '''
        if direction == self.UP:
            new_segment = (last_segment[0]+1,last_segment[1])
        elif direction == self.DOWN:
            new_segment = (last_segment[0]-1,last_segment[1])
        elif direction == self.RIGHT:
            new_segment = (last_segment[0],last_segment[1]-1)
        elif direction == self.LEFT:
            new_segment = (last_segment[0],last_segment[1]+1)'''

        snake.body.insert(0,new_segment)


    def check_collision(self,snake):
        head = snake.head()
        head_y = head[0]
        head_x = head[1]
        upperbound = self.height-1
        rightbound = self.width-1
        if head_y > upperbound or head_y < 0: return False
        elif head_x > rightbound or head_x <0: return False
        if head in snake.body[:-1]: return False
        else: return  True

    def check_apple_collision(self,snake,apple):
        head = snake.head()
        head_y, head_x = head
        apple_y, apple_x = apple
        if head_y == apple_y and head_x == apple_x:
            return True

    def create_empty(self):
        board = []
        for i in range(self.height):
            board.append([])
            for k in range(self.width):
                board[i].append(None)
        return board

    def insert_into(self,head,body,grid,height,apple):
        if head[0] == height:
            grid[head[1]] = 'X'
        for b in body:
            if b[0] == height:
                grid[b[1]] = 'O'
        if apple[0] == height:
            grid[apple[1]] = '*'
        return grid

    def render(self):
        matrix = self.create_empty()
        print('+'+ '--'*len(matrix[0]) + '+')
        *body,head = self.snake.body
        apple = self.apple
        for height,i in enumerate(matrix) :
            grid = [x if x else ' ' for x in i]
            self.insert_into(head,body,grid,height,apple)
            print('| ' + ' '.join(grid) + '|')
        print('+'+'--'*len(matrix[0])+'+')

    def game_loop(self,snake,apple):
        score = 0
        while True:
            move = self.move_dic[input('enter direction ').upper()]
            dir = snake.set_direction(move)
            nex_p = snake.next_pos(dir)
            snake.takestep(nex_p)
            if not self.check_collision(snake):
                return
            if self.check_apple_collision(snake,self.apple):
                self.apple = self.check_apple(self.height,self.width,snake)
                score +=1
                self.increase_size(snake,self.height,self.width)
            print(f'{score}')
            self.render()


if __name__ == '__main__':
    test = Game(10,10)
    test.render()
    test.game_loop(test.snake,test.apple)
    #print(test.snake.body)
    #test.render()