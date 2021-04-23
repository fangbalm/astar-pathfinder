import pygame
import math
import colors
from queue import PriorityQueue

WIDTH = 800 
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Pathfinder")

class Spot: 
    def __init__(self, row, col, width, total_rows):
        self.row = row 
        self.col = col
        self.x = row * width 
        self.y = col * width 
        self.color = colors.WHITE
        self.neighbors = []
        self.width = width 
        self.total_rows = total_rows 

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == colors.PINK

    def is_open(self): 
        return self.color == colors.RED

    def is_barrier(self): 
        return self.color == colors.BROWN 

    def is_start(self): 
        return self.color == colors.YELLOW

    def is_end(self):
        return self.color == colors.TURQUOISE

    def reset(self):
        self.color == colors.WHITE

    def make_closed(self): 
        self.color = colors.PINK

    def make_open(self):
        self.color = colors.RED

    def make_barrier(self): 
        self.color = colors.BROWN

    def make_start(self): 
        self.color = colors.YELLOW
    
    def make_end(self):
        self.color = colors.TURQUOISE

    def make_path(self):
        self.color = colors.PURPLE 

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid): 
        pass

    def __lt__(self, other):
        return false 

def h(p1, p2): 
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def make_grid(rows, width): 
    grid = []
    gap = width // rows 
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid


def draw_grid(win, rows, width):
    gap = width // rows 
    for i in range(rows):
        pygame.draw.line(win, colors.GRAY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, colors.GRAY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
    win.fill(colors.WHITE)

    for row in grid: 
        for spot in row: 
            spot.draw(win) 
        
    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width): 
    gap = width // rows 
    y,x = pos 

    row = y // gap 
    col = x // gap 

    return row, col

def main(win, width): 
    ROWS = 30
    grid = make_grid(ROWS, width)

    start = None 
    end = None 

    run = True 
    started = False 
    while run: 
        draw(win, grid, ROWS, width)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = false 

            if started: 
                continue

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start:
                    start = spot
                    start.make_start()
                
                elif not end: 
                    end = spot 
                    end.make_end()
                
                elif spot != end and spot != start: 
                    spot.make_barrier()
            
            elif pygame.mouse.get_pressed()[2]: 
                pass

    pygame.quit()

main(WIN, WIDTH)










