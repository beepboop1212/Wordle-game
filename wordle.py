import pygame
import words
import random
pygame.init()

#screen
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
purple = (128, 0, 128)
width = 500
height = 700
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Wordle !")
turn = 0

board = [[" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "]]

fps = 60
timer = pygame.time.Clock()
used_font = pygame.font.Font('freesansbold.ttf', 56)
game_over = False
letter = 0
active_turn = True
wordd = words.Words[random.randint(0, len(words.Words)-1)]

def draw_board():
    global turn
    global board
    for col in range(5): #5letters
        for row in range(6): #6turns
            pygame.draw.rect(screen, white, [col * 100 + 12, row * 100 + 12, 75, 75], 3, 5) #x,y,width,height,hollow(0=solid),rounded
            text_piece = used_font.render(board[row][col], True, purple)
            screen.blit(text_piece, (col * 100 + 33, row * 100 + 25))
    pygame.draw.rect(screen, red, [5, turn * 100 + 5, width - 10, 90], 3, 5)

def check_word():
    global turn
    global board
    global wordd
    for col in range(5): 
        for row in range(6):
            if wordd[col] == board[row][col] and turn > row:
                pygame.draw.rect(screen, green, [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5)
            elif board[row][col] in wordd and turn > row:
                pygame.draw.rect(screen, yellow, [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5)

running = True
while running:
    timer.tick(fps)
    screen.fill(black)
    check_word()
    draw_board()

    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.TEXTINPUT and active_turn and not game_over:
            entry = event.__getattribute__('text')
            if entry != " ":
                board[turn][letter] = entry
                letter += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and letter > 0:
                board[turn][letter-1] = ' '
                letter -= 1
            if event.key == pygame.K_SPACE and not game_over:
                turn += 1
                letter = 0
            if event.key == pygame.K_SPACE and game_over:
                turn = 0
                letter = 0
                game_over = False
                wordd = words.Words[random.randint(0, len(words.Words)-1)]
                board = [[" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "]]

    for row in range(6):
        guess = board[row][0] + board[row][1] + board[row][2] + board[row][3] + board[row][4]
        if guess == wordd and row < turn: #commit to pressing space key
            game_over = True

    if letter == 5:
        active_turn = False
    if letter < 5:
        active_turn = True

    if turn == 6:
        game_over = True
        losing_text = used_font.render('You lost !', True, white)
        screen.blit(losing_text, (40, 610))

    if game_over and turn < 6:
        winning_text = used_font.render('You won !!', True, white)
        screen.blit(winning_text, (40, 610))

    pygame.display.flip()
pygame.quit()

