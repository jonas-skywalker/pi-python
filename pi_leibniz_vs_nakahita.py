import pygame
import time
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
size = 500, 500
my_font = pygame.font.Font(None, 40)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pi-Leibniz approximation")
screen.fill(white)

_pi_leib_ = 0
_i_ = 1
_j_ = 1

_pi_nak_ = 3
_a_ = 2
_b_ = 3
_c_ = 4


def pi_leibniz(i, j, pi):
    if j % 2 == 0:
        pi -= (4/i)
    else:
        pi += (4/i)
    return pi


def pi_nakahita(a, b, c, j, pi):
    if j % 2 == 0:
        pi -= (4/(a * b * c))
    else:
        pi += (4/(a * b * c))
    return pi


while True:
    # function for Pygame updating the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    _pi_leib_ = pi_leibniz(_i_, _j_, _pi_leib_)
    _pi_nak_ = pi_nakahita(_a_, _b_, _c_, _j_, _pi_nak_)

    screen.fill(white)
    label = my_font.render(str(_pi_leib_), 0, black)
    screen.blit(label, ((size[0]/2)-125, size[1]/2))
    label2 = my_font.render(str(_pi_nak_), 0, black)
    screen.blit(label2, ((size[0] / 2) - 125, (size[1] / 2) - 50))

    _i_ += 2
    _j_ += 1

    _a_ += 2
    _b_ += 2
    _c_ += 2

    pygame.display.update()
