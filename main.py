import pygame,time
from pygame.locals import *
import random
from circle_info import CircleInfo

pygame.init()
pygame.font.init()

font = pygame.font.SysFont("Helvetica",20)
size = (width,height) = (500,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

done = False
is_stopped = False
has_adjusted_points = False
stop_cooldown = 30
stop_timer = 0
points = 0

WHITE = (255,255,255)
ORANGE = (245,179,66)
BLUE = (76,234,237)
RED = (255,0,0)

def is_touching_color(surface,rect,check_color):


    for x in range(rect.left,rect.right):
        for y in range(rect.top,rect.bottom):
            if not (x <= 0 or y <= 0 or x >= width or y >= height):


                color = screen.get_at((x, y))

                surface_x = x - rect.left
                surface_y = y - rect.top

                has_color_at_point = surface.get_at((surface_x,surface_y)) != surface.get_at((0,0))
                if has_color_at_point and color == check_color:
                    return True
    return False

def randomize_rect(some_rect):
    some_rect.center = (
        random.randint(some_rect.width // 2, width - some_rect.width // 2),
        random.randint(some_rect.height // 2, height - some_rect.height // 2))
    return some_rect

def main():
    global done,is_stopped,stop_cooldown,stop_timer,points,has_adjusted_points
    circle_info_group = []
    color = "blue"
    for i in range(10):
        if random.randint(0,1) == 0:
            color = "orange"
        else:
            color = "blue"
        circle_info_group.append(CircleInfo(color))

    scratchy = pygame.image.load("scratchy1.png")
    scratchy.set_colorkey(scratchy.get_at((0,0)))
    scratchy_rect = scratchy.get_rect()

    text = font.render("Moving...", True, RED)
    text_rect = text.get_rect()
    text_rect.center = (width//2,50)

    points_text = font.render("Points: {}".format(points), True, RED)
    points_text_rect = points_text.get_rect()
    points_text_rect.center = (width//2,height-50)

    while not done:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()


        keys = pygame.key.get_pressed()
        if not is_stopped and keys[K_SPACE]:
            is_stopped = True
            has_adjusted_points = False

        if is_stopped:
            stop_timer += 0.5
            if stop_timer > stop_cooldown:
                is_stopped = False
                stop_timer = 0
                text = font.render("Moving...", True, RED)

        #For testing purposes only
        # scratchy_rect.center = pygame.mouse.get_pos()

        if not is_stopped and pygame.time.get_ticks()//10 % 10 == 0:
             scratchy_rect = randomize_rect(pygame.Rect(scratchy_rect))

        if is_stopped and not has_adjusted_points:
            if is_touching_color(scratchy,scratchy_rect,BLUE):
                print("Touching blue")
                text = font.render("Touching BLUE", True, RED)
                points += 5
                has_adjusted_points = True
            elif is_touching_color(scratchy,scratchy_rect,ORANGE):
                print("Touching orange")
                text = font.render("Touching ORANGE", True, RED)
                points -= 1
                has_adjusted_points = True
            else:
                print("Not touching a color")
                text = font.render("Not touching a color", True, RED)

        points_text = font.render("Points: {}".format(points), True, RED)
        screen.fill(WHITE)
        for circle_info in circle_info_group:
            pygame.draw.circle(screen, circle_info.color, circle_info.center, circle_info.radius)

        screen.blit(scratchy,scratchy_rect)
        screen.blit(text,text_rect)
        screen.blit(points_text,points_text_rect)
        pygame.display.flip()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
