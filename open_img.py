import pygame
from PIL import Image
import colorsys
import zlib

f = open(input('Which file? '),'rb').read()
decompressed = zlib.decompress(f, wbits=0)
ints = int.from_bytes(decompressed, 'little')
print(ints)

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False