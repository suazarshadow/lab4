import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import random 

# Початкові параметри

rotation_enabled = False
rotation_axis = True
rotation_speed = 1.0


vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 7),
    (6, 3),
    (7, 2),
    (0, 4),
    (1, 5),
    (7, 6),
    (4, 6)
)

def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    draw_cube()

    pygame.display.flip()
    pygame.time.wait(10)

def main():

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    

    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:    
                        glColor3fv((random.random(), random.random(), random.random()))
                    elif event.button == 3:  
                        global rotation_enabled
                        rotation_enabled = not rotation_enabled
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        global rotation_speed
                        rotation_speed += 1.0
                    elif event.key == pygame.K_DOWN:
                        rotation_speed -= 1.0
                    elif event.key == pygame.K_SPACE:
                        global rotation_axis
                        rotation_axis = not rotation_axis

            if rotation_enabled:
                if rotation_axis:
                    glRotatef(rotation_speed, 1, 0, 0)
                else:
                    glRotatef(rotation_speed, 0, 1, 0)


            draw()

if __name__ == "__main__":
    main()