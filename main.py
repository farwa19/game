import pygame
from random import randint
class new_game:
    def __init__(self):
        pygame.init()
        
        self.load_images()
        self.points = 0
        
        self.game_font = pygame.font.SysFont("Arial", 24)
        
        self.x = randint(0,600)
        self.y = randint(0,400)
        self.a = randint(0,591)
        self.b = randint(0,395)
        self.c= -1
        self.d = 394
        print(self.x,self.y,self.a,self.b)
        self.clock = pygame.time.Clock()
       
        


        window_height = 480
        window_width = 640
        self.window = pygame.display.set_mode((window_width, window_height))

        pygame.display.set_caption("game")

        self.main_loop()
    def load_images(self):
        self.robot = pygame.image.load("robot.png")
        self.monster = pygame.image.load("monster.png")
        self.door  = pygame.image.load("door.png")
        self.coin= pygame.image.load("coin.png")
        
    def main_loop(self):
        while True:
            self.check_events()
            self.draw_window()
            self.move()
           

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def draw_window(self):
        self.window.fill((0, 128, 128))
        self.window.blit(self.coin,(self.a,self.b))
        self.task= self.game_font.render("Task: collect 10 coins", True, (0, 0, 0))
        self.remain = self.game_font.render(f"remaining points: {10 - self.points}", True, (0, 0, 0))
        self.text = self.game_font.render(f"points: {self.points}", True, (0, 0, 0))
        self.window.blit(self.task, (10, 0))
        self.window.blit(self.remain, (10, 26))
        self.window.blit(self.text, (500, 26))
        self.window.blit(self.door,(self.c,self.d))
        self.window.blit(self.robot,(self.x,self.y))
        self.end_game_font = pygame.font.SysFont("Arial", 100)
        self.ta= self.end_game_font.render("END GAME", True, (0, 0, 0))
        
        
        
        
        pygame.display.flip()
        self.clock.tick(60)
        
        
    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP] and self.y >= 0:
            self.y -= 1
            if self.x == self.a and self.y == self.b:
                self.collect_coin()
            elif self.points == 10:
                if self.x == self.c and self.y == self.d:
                    self.enter_door()
        elif keys[pygame.K_DOWN] and self.y + self.robot.get_height() <= 480:
            self.y += 1
            if self.x == self.a and self.y == self.b:
                self.collect_coin()
            elif self.points == 10:
                if self.x == self.c and self.y == self.d:
                    self.enter_door()
        elif keys[pygame.K_LEFT] and self.x >= 0:
            self.x -= 1
            if self.x == self.a and self.y == self.b:
                
                self.collect_coin()
            elif self.points == 10:
                if self.x == self.c and self.y == self.d:
                    self.enter_door()
        elif keys[pygame.K_RIGHT] and self.x + self.robot.get_width() <= 640:
            
            self.x += 1
            if self.x == self.a and self.y == self.b:
                self.collect_coin()
            elif self.points == 10:
                if self.x == self.c and self.y == self.d:
                    self.enter_door()
        
    def collect_coin(self):
        if self.points < 10:
            self.points+=1
            self.a = randint(0,591)
            self.b = randint(0,395)
            print(self.a,self.b)

            self.window.blit(self.coin,(self.a,self.b))
        else:
            if self.c == self.x or self.d == self.y:
                enter_door()
    def enter_door(self):
        
        self.window.blit(self.ta, (120, 150))
        pygame.display.flip()
        print("END")
        
        return True


        


if __name__ == "__main__":
    new_game()

