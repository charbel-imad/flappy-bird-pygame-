#april 2024
import pygame as pg,sys,random
from pygame import Vector2

class BIRD():
    def __init__(self):
        self.position = Vector2(10,cell_size*8 )
    def draw(self):
        self.bird_o=pg.Rect((self.position.x,self.position.y,cell_size,cell_size))
        pg.draw.rect(screen,(237, 245, 17),self.bird_o)

    def die(self):
        print(f"lost your score was {score_n}")
        pg.quit()
        sys.exit()

class PIPE:
    def __init__(self):
        self.size = random.randint(2,11)*cell_size
        self.position = Vector2(cell_num_x*cell_size-cell_size*3,0)      
    def add_pipe(self):
        self.pipe_rect = pg.Rect(self.position.x,
                                 self.position.y,
                                 3*cell_size,
                                 self.size)
        pg.draw.rect(screen,(0,255,0),self.pipe_rect)
        self.pipe_rect_2 = pg.Rect(self.position.x,
                                   self.position.y+self.size+4*cell_size ,
                                   3*cell_size,
                                   cell_num_y*cell_size-(self.size+3*cell_size))
        pg.draw.rect(screen,(0,255,0),self.pipe_rect_2)
    def check_loss(self):
        if pg.Rect.colliderect(bird.bird_o,self.pipe_rect) or pg.Rect.colliderect(bird .bird_o,self.pipe_rect_2):
            bird.die( )
        if bird.position.y >= 640:
            bird.die()

    def update_pipes(self):
         self.position.x -= cell_size
         if pipes_l[0].position.x <= bird.position.x-3*cell_size:
             global score_n 
             score_n +=1
             pipes_l.remove(pipes_l[0])

score_n  = 0
cell_num_x = 30
cell_num_y = 16
cell_size = 40
pg.init()
pg.font.init()
my_font = pg.font.SysFont('Comic Sans MS', 30)


screen = pg.display.set_mode((cell_num_x*cell_size,cell_num_y*cell_size))
pg.display.set_caption("flappy bird")
clock = pg.time.Clock()

bird = BIRD()
pipes_l = [PIPE()]

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and bird.position.y > 4  :
                bird.position.y -= cell_size*3
    screen.fill((91,208,235))
    score = my_font.render(f"score:{int(score_n)}",False,(255,255,255))
    screen.blit(score,(10,10))
    bird.draw()
    bird.position.y += cell_size 
    if pipes_l[-1].position.x <= cell_num_x*cell_size-15.9*cell_size:
        pipes_l.append(PIPE())
    for i in pipes_l:
        i.add_pipe()
        i.update_pipes()
        i.check_loss()


    clock.tick(7)
    pg.display.update()