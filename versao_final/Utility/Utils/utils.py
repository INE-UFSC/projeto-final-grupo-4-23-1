import os
import pygame
#retorna o caminho para a pasta assets
def get_assets_path(file_path):
    current_path = os.path.dirname(file_path).split('\\')
    return '\\'.join(current_path[0:current_path.index('States')]) + '\\assets'

