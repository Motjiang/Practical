import pygame

class Ship:
    def __int__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/shiip.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen.rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)    

