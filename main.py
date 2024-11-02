import pygame
import os
import random
import math
import sys
import neat
from settings import *

pygame.init()

best_scores_per_generation = [0] 

class Agent:

    X_POS = 80
    Y_POS = 430
    JUMP_VEL = 9
    MAX_JUMP_HEIGHT = 130 
    

    def __init__(self, img=AGENT_IMG):
        self.image = img
        self.agent_run = True
        self.agent_jump = False
        self.jump_vel = self.JUMP_VEL
        self.rect = pygame.Rect(self.X_POS, self.Y_POS, img.get_width(), img.get_height())
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.step_index = 0
        self.score = 0
        self.best_score = 0
        self.projectiles = []
        self.last_fire_points = 0

    def fire(self, current_points):

        if current_points - self.last_fire_points >= 500:

            projectile = Projectile(self.rect.right, self.rect.centery, FIRE)
            self.projectiles.append(projectile)
            self.last_fire_points = current_points

    def update_projectiles(self):

        for projectile in self.projectiles[:]:
            projectile.update()

            if projectile.rect.x > SCREEN_WIDTH:
                self.projectiles.remove(projectile)

    def draw_projectiles(self, SCREEN):
        
        for projectile in self.projectiles:
            projectile.draw(SCREEN)
    
    def update_score(self): 
        self.score += 1
        if self.score > self.best_score:
            self.best_score = self.score 

    def update(self):
        if self.agent_run:
            self.run()
        if self.agent_jump:
            self.jump()
        if self.step_index >= 10:
            self.step_index = 0

        self.update_projectiles()

    def jump(self):
        if self.agent_jump:
            if self.rect.y > self.MAX_JUMP_HEIGHT:  
                self.rect.y -= self.jump_vel * 4
                self.jump_vel -= 0.8
            else: 
                self.jump_vel = -self.JUMP_VEL

        if self.jump_vel <= -self.JUMP_VEL:
            self.agent_jump = False
            self.agent_run = True
            self.jump_vel = self.JUMP_VEL

    def run(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index += 1

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))
        
        #pygame.draw.rect(SCREEN, self.color, (self.rect.x, self.rect.y, self.rect.width, self.rect.height), 2)
        #for obstacle in obstacles:
            #pygame.draw.line(SCREEN, self.color, (self.rect.x + 54, self.rect.y + 12), obstacle.rect.center, 2)
        self.draw_projectiles(SCREEN)


class Obstacle:
    def __init__(self, image, number_of_obstacle):
        self.image = image
        self.type = number_of_obstacle
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect)

class EnemySmall(Obstacle):
    def __init__(self, image, number_of_obstacle):
        super().__init__(image, number_of_obstacle)
        self.rect.y = 490

class EnemyAirSmall(Obstacle):  
    def __init__(self, image, number_of_obstacle):
        super().__init__(image, number_of_obstacle)
        positions = [400, 415, 450, 480]
        self.rect.y = random.choice(positions)

class EnemyLarge(Obstacle):
    def __init__(self, image, number_of_obstacle):
        super().__init__(image, number_of_obstacle)
        self.rect.y = 430

class EnemyBoss(Obstacle):
    def __init__(self, image, number_of_obstacle):
        super().__init__(image, number_of_obstacle)
        self.rect.y = 47
        
class Projectile:

    WIDTH = 20
    HEIGHT = 10
    COLOR = (255, 0, 0)

    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        self.rect.x += 15

    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect)
      

def remove(index):
    agents.pop(index)
    list_genomes.pop(index)
    nets.pop(index)

def distance(pos_a, pos_b):
    dx = pos_a[0] - pos_b[0]
    dy = pos_a[1] - pos_b[1]
    return math.sqrt(dx**2 + dy**2)

def evaluate_genomes(genomes, config):
    global game_speed, obstacles, agents, list_genomes, nets, points
    clock = pygame.time.Clock()
    points = 0
    nets, agents, obstacles, list_genomes = [], [], [], []
    original_game_speed = 20
    game_speed = original_game_speed

    for _, genome in genomes:

        
        agents.append(Agent())
        
        list_genomes.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0

    def score():
        global points, game_speed
        points += 1
        for agent in agents:
            best_scores_per_generation.append(agent.best_score)
            agent.update_score()

        if points % 1000 == 0:
            obstacles.clear()
            obstacles.append(EnemyBoss(pygame.transform.scale(pygame.image.load(os.path.join("assets/", "susanoo.png")), (ENEMY_WIDTH_BOSS, ENEMY_HEIGHT_BOSS)), random.randint(0, 1)))
            


        if points % 200 == 0 and game_speed <= 50:
            game_speed += 1

       
        text = FONT.render(f'Pontos: {str(points)}', True, (0, 0, 0))  
        SCREEN.blit(text, (950, 50))

    def statistics():
        text_1 = FONT.render(f'Sobreviventes: {str(len(agents))}', True, (0, 0, 0))
        text_2 = FONT.render(f'Geração: {population.generation + 1}', True, (0, 0, 0))
        text_3 = FONT.render(f'Velocidade: {str(game_speed)}', True, (0, 0, 0))
        overall_best_score = max(best_scores_per_generation)  
        text_4 = FONT.render(f'Melhor pontuação: {overall_best_score}', True, (0, 0, 0))
        SCREEN.blit(text_1, (50, 80))
        SCREEN.blit(text_2, (50, 100))
        SCREEN.blit(text_3, (50, 120))
        SCREEN.blit(text_4, (50, 140))

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.blit(BACKGROUND,(0,0))

        for i, agent in enumerate(agents):

            agent.update()
            agent.draw(SCREEN)

            list_genomes[i].fitness +=1

            if agent.score > agent.best_score:
                list_genomes[i].fitness += 5

        if len(agents) == 0:
            break
           
        if len(obstacles) == 0:
            rand_int = random.randint(0, 2)
            if rand_int == 0:
                obstacles.append(EnemySmall(ENEMY_SMALL_IMG, random.randint(0, 2)))
            elif rand_int == 1:
                obstacles.append(EnemyLarge(random.choice(ENEMY_LARGE_IMG), random.randint(0, 1)))
            else:
                obstacles.append(EnemyAirSmall(ENEMY_AIR_IMG, random.randint(0, 2)))

        for obstacle in obstacles[:]:
                    
                    obstacle.draw(SCREEN)
                    obstacle.update()

                    for agent in agents:
                        for projectile in agent.projectiles[:]:
                            if projectile.rect.colliderect(obstacle.rect):
                                if obstacle in obstacles:
                                    obstacles.remove(obstacle)
                                if projectile in agent.projectiles:
                                    agent.projectiles.remove(projectile)
                                    
                    #Nada é mais permanente do que uma gambiarra provisória
                    for i in range(len(agents) - 1, -1, -1): 
                        agent = agents[i]
                        output = nets[i].activate((agent.rect.y,
                                                distance((agent.rect.x, agent.rect.y),
                                                obstacle.rect.midtop)))

                        if output[0] > 0.5 and agent.rect.y == agent.Y_POS:
                            agent.agent_jump = True
                            agent.agent_run = False

                        if output[1] > 0.5:
                            agent.fire(points)

                        for obstacle in obstacles:
                            if agent.rect.colliderect(obstacle.rect):
                                list_genomes[i].fitness -= 1
                                remove(i)
                                break


        statistics()
        score()
        clock.tick(30)
        pygame.display.update()


def run(config_path):
    global population
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )
    population = neat.Population(config)
    population.run(evaluate_genomes)



if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = 'config.txt'
    run(config_path)
