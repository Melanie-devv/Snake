import pygame
import random

class snake():
    def __init__(self, display, taille_case, x = 80, y = 80):
        self.display = display
        self.taille_case = taille_case
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0
        self.snakelist = [(-x, -y),(0,0)]
        self.start = (x,y)
        self.snakelist.append(self.start)
        self.taille_serpent = 3
        self.direction = ''
        
    def gauche(self):
        self.x_change -= self.taille_case
        self.y_change = 0
        self.direction = 'gauche'

    def droite(self):
        self.x_change += self.taille_case
        self.y_change = 0
        self.direction = 'droite'

    def haut(self):
        self.x_change = 0
        self.y_change -= self.taille_case
        self.direction = 'haut'

    def bas(self):
        self.x_change = 0
        self.y_change += self.taille_case
        self.direction = 'bas'
    
    def grossir(self):
        self.taille_serpent += 1
        
    def bouger(self):
        self.x += self.x_change
        self.y += self.y_change
        self.snakehead = (self.x, self.y)
        if self.taille_serpent > 3:
            if self.snakehead in self.snakelist:
                return False
        self.snakelist.append(self.snakehead)
        if len(self.snakelist) > self.taille_serpent:
            del self.snakelist[0]
        
        
class Pommes():
    def __init__(self, largeur, hauteur, taille_case, nb_pommes = 1):
        self.largeur = largeur
        self.hauteur = hauteur
        self.taille_case = taille_case
        self.x = round(random.randrange(0, self.largeur - self.taille_case)/self.taille_case)*self.taille_case
        self.y = round(random.randrange(0, self.hauteur - self.taille_case)/self.taille_case)*self.taille_case  
        self.nb_pommes = nb_pommes
        self.pommes_list = []

    def spawn_pommes(self):
        for i in range(self.nb_pommes):
            self.pommes_list.append(Pommes(self.largeur, self.hauteur, self.taille_case))

    def remove_pomme(self, pomme):
        self.pommes_list.remove(pomme)

    def add_pomme(self):
        self.pommes_list.append(Pommes(self.largeur, self.hauteur, self.taille_case))


class Pieges():
    def __init__(self, largeur, hauteur, taille_case):
        self.largeur = largeur
        self.hauteur = hauteur
        self.taille_case = taille_case
        self.pieges_list = []
        self.x = round(random.randrange(0, self.largeur - self.taille_case)/self.taille_case)*self.taille_case
        self.y = round(random.randrange(0, self.hauteur - self.taille_case)/self.taille_case)*self.taille_case  

    def add_piege(self):
        self.pieges_list.append(Pieges(self.largeur, self.hauteur, self.taille_case))

    def supprimer_piege(self,piege):
        for i in range(len(self.pieges_list)-1):
            if self.pieges_list[i].x == piege.x and self.pieges_list[i].y == piege.y:
                del(self.pieges_list[i]) 

