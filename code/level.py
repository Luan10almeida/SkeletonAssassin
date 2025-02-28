#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list [Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('0_Skeleton_Crusader_Running_000'))
        self.timeout = 20000


    def run(self, ):
      #  pygame.mixer_music.load(f'./asset/{self.name}mp3') # Carregando musica level 1
        # pygame.mixer_music.play(-1)
        #clock = pygame.time.Clock()


        while True:
            #clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                #ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            pass
