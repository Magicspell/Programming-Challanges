import pygame
from PIL import Image

multiplyer = 4
im = Image.open('Zemmaemoji.png')
pix = im.load()
width, height = im.size
screen = pygame.display.set_mode((width*multiplyer, height*multiplyer))
pygame.display.set_caption('IDK')

def draw_pixels(size, separation):
    drawing_pixel = 0
    for w in range(width*multiplyer):
        for h in range(height*multiplyer):
            if drawing_pixel == separation:
                pygame.draw.circle(screen, pix[w/multiplyer,h/multiplyer], (w, h), size)
                # screen.set_at((w, h), pix[w/multiplyer,h/multiplyer])
                drawing_pixel=0
            else:
                drawing_pixel += 1
    pygame.display.flip()


running = True
size = 8
sep = 100
draw_pixels(size, sep)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 4:
                size += 1
                sep += width/2
                draw_pixels(size, sep)
            if event.button == 5:
                size -= 1
                sep -= width/2
                if sep <= 0:
                    sep = 0
                draw_pixels(size, sep)