import pygame, sys

#borders for paddles
def paddleborders():
	if box1.top<win.top:
		box1.top=win.top
	if box1.bottom>win.bottom:
		box1.bottom=win.bottom
	if box2.top<win.top:
		box2.top=win.top
	if box2.bottom>win.bottom:
		box2.bottom=win.bottom

#makes ball bounce from wall
def ballmove():
	if box3.left < win.left or box3.right > win.right:
		vec[0] = -vec[0]
	if box3.top < win.top or box3.bottom > win.bottom:
		vec[1] = -vec[1]
# makes ball bounce from paddles
def bounce():
	#~ if box3.right<box1.right and box3.left>box1.left and (box3.bottom<box1.top or box3.top>box1.bottom):
		#~ vec[1]=-vec[1]
		#~ vec[0]=-vec[0]
	#~ if box3.right<box2.right and box3.left>box2.left and (box3.bottom<box2.top or box3.top>box2.bottom):
		#~ vec[1]=-vec[1]
		#~ vec[0]=-vec[0]
	if box3.left==box1.right and box3.top>box1.top and box3.bottom<box1.bottom:
		vec[0]=-vec[0]
	if box3.right==box2.left and box3.top>box2.top and box3.bottom<box2.bottom:
		vec[0]=-vec[0]

	
#colors
black = (0, 0, 0); white = (255, 255, 255)
blue=(0,0,255)
red=(255,0,0)
pygame.init()
#size of window
windwidth=640
windheight=480

scr = pygame.display.set_mode((windwidth, windheight))
win = scr.get_rect()

box1 = pygame.Rect( 0, 0, 15, 100)#player1 paddle
#player1 starting position
box1.x = 0
box1.y = (windheight-100)/2
box2 = pygame.Rect( 0, 0, 15, 100)#player2 paddle
#player2 starting position
box2.x=windwidth-15
box2.y=(windheight-100)/2
box3 = pygame.Rect( 0, 0, 10, 10)#ball
#ball starting position
box3.x=windwidth/2
box3.y=windheight/2
#scores at the beginning of the game
score1=0
score2=0

step=30
pygame.key.set_repeat(50,50)

vec=[1,1]
fps=pygame.time.Clock()

myfont = pygame.font.Font('freesansbold.ttf', 22)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				box1 = box1.move(0,-step)
			if event.key == pygame.K_s:
				box1 = box1.move(0,step)
			if event.key == pygame.K_UP:
				box2 = box2.move(0,-step)
			if event.key == pygame.K_DOWN:
				box2 = box2.move(0,step)
	
	paddleborders()
	box3=box3.move(vec)#starts ball movement
	ballmove()
	bounce()
	
	
	#adds 1 point to one of players for hiting oponent's wall
	if box3.left < win.left:
		score2 = score2+1
	if box3.right > win.right:
		score1 = score1+1
	#writes players scores on the screen
	msg=myfont.render("Player1: %s       Player2: %s"%(score1, score2), True, white)
	msg_box=msg.get_rect()
	msg_box.center=win.center
	
	scr.fill(black)
	scr.blit(msg, msg_box)
	pygame.draw.rect(scr,blue,box1)
	pygame.draw.rect(scr,red,box2)
	pygame.draw.rect(scr,white,box3)
	pygame.display.flip()
	fps.tick(500)
