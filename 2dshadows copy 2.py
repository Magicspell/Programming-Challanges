import pygame

(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Shadows')
mainclock = pygame.time.Clock()

screen.fill((255,255,255))
pygame.display.flip()

obsticals = [(100,100,100), (300, 400, 50), (700, 400, 10)]

rays = []

class Ray():
    def __init__(self, endpoint, collided_obstical):
        self.endpoint = endpoint
        self.collided_obstical = collided_obstical

def draw_obsticals():
    for obstical in obsticals:
        x = obstical[0]
        y = obstical[1]
        r = obstical[2]
        rect = pygame.Rect(x-r, y-r, r*2, r*2)
        pygame.draw.rect(screen, (200,200,200), rect)

def raycast(x, y):
    ray = Ray((x,y), None)
    m_x = pygame.mouse.get_pos()[0]
    m_y = pygame.mouse.get_pos()[1]
    run = x - m_x
    rise = y - m_y
    run /= 300
    rise /= 300
    prev_x = m_x
    prev_y = m_y
    hit = False
    prev_hit = False
    for i in range(300):
        for obstical in obsticals:
            #Find obstical eges
            other_max_x = obstical[0] + obstical[2]
            other_min_x = obstical[0] - obstical[2]
            other_max_y = obstical[1] + obstical[2]
            other_min_y = obstical[1] - obstical[2]
            
            #Determine if touching obstical
            touching_x = prev_x > other_min_x and prev_x < other_max_x
            touching_y = prev_y > other_min_y and prev_y < other_max_y
            if touching_x and touching_y:
                hit = True

            #Draw segment
            elif not hit:
                pygame.draw.line(screen, (0,0,0), (prev_x, prev_y), (prev_x + run, prev_y + rise))

            #If it hits an obstical
            if not prev_hit and hit:
                pygame.draw.circle(screen, (0,0,255), (prev_x, prev_y), 4)
                ray.endpoint = (prev_x, prev_y)
                ray.collided_obstical = obstical
                return
            prev_hit = hit
        error_margin = 10

        #If it hits the edge of the screen
        if prev_y < (y + error_margin) and prev_x < (x + error_margin) and not hit:
            pygame.draw.circle(screen, (0,0,255), (x, y), 4)
            ray.endpoint = (prev_x, prev_y)
            ray.collided_obstical = None
        prev_x += run
        prev_y += rise
        prev_x = round(prev_x, 3)
        prev_y = round(prev_y, 3)
    rays.append(ray)


line_space = 50

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    draw_obsticals()
    w = 0
    h = 0
    rays = []
    raycast(203,0)
    raycast(260,0)
    raycast(0,240)
    raycast(0,270)
    # while w < width - line_space:
    #     w += line_space
    #     raycast(w,0)
    #     raycast(w,height)
    #     # counter += 1
    #     print(counter)
    # while h < height - line_space:
    #     h += line_space
    #     raycast(0,h)
    #     raycast(width,h)
    #     # counter += 1
    #     print(counter)
    # for shadow in shadows:
    #     shadow.draw()
    prev_obstical = True
    i = 0
    start_point = 0
    end_point = 0
    for ray in rays:
        if (not prev_obstical) and ray.collided_obstical:
            start_point = i - 1
            print(f'Found starting point: {start_point}')
        if prev_obstical and not ray.collided_obstical:
            print(f'Found ending point: {end_point}')
            end_point = i
            pygame.draw.circle(screen, (255,0,0), rays[end_point].endpoint, 5)
            pygame.draw.circle(screen, (0,255,0), rays[start_point].endpoint, 5)
        if ray.collided_obstical == None:
            prev_obstical = False
        else:
            prev_obstical = True
        i += 1

    pygame.display.flip()
    mainclock.tick(60)