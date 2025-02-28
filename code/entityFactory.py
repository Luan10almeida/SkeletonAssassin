#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str , position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(8):
                    list_bg.append(Background(f'Level1Bg{i}', position(0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', position(WIN_WIDTH, 0)))
                return list_bg
            #case '0_Skeleton_Crusader_Running_000':
                #return Player('0_Skeleton_Crusader_Running_000'), (10, WIN_HEIGHT / 2 ))
