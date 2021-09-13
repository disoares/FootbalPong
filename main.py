import pygame

pygame.init()

window = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("Football Pong")

win = pygame.image.load("assets/win.png")

score1 = 0
score1_image = pygame.image.load("assets/score/0.png")
score2 = 0
score2_image = pygame.image.load("assets/score/0.png")

field = pygame.image.load("assets/field.png")

player1 = pygame.image.load("assets/player1.png")
player1_y = 290
player1_moveup = False
player1_movedown = False

player2 = pygame.image.load("assets/player2.png")
player2_y = 290

ball = pygame.image.load("assets/ball.png")
ball_x = 617
ball_y = 337
ball_dir = -6
ball_dir_y = 1


def player_move():
    global player1_y

    if player1_moveup and player1_y > 0:
        player1_y -= 10

    if player1_movedown and player1_y < 575:
        player1_y += 10


def player2_move():
    global player2_y
    player2_y = ball_y


def move_ball():
    global ball_x
    global ball_y
    global ball_dir
    global ball_dir_y
    global score1
    global score1_image
    global score2
    global score2_image

    ball_x += ball_dir
    ball_y += ball_dir_y

    if ball_x < 120:
        if player1_y < ball_y + 23 and player1_y + 146 > ball_y:
            ball_dir *= -1
            ball_dir += 2

    if ball_x > 1100:
        if player2_y < ball_y + 23 and player2_y + 146 > ball_y:
            ball_dir *= -1
            ball_dir -= 2

    if ball_y > 670:
        ball_dir_y *= -1
    elif ball_y < 0:
        ball_dir_y *= -1

    if ball_x < -50:
        ball_x = 617
        ball_y = 337
        ball_dir *= -1
        ball_dir_y *= -1
        score2 += 1
        score2_image = pygame.image.load(f"assets/score/{score2}.png")
        ball_dir = -6

    elif ball_x > 1320:
        ball_x = 617
        ball_y = 337
        ball_dir *= -1
        ball_dir_y *= -1
        score1 += 1
        score1_image = pygame.image.load(f"assets/score/{score1}.png")
        ball_dir = -6


def draw():
    if score1 or score2 < 9:
        window.blit(field, (0, 0))
        window.blit(player1, (50, player1_y))
        window.blit(player2, (1150, player2_y))
        window.blit(ball, (ball_x, ball_y))
        window.blit(score1_image, (500, 50))
        window.blit(score2_image, (710, 50))
        move_ball()
        player_move()
        player2_move()
    else:
        window.blit(win, (300, 330))


loop = True
while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player1_moveup = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player1_movedown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player1_moveup = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player1_movedown = False

    draw()
    pygame.display.update()