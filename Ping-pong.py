#import
from pygame import *
#class "GameSprite"
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
         window.blit(self.image,(self.rect.x,self.rect.y))

win_width = 700
win_height = 500

#Window
window = display.set_mode(
    (win_width, win_height) 
)
display.set_caption("Ping-pong")
background = transform.scale(
    image.load("BACKGROUND.jpg"),
    (win_width, win_height)
)
#time
clock = time.Clock()
#FPS
FPS = 60

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0,0))
    display.update()
    time.delay(50)
