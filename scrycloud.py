import pygame
import os
import logging

# Set up logging
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Pygame
pygame.init()

# Screen settings
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("TekMajik: ScryCloud")

# Frame rate settings
clock = pygame.time.Clock()
fps = 60  # Set a high frame rate

# Variables
ghost_fx_delay = 0.5
music_volume = 0.5
sigil_brightness = 1.0
show_controls = False

# CloudSprite Class
class CloudSprite(pygame.sprite.Sprite):
    def __init__(self, image_files):
        super().__init__()
        self.images = [pygame.image.load(img).convert_alpha() for img in image_files]
        self.current_image = 0
        self.next_image = (self.current_image + 1) % len(self.images)
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect()
        self.transition_counter = 0
        self.transition_delay = int(ghost_fx_delay * fps)
        self.alpha_value = 255  # Start with full opacity for blending

    def update(self):
        self.transition_counter += 1
        if self.transition_counter >= self.transition_delay:
            self.transition_counter = 0
            self.current_image = self.next_image
            self.next_image = (self.current_image + 1) % len(self.images)
            self.alpha_value = 0  # Reset alpha for new transition

    def blend_update(self):
        if self.alpha_value < 255:
            self.alpha_value += 5  # Adjust this value for faster/slower blending
            if self.alpha_value >= 255:
                self.alpha_value = 255  # Finalize the blend

            # Blend the current image with the next image
            current_img = self.images[self.current_image].copy()
            next_img = self.images[self.next_image].copy()
            next_img.set_alpha(self.alpha_value)
            current_img.blit(next_img, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)
            self.image = current_img

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

# Load resources with error handling
try:
    sigil_image = pygame.image.load('sc_img/sigil.png').convert_alpha()
except pygame.error as e:
    print(f"Error loading sigil image: {e}")
    pygame.quit()
    exit()

try:
    music = pygame.mixer.Sound('sc_img/music.wav')
except pygame.error as e:
    print(f"Error loading music: {e}")
    pygame.quit()
    exit()

# Initialize cloud sprites
cloud1_images = [f'sc_img/cloud1_costume{i}.png' for i in range(1, 8)]
cloud2_images = [f'sc_img/cloud2_costume{i}.png' for i in range(1, 8)]
cloud3_images = [f'sc_img/cloud3_costume{i}.png' for i in range(1, 8)]

# Check if files exist before creating sprites
for img in cloud1_images + cloud2_images + cloud3_images:
    if not os.path.isfile(img):
        print(f"Missing file: {img}")
        pygame.quit()
        exit()

cloud1 = CloudSprite(cloud1_images)
cloud2 = CloudSprite(cloud2_images)
cloud3 = CloudSprite(cloud3_images)

all_clouds = pygame.sprite.Group(cloud1, cloud2, cloud3)

# Play music
music.set_volume(music_volume)
music.play(-1)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                show_controls = not show_controls

    # Update cloud effects
    for cloud in all_clouds:
        cloud.update()
        cloud.blend_update()

    # Draw everything
    screen.fill((0, 0, 0))  # Clear screen
    
    # Sigil with brightness control
    sigil = pygame.transform.rotozoom(sigil_image, 0, sigil_brightness)
    sigil_rect = sigil.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(sigil, sigil_rect.topleft)  # Draw sigil centered

    # Draw clouds on top of the sigil with blending
    for cloud in all_clouds:
        cloud.draw(screen)

    if show_controls:
        # Draw controls here (like sliders)
        pass

    pygame.display.flip()
    clock.tick(fps)  # Control the frame rate

pygame.quit()
