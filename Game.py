import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# GameObject is the parent class for the player, background, and treasure object
class GameObject:

    def __init__(self, image_file, x, y, width, height):
        object_image = pygame.image.load(image_file)
        # Scale image up
        self.image = pygame.transform.scale(object_image, (width, height))
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

    def draw(self, background):
        # 'Blit' the image on the background, at the position in the tuple
        background.blit(self.image, (self.x_pos, self.y_pos))


#
class Players(GameObject):
    SPEED = 10

    def __init__(self, image_file, x, y, width, height):
        super().__init__(image_file, x, y, width, height)

    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= Player.SPEED
        elif direction < 0:
            self.y_pos += Player.SPEED
        # Lower Screen Limit
        if self.y_pos >= max_height - 50:
            self.y_pos = max_height - 50
        # Upper Screen Limit
        elif self.y_pos <= 20:
            self.y_pos = 20
    
    def detect_collision(self, other_body: GameObject):
        # Return false if player is above or below the enemy (since we can't ever hit them)
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        
        # Return false if player is too far to the right or left of enemy
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.height < other_body.x_pos:
            return False
        
        # If every check passes, then there must be collision
        return True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
