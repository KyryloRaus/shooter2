import pygame
from random import randint
pygame.mixer.init()
pygame.font.init()
score = 0
font1 = pygame.font.Font(None, 60)
level_text = font1.render('Level 1', True,(250,250,250))
level_text1 = font1.render('Level 2', True,(250,250,250))
#pygame.mixer.music.load('World 1.mp3')
#pygame.mixer.music.play()
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
w = 700
h = 500
window = pygame.display.set_mode((w,h))
pygame.display.set_caption('Labirint')
background  = pygame.transform.scale(pygame.image.load('Yest-li-zvuk-v-kosmose-.jpg'),(w,h))
class Player(pygame.sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image),(70,70)) #була помилка в слові transform
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Enemy(Player):
    direction = 'right'
    def update(self):
        if self.rect.x <= 300:
            self.direction = 'right'
        if self.rect.x >= 530:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed

class Enemy1(Player):
    direction = 'right'
    def update(self):
        if self.rect.x <= 2:
            self.direction = 'right'
        if self.rect.x >= 100:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed

            
class Hero(Player):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y <= 500: #була неправильна цифра, у нас висота 500
            self.rect.y += self.speed
        if keys[pygame.K_LEFT] and self.rect.x >= 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x <= 700:
            self.rect.x += self.speed

class Wall(pygame.sprite.Sprite):
    def __init__ (self,width,height,color,wall_x,wall_y):
        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill((color))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
        
    def update(self,walls):
        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self,walls,False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self,walls,False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom



                wall_list = pygame.sprite.Group()

                wall = Wall()
                wall_list.add(wall)
                all_sprite_list.add(wall)

                clock = pygame.time.Clock()








hero = Hero('p1.png',10,400,10) #стояв неправильний клас (був Player), потрібен був Hero, у нас клас Hero потрібен для головного героя
enemy = Enemy('p2.png',500,70,30) #стояв неправильний клас (був Player), потрібен клас Enemy, клас Enemy - для створення ворога
enemy1 = Enemy1('fdjdffji.PNG',100,70,10)
skarb = Player('Portal-Transparent-Background.png',500,400,401)
skarb1 = Player('27516-2-portal-photos-thumb.png',630,400,401)
wall = Wall(20,550,(130,183,254),150,100)
wall1 = Wall(20,550,(130,183,254),300,100)
wall2 = Wall(20,550,(130,183,254),400,70)
wall3 = Wall(20,550,(130,183,254),600,0)
wall4 = Wall(100,20,(130,183,254),620,100)
key = Player('Cortex-key.webp',320,400,40)
key1 = Player('Cortex-key.webp',200,400,40)
key2 = Player('Cortex-key.webp',80,300,40)
key3 = Player('Cortex-key.webp',500,200,40)
key4 = Player('Cortex-key.webp',500,75,40)
key5 = Player('Cortex-key.webp',630,30,401)
game = True
finish = False
clock = pygame.time.Clock()
FPS = 60
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    if finish != True: #були неправильні відступи, все поставив у for, а треба було у while
         level_text = font1.render("Level 1", True,(250,250,250))
         window.blit(background, (0,0))
         window.blit(level_text, (250,0))
         hero.update()
         enemy.update()
         enemy1.update()
         hero.reset()
         enemy.reset()
         enemy1.reset()
         skarb.reset()
         key.reset()
         key1.reset()
         key2.reset()
         key3.reset()
         key4.reset()
         key5.reset()
         skarb1.reset()
         wall.draw_wall()
         wall1.draw_wall()
         wall2.draw_wall()
         wall3.draw_wall()
         wall4.draw_wall()
         if pygame.sprite.collide_rect(hero,wall) or pygame.sprite.collide_rect(hero,enemy) or pygame.sprite.collide_rect(hero,wall2) or pygame.sprite.collide_rect(hero,wall3) or pygame.sprite.collide_rect(hero,wall1) :
            hero.rect.x = 10
            hero.rect.y = 400




            


            
             
         if pygame.sprite.collide_rect(hero,key):
             enemy.rect.x = 30000000
             enemy.rect.y = 30000000

         if pygame.sprite.collide_rect(hero,key4):
             enemy1.rect.x = 30000000
             enemy1.rect.y = 30000000
             wall4.rect.x = 20000000
             wall4.rect.y = 20000000

         if pygame.sprite.collide_rect(hero,key1):
              hero.rect.x = 630
              hero.rect.y = 310
         if pygame.sprite.collide_rect(hero,skarb1):
             hero.rect.x = 500
             hero.rect.y = 400
         if pygame.sprite.collide_rect(hero,enemy1):
              hero.rect.x = 10
              hero.rect.y = 400
         if pygame.sprite.collide_rect(hero,key2):
              hero.rect.x = 200
              hero.rect.y = 300
         if pygame.sprite.collide_rect(hero,key2):
              hero.rect.x = 200
              hero.rect.y = 300
         if pygame.sprite.collide_rect(hero,key3):
              hero.rect.x = 320
              hero.rect.y = 300
         if pygame.sprite.collide_rect(hero,key5):
             hero.rect.x = 10
             hero.rect.y = 400
             key.rect.x = 3020000
             key.rect.y = 31000000
             key1.rect.x = 302000222
             key1.rect.y = 310000222
             key2.rect.x = 310002323
             key2.rect.y = 310002323
             key3.rect.x = 310002323
             key3.rect.y = 310002323
             key4.rect.x = 310002323
             key4.rect.y = 310002323
             key5.rect.x = 310002323
             key5.rect.y = 310002323
             wall.rect.x = 310002323
             wall.rect.y = 310002323
             wall1.rect.x = 310002323
             wall1.rect.y = 310002323
             wall2.rect.x = 310002323
             wall2.rect.y = 310002323
             wall3.rect.x = 310002323
             wall3.rect.y = 310002323
             wall4.rect.x = 310002323
             wall4.rect.y = 310002323
             skarb.rect.x = 310002323
             skarb.rect.y = 310002323
             skarb1.rect.x = 310002323
             skarb1.rect.y = 310002323
             window.blit(level_text, (1000,1000))
                 


             
        
             
             
             
             
        
        

    pygame.display.update()
    clock.tick(FPS)