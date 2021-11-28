import sys
import os
import core
import forces
from multiprocessing import Process,Queue
import numpy as np
from numpy import array
import random

_rand=lambda a,b:random.randint(a,b)

def simulation(main_queue):
    print("计算进程：%d"%os.getpid())
    space=core.Space()

    space.add_force(forces.Attraction(core.Body(pos=(0,0),mass=10**14)))
    space.add_force(forces.Gravity())

    space.add_body(core.Body(vel=(20,70),pos=(15,-10)))
    while 1:
        space.process(0.01)
        out=[]
        for i in space.bodies:
            out.append(tuple(i.pos))
        #print(out)
        main_queue.put(out)

if __name__ == "__main__":
    import pygame
    from pygame.locals import *

    print("渲染进程：%d"%os.getpid())
    main_queue=Queue(1024)
    process=Process(target=simulation,args=(main_queue,))
    process.start()

    FPS=60
    pygame.init()
    screen=pygame.display.set_mode((600,600),HWSURFACE)
    clock=pygame.time.Clock()
    clock.tick(FPS)
    while 1:
        pygame.draw.circle(screen,(255,0,0),(300,300),5)
        for i in main_queue.get():
            point=array((i[0]+100,-i[1]+100))*3
            pygame.draw.circle(screen,(255,255,255),point,5)
        for event in pygame.event.get():
            if event.type==QUIT:
                process.terminate()
                sys.exit()
        pygame.display.flip()
        screen.fill((0,0,0))
        clock.tick(FPS)