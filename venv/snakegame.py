class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction


    def takestep(self, posistion):
        self.body = self.body[1:]+posistion

    def set_direction(self,direction):
        self.direction = direction


class Apple:
    def __init__(self):
        self

class Game:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def create_empty(self):
        board = []
        for i in range(self.height):
            board.append([])
            for k in range(self.width):
                board[i].append(None)
        return board

    def render(self):
        matrix = self.create_empty()
        print('+'+ '--'*len(matrix[0]) + '+')
        for i in matrix :
            grid = [x if x else ' ' for x in i]
            print('| ' + ' '.join(grid) + '|')
        print('+'+'--'*len(matrix[0])+'+')

if __name__ == '__main__':
    test = Game(10,5)
    test.render()