import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс представляющий одного прищельца"""

    def __init__(self, ai_settings, screen):
        """"Иницилизирует прищельца и задает начальную позицию"""
        super(Alien, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        # Загрузка изображения и назначение атрибута rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый прищелец появляется в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Сохранение точной позиции прищельца
        self.x = float(self.rect.x)

    def blitme(self):
        """"Выводит прищельца в текущем положении"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Возвращает True, если прищелец у края"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """"Перемещает прищельца вправо и влево"""
        self.x += (self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x = self.x

