import pygame.font


class Button():

    def __init__(self, screen, msg):

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 600, 720
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.intro_logo = pygame.image.load('images2/pacmanLogo.png')
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):

        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        self.screen.blit(self.intro_logo, (110, 250))

    def draw_button(self):

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.intro_logo, (110, 150))
