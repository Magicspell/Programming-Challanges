import pygame
import colorsys



(width, height) = (1280, 720)
# screen = pygame.display.set_mode((width, height))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('IDK')

i = 1
running = True
points = []
color = 0
while running:
  ev = pygame.event.get()
  for event in ev:
    if pygame.key.get_pressed()[pygame.KMOD_LSHIFT]:
        print('test')
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 3:
            i += 1
            pos = pygame.mouse.get_pos()
            rgb = colorsys.hsv_to_rgb(color, 1, (i/10)%1)
            newtuple = (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
            rect = pygame.Rect((0,0), (30,40))
            pygame.draw.rect(screen, newtuple, rect)
            pygame.display.flip()
        if event.button == 4:

            color += 0.03
            color %= 360
            rgb = colorsys.hsv_to_rgb(color, 1, 1)
            newtuple = (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
            rect = pygame.Rect((0,0), (30,40))
            pygame.draw.rect(screen, newtuple, rect)
            pygame.display.flip()
        if event.button == 5:
            color -= 0.03
            if color <= 0:
                color = 360
            rgb = colorsys.hsv_to_rgb(color, 1, 1)
            newtuple = (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
            rect = pygame.Rect((0,0), (30,40))
            pygame.draw.rect(screen, newtuple, rect)
            pygame.display.flip()
        # if len(points) == 3:
        #     print(points)
        #     pygame.draw.polygon(screen, (255,0,0), points)
        #     pygame.display.flip()
        #     points = []
        # else:
        #     points.append(pos)
    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        rgb = colorsys.hsv_to_rgb(color, 1, (i/10)%1)
        newtuple = (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
        pygame.draw.circle(screen, newtuple, pos, 18)
        pygame.display.flip()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False