#The crazy reddit comment wheel of randomness by u/sam0s
import praw
import random
newlist = []

#USE YUR OWN REDDIT USERNAME HERE
r = praw.Reddit(user_agent='sam0s')

sub=r.get_submission(submission_id='4oypr1')#Plug in your reddit post's short url
sub.replace_more_comments(limit=10000, threshold=10)

flat_comments = praw.helpers.flatten_tree(sub.comments)
for c in flat_comments:
    if c.body.startswith('/u'):
        newlist.append((str(c).split(" "))[0])

for f in newlist:
    if '\n' in f:
        newlist[newlist.index(f)]=(f.split('\n'))[0]

print list(set(newlist))


spin=False

import pygame
from pygame.locals import *



pygame.init()
disp=pygame.display.set_mode((640,480))
fnt=pygame.font.Font(None,37)
pygame.display.set_caption("CRAZY REDDIT GIVEAWAY WHEEL")
msg= fnt.render(str(len(newlist))+" entries! Press any key to begin!", 1, (255,255,255))
winner = random.choice(newlist)

msg2= fnt.render("the winner is " +winner, 1, (255,255,255))
go=True
wheelimg="wheel img.png"
wheelimg=pygame.image.load(wheelimg)
wheeltime = random.randrange(10000,10010)
wheelimg=pygame.transform.scale(wheelimg,(200,200))
while go:
    disp.fill((0,0,185))
    disp.blit(wheelimg,(230,138))
    disp.blit(msg,(25,160))
    for e in pygame.event.get():
        if e.type == QUIT:
            go =0
        if e.type == KEYDOWN:
            spin=True
    pygame.display.flip()
    while spin:
        wheeltime-=1
        disp.fill((0,0,185))
        wheelimg=pygame.transform.rotate(wheelimg,90)
        disp.blit(wheelimg,(230,138))
        winner = random.choice(newlist)

        msg2= fnt.render("the winner is " +winner, 1, (255,255,255))
        disp.blit(msg2,(25,50))
        for e in pygame.event.get():
            if e.type == QUIT:
                go =0
                spin =0
        
        pygame.display.flip()
        while wheeltime==0:
            disp.fill((0,0,185))
            disp.blit(wheelimg,(230,138))
            disp.blit(msg2,(25,60))
            for e in pygame.event.get():
                if e.type == QUIT:
                    go =0
                    wheeltime=1
                    spin=0
            pygame.display.flip()

pygame.display.quit()
