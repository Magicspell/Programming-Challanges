import pygame
from PIL import Image, ImageFilter
import colorsys
import zlib


im = Image.open(input('Which image? '))

pix = im.load()
width, height = im.size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Image Compression')

def get_2x2(i):
    for w in range(width):
        for h in range(height):
            if w == i and h == i:
                pixel1 = pix[w,h]
            if w == i+1 and h == i:
                pixel2 = pix[w,h]
            if w == i and h == i+1:
                pixel3 = pix[w,h]
            if w == i+1 and h == i+1:
                pixel4 = pix[w,h]
    return pixel1, pixel2, pixel3, pixel4

def avg_2x2(coords):
    pixels = get_2x2(coords)
    hsv1 = colorsys.rgb_to_hsv(pixels[0][0], pixels[0][1], pixels[0][2])
    hsv2 = colorsys.rgb_to_hsv(pixels[1][0], pixels[1][1], pixels[1][2])
    hsv3 = colorsys.rgb_to_hsv(pixels[2][0], pixels[2][1], pixels[2][2])
    hsv4 = colorsys.rgb_to_hsv(pixels[3][0], pixels[3][1], pixels[3][2])
    newhue = (hsv1[0]+hsv2[0]+hsv3[0]+hsv4[0])/4
    rgb1 = colorsys.hsv_to_rgb(newhue,hsv1[1],hsv1[2])
    rgb2 = colorsys.hsv_to_rgb(newhue,hsv2[1],hsv2[2])
    rgb3 = colorsys.hsv_to_rgb(newhue,hsv3[1],hsv3[2])
    rgb4 = colorsys.hsv_to_rgb(newhue,hsv4[1],hsv4[2])
    print(hsv1, hsv2, hsv3, hsv4)
    return rgb1, rgb2, rgb3, rgb4

def grayscale():
    for w in range(width):
        for h in range(height):
            hsv1 = colorsys.rgb_to_hsv(pix[w,h][0], pix[w,h][1], pix[w,h][2])
            rgb1 = colorsys.hsv_to_rgb(0,0,hsv1[2])
            screen.set_at((w, h), rgb1)

def blurred(size):
    blurImage = im.filter(ImageFilter.BoxBlur(size))
    blurpix = blurImage.load()
    f = open('bytes.txt','wb')
    pix_bytes = bytearray(0)
    for w in range(width):
        for h in range(height):
            hsv1 = colorsys.rgb_to_hsv(pix[w,h][0], pix[w,h][1], pix[w,h][2])
            blurhsv = colorsys.rgb_to_hsv(blurpix[w,h][0], blurpix[w,h][1], blurpix[w,h][2])
            rgb1 = colorsys.hsv_to_rgb(round(blurhsv[0], 5), round(blurhsv[1], 5), round(hsv1[2], 5))
            # pix_byte = hsv1[2].to_bytes(2, byteorder='little')
            pix_bytes.append(hsv1[2])
            # pix_bytes = zlib.compress(pix_bytes)
            # print(pix_bytes)
            # print(int.from_bytes(pix_bytes, 'little'))
            screen.set_at((w, h), rgb1)
    
    f.write(zlib.compress(pix_bytes))
    # f.write(pix_bytes)
    f.close()

# i = 0
# for pixel in get_2x2(0):
#     print(pixel)
#     rect = pygame.Rect((i*30,0), (30,40))
#     pygame.draw.rect(screen, pixel, rect)
#     i += 1
# i = 0
# for pixel in avg_2x2(0):
#     rect = pygame.Rect((i*30,40), (30,40))
#     pygame.draw.rect(screen, pixel, rect)
#     i += 1

size = 0
blurred(size)
print(size)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 4:
                size += 10
                blurred(size)
                print(size)
                pygame.display.flip()
            if event.button == 5:
                size -= 10
                if size <0:
                    size = 0
                blurred(size)
                print(size)
                pygame.display.flip()
