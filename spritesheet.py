import pygame

class Spritesheet:
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image

class Sprite:
    def __init__(self, anims, current_anim, fps, frame):
        self.anims = anims
        self.current_anim = current_anim
        self.fps = fps
        self.frame = frame
        self.timer = 0

    def animate(self):
        if self.timer >= (60 / self.fps):
            pass
        self.timer += 1