class jouer():
    black = (0,0,0)
    red = (200, 0, 0)
    green = (0, 200, 0)
    white = (240, 240, 240)
    grey = (20, 20, 20)
    
    colors = [(255, 110, 0), (255, 165, 0), (255, 195, 0), (255, 225, 0), (255, 255, 0), (170, 213, 0), (85, 170, 0), (0, 128, 0), (0, 85, 85), (0, 43, 170), (0, 0, 255), (25, 0, 213), (50, 0, 172), (75, 0, 130), (129, 43, 166), (184, 87, 202), (208, 58, 135), (231, 29, 67), (255, 0, 0), (255, 55, 0), (255, 110, 0), (255, 165, 0), (255, 195, 0), (255, 225, 0), (255, 255, 0), (170, 213, 0), (85, 170, 0), (0, 128, 0), (0, 85, 85), (0, 43, 170), (0, 0, 255), (25, 0, 213), (50, 0, 172), (75, 0, 130), (129, 43, 166), (184, 87, 202), (208, 58, 135), (231, 29, 67), (255, 0, 0), (255, 55, 0), (255, 110, 0), (255, 165, 0), (255, 195, 0), (255, 225, 0), (255, 255, 0), (170, 213, 0), (85, 170, 0), (0, 128, 0), (0, 85, 85), (0, 43, 170), (0, 0, 255), (25, 0, 213), (50, 0, 172), (75, 0, 130), (129, 43, 166), (184, 87, 202), (208, 58, 135), (231, 29, 67), (255, 0, 0), (255, 55, 0), (255, 110, 0), (255, 165, 0), (255, 195, 0), (255, 225, 0), (255, 255, 0), (170, 213, 0), (85, 170, 0), (0, 128, 0), (0, 85, 85), (0, 43, 170), (0, 0, 255), (25, 0, 213), (50, 0, 172), (75, 0, 130), (129, 43, 166), (184, 87, 202), (208, 58, 135)]

    def __init__(self, largeur, hauteur, taille_case):
        pygame.init()
        self.running = True
        self.endgame = False
        self.pregame = True
        self.largeur = largeur
        self.hauteur = hauteur
        self.taille_case = taille_case
        self.display = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption('Snake python')
        
        self.clock = pygame.time.Clock()
        self.snakespeed = 8
        self.time = 1
        
        self.snake = snake(self.display, self.taille_case)
        self.pommes = Pommes(self.largeur, self.hauteur, self.taille_case)

        self.gamemode = 'normal'

    def game_loop(self):
        while self.running == True:
            if self.pregame == True:
                while self.pregame == True:
                    self.display.fill(self.black)
                    self.message('Bienvenue au Snake ! Choisir la difficulté :', self.largeur/2, 80)
                    self.message('A- Normal', self.largeur/2, (self.hauteur/2 - 64)) 
                    self.message('B- Snake plus rapide', self.largeur/2, (self.hauteur/2)) 
                    self.message('C- Une seule pomme', self.largeur/2, (self.hauteur/2 + 64)) 
                    self.message('D- Pieges aléatoires', self.largeur/2, (self.hauteur/2 + 128)) 
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_a:
                                self.pregame = False 
                            if event.key == pygame.K_b:
                                self.pregame = False 
                                self.gamemode = 'rapide'
                            if event.key == pygame.K_c:
                                self.pregame = False 
                                self.gamemode = 'une pomme'
                            if event.key == pygame.K_d:
                                self.pregame = False 
                                self.gamemode = 'pieges'
                                self.pieges = Pieges(self.largeur, self.hauteur, self.taille_case)
                if self.gamemode == 'une pomme':
                    self.pommes.spawn_pommes()
                else:
                    for i in range(3):
                        self.pommes.spawn_pommes()
            if self.gamemode == 'rapide':
                self.snakespeed = 20
            elif self.gamemode == 'pieges':
                nb = random.randint(0, 30)
                if nb == 3:
                    self.pieges.add_piege()
                for piege in self.pieges.pieges_list:
                    for pomme in self.pommes.pommes_list:
                        if pomme.x == piege.x and pomme.y == piege.y:
                            self.pieges.supprimer_piege(piege)


            if self.endgame == True:
                while self.endgame == True:
                    self.display.fill(self.red)
                    self.message('Tu as PERDU haha !', self.largeur/2, (self.hauteur/2 - 64))  
                    self.message('R pour une renvenche, Q pour ragequit', self.largeur/2, self.hauteur/2)
                    self.scoremessage = ('Ton score : ') + self.printscore
                    self.message(self.scoremessage, self.largeur/2, (self.hauteur/2 + 64))       
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                main()
                            if event.key == pygame.K_q:
                                self.running = False
                                pygame.quit()
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if self.snake.direction != 'gauche':
                            self.snake.droite()
                    if event.key == pygame.K_LEFT:
                        if self.snake.direction != 'droite':
                            self.snake.gauche()
                    if event.key == pygame.K_UP:
                        if self.snake.direction != 'bas':
                            self.snake.haut()
                    if event.key == pygame.K_DOWN:
                        if self.snake.direction != 'haut':
                            self.snake.bas()
                    if event.key == pygame.K_q:
                        self.running = False
                        pygame.quit()
            
            if self.snake.bouger() == False:
                self.endgame = True
            
            if self.murcollision() == True:
                self.endgame = True
            
            pomme = self.pommecollision()
            if pomme != False:
                self.snake.grossir()
                self.pommes.add_pomme()
                self.pommes.remove_pomme(pomme)
                
            self.display.fill(self.black)
            self.drawfond()
            
            self.printscore = str(self.score())
            self.message('Score : ' + self.printscore, 100, 32)
            self.message('Temps : ' + str(round(self.time/self.snakespeed)), 700, 32)
            
            if self.gamemode == 'pieges':
                self.drawpiege(self.pieges)
            self.drawpomme(self.pommes)
            self.drawsnake(self.snake)
            
            pygame.display.flip()
            self.clock.tick(self.snakespeed) 
            self.time += 1        
            
    def drawsnake(self, snake):
        i=0
        for segment in self.snake.snakelist:
            pygame.draw.rect(self.display, self.colors[i], (segment[0], segment[1], snake.taille_case, snake.taille_case))
            i+=1
    
    def drawpomme(self, pomme):
        for pomme in self.pommes.pommes_list:
            pygame.draw.circle(self.display, self.red, (pomme.x+pomme.taille_case/2, pomme.y+pomme.taille_case/2), pomme.taille_case/2)

    def drawpiege(self, piege):
        for piege in self.pieges.pieges_list:
            pygame.draw.rect(self.display, self.white, (piege.x, piege.y, piege.taille_case, piege.taille_case))

    def drawfond(self):
        for i in range(0, self.largeur, self.taille_case):
            for j in range(0, self.hauteur, self.taille_case):
                if (i+j) %(self.taille_case*2) == 0:
                    pygame.draw.rect(self.display, self.grey, (i, j, self.taille_case, self.taille_case))


    def murcollision(self):
        if self.snake.x < 0 or self.snake.y < 0 or self.snake.x > self.largeur - self.taille_case or self.snake.y > self.hauteur - self.taille_case:
            return True
        if self.gamemode == 'pieges':
            for piege in self.pieges.pieges_list: 
                if self.snake.x == piege.x and self.snake.y == piege.y:
                    return True
        return False
    
    def pommecollision(self):
        for pomme in self.pommes.pommes_list: 
            if self.snake.x == pomme.x and self.snake.y == pomme.y:
                return pomme
        return False
     
    def message(self, message, x, y):
        self.font = pygame.font.SysFont('bahnschrift', 32)
        self.text = self.font.render(message, True, self.green)
        self.textRect = self.text.get_rect()
        self.textRect.center = (x,y)
        self.display.blit(self.text, self.textRect)

    def score(self):
        counter = -3
        for i in range(self.snake.taille_serpent):
            counter += 1
        return counter


def main():
    playgame = jouer(800, 800, 40)
    playgame.game_loop()
    
    
main()