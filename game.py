import pygame
import pytmx
import pyscroll
from player import Player
import Data.settings.setting as setting
import Data.data as data


class Game:
    def __init__(self):
        
        # creer la fenetre du jeu 
        self.screen = pygame.display.set_mode((data.display_x, data.display_y))
        pygame.display.set_caption(data.game_name)   


        # charger la carte
        tmx_data = pytmx.util_pygame.load_pygame('tiled/map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # generer un joueur
        player_position = tmx_data.get_object_by_name('player')
        self.player = Player(player_position.x, player_position.y)

        # dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)

    def move(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()
        if pressed[pygame.K_RIGHT]:
            self.player.move_right()
        if pressed[pygame.K_DOWN]:
            self.player.move_down()
        if pressed[pygame.K_LEFT]:
            self.player.move_left()
    def run(self):

        clock = pygame.time.Clock()

        # boucle du jeu 
        running = True


        while running:

            self.group.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            self.move()
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(setting.FPS)

        pygame.quit()