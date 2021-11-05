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

    def check_collision(self,snake):
        head = snake.head()
        head_y = head[0]
        head_x = head[1]
        upperbound = self.height-1
        rightbound = self.width-1
        if head_y > upperbound or head_y < 0: return False
        elif head_x > rightbound or head_x <0: return False
        elif head in snake.body[:-1]: return False
        else: return  True


    def create_empty(self):
        board = []
        for i in range(self.height):
            board.append([])
            for k in range(self.width):
                board[i].append(None)
        return board

    def insert_snake(self,head,body,grid,height):
        if head[0] == height:
            grid[head[1]] = 'X'

        for b in body:
            if b[0] == height:
                grid[b[1]] = 'O'

        return grid

    def render(self):
        matrix = self.create_empty()
        print('+'+ '--'*len(matrix[0]) + '+')
        *body,head = self.snake.body
        for height,i in enumerate(matrix) :
            grid = [x if x else ' ' for x in i]
            self.insert_snake(head,body,grid,height)
            print('| ' + ' '.join(grid) + '|')
        print('+'+'--'*len(matrix[0])+'+')

    def game_loop(self,snake):
        while True:
            move = self.move_dic[input('enter direction ').upper()]
            dir = snake.set_direction(move)
            nex_p = snake.next_pos(dir)
            snake.takestep(nex_p)
            if not self.check_collision(snake):
                return
            self.render()


if __name__ == '__main__':
    test = Game(10,10)
    test.render()
    test.game_loop(test.snake)
    #print(test.snake.body)
    #test.render()