import pygame
import random
import math

# Initialize the pygame
pygame.init()
# create the screen
screen = pygame.display.set_mode((1920, 1080))
# background image
background_img = pygame.image.load('stars.jpg')

# title and icons (32 X 32) of game
pygame.display.set_caption('Spaceship')
icon = pygame.image.load('space3.png')
pygame.display.set_icon(icon)

# background music

bulletSound = pygame.mixer.Sound("fire.wav")
hitSound = pygame.mixer.Sound("bangSmall.wav")
music = pygame.mixer.music.load("1.mp3")

#pygame.mixer.music.play(-1) # -1 will ensure the song keeps looping

score = 0
class Space_ship:
    def __init__(self, ship_imageX, ship_imageY, vel, ship_width, ship_height, img):
        self.ship_imageX = ship_imageX
        self.ship_imageY = ship_imageY
        self.vel = vel
        self.ship_width = ship_width
        self.ship_height = ship_height
        self.ship_image = pygame.image.load(img)

    def draw_ship(self):
        # blit used to draw image on screen
        screen.blit(self.ship_image, (self.ship_imageX, self.ship_imageY))


class Enemy_ship:
    def __init__(self, enemy_imageX, enemy_imageY, vel, enemy_width, enemy_height, img):
        self.enemy_imageX = [random.randint(0,1900),random.randint(0,1900),random.randint(0,1900),random.randint(0,1900)]
        self.enemy_imageY = [5,5,5,5]
        self.vel = vel
        self.enemy_width = enemy_width
        self.enemy_height = enemy_height
        self.enemy_image = [pygame.image.load(img),pygame.image.load(img),pygame.image.load(img),pygame.image.load(img)]
        self.displaY_enemy = True

    def isCollide(self,i):
      d = math.sqrt(math.pow(enemy.enemy_imageX[i] - bullet.X, 2) + math.pow(enemy.enemy_imageY[i] - bullet.Y, 2))
      if d < 60:
        return True
      else:
        return False

    def draw_enemy(self):
        global score
        # blit used to draw image on screen
        for i in range(4):
            self.enemy_imageX [i]+= self.vel
            if self.enemy_imageX[i] <= self.vel + 20:
                self.vel = 10
                self.enemy_imageY[i] += 30
            elif self.enemy_imageX[i] >= 1777:
                self.vel = -10
                self.enemy_imageY[i] += 30
            collide = self.isCollide(i)
            if collide:
                hitSound.play()
                enemy.enemy_imageX[i] = random.randint(0,1900)
                enemy.enemy_imageY[i] = 5
                bullet.Y= ship.ship_imageY
                score +=1

        # self.ship_imageY += 1
            screen.blit(self.enemy_image[i], (self.enemy_imageX[i], self.enemy_imageY[i]))


class Bullets:
    def __init__(self, bullet_X, bullet_Y, bullet_width, bullet_height, bullet_vel, bullet_img):
        self.bullet_width = bullet_width
        self.bullet_height = bullet_height
        self.bullet_vel = bullet_vel
        self.bullet_img = pygame.image.load(bullet_img)
        self.X = ship.ship_imageX - 40
        self.Y = ship.ship_imageY - 5
        self.visible = False
        self.t = True
        self.next = True

    def draw_bullet(self):
        screen.blit(self.bullet_img, (self.X, self.Y))
        self.t = False


re = 0


#def isCollide():
 #   d = math.sqrt(math.pow(enemy.enemy_imageX - bullet.X, 2) + math.pow(enemy.enemy_imageY - bullet.Y, 2))

  #  if d < 60:
   #     return True
    #else:
     #   return False


def redrawGameWindow():
    #  calling space_ship() to draw image
    ship.draw_ship()
    if enemy.displaY_enemy:
        enemy.draw_enemy()
    # bullet.X = ship.ship_imageX + 44

    if bullet.visible:
        bullet.draw_bullet()
    text = font.render("Score: " + str(score) , 1, (255,255,255))  # Arguments are: text, anti-aliasing, color
    text2 = font.render("Rohit Kashyap", 1, (255,255,255))  # Arguments are: text, anti-aliasing, color

    screen.blit(text,(5,5))
    screen.blit(text2,(1600,10))



  #  text = font.render("Score: " + str(score), 1, (0, 0, 0))  # Arguments are: text, anti-aliasing, color


    # update window
    pygame.display.update()

font = pygame.font.SysFont("comicsans", 50, True)

ship = Space_ship(930, 880, 20, 120, 120, 'shoot3.png')
enemy = Enemy_ship(930, 10, 10, 120, 120, 'e2.png')
bullet = Bullets(ship.ship_imageX, ship.ship_imageY, 32, 32, 5, 'bullet1.png')
running = True
while running:
    # background color
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                if bullet.next:
                    bulletSound.play()
                    bullet.X = ship.ship_imageX + 30
                    bullet.visible = True
                    bullet.t = True

    keys = pygame.key.get_pressed()

    k = pygame.key.get_focused()

    if keys[pygame.K_RIGHT] and ship.ship_imageX < 1920 - ship.vel - ship.ship_width - 20:
        ship.ship_imageX += ship.vel

    if keys[pygame.K_LEFT] and ship.ship_imageX > ship.vel + 20:
        ship.ship_imageX -= ship.vel


  #  collide = isCollide()
   # if collide:
    #    enemy.enemy_imageX = random.randint(0,1900)
     #   enemy.enemy_imageY = 0
      #  bullet.Y= ship.ship_imageY
       # score +=1
        #print('score : {}'.format(score))


    def f():
        if bullet.visible:
            bullet.Y -= 60
        if bullet.Y <= 0:
            bullet.visible = False
            bullet.Y = ship.ship_imageY
            bullet.next = True


    if bullet.visible:
        bullet.next = False
        f()

    redrawGameWindow()
pygame.quit()
