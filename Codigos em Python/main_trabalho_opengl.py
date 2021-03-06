import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

''' Variaveis de entrada '''
#glOrtho(left,right,bottom,top,near,far)
#glFrustum(left,right,bottom,top,near,far)
#gluPerspective(ang, aspect, zNear, zFar)
#glRotate(angle, x, y, z)
#gluLookAt(eye, look_at, Avup)

def converte(valor):
    return int(valor[0:valor.find('/')])

def Objeto(arquivo, cor=None):
    if cor is None: 
        cor = (0.6, 0.6, 0.6)
    
    vertices = []
    faces_triangulares = []
    faces_quadriculares = []

    with open(arquivo) as meu_arquivo:
        for linha in meu_arquivo:
            valores = linha.split()

            if len(valores) == 4 and valores[0] == 'v':
                vertices.append((float(valores[1]), float(valores[2]), float(valores[3])))
            
            elif len(valores) == 4 and valores[0] == 'f':
                v1 = converte(valores[1]) - 1
                v2 = converte(valores[2]) - 1
                v3 = converte(valores[3]) - 1
                faces_triangulares.append((v1, v2, v3))

            elif len(valores) == 5 and valores[0] == 'f':
                v1 = converte(valores[1]) - 1
                v2 = converte(valores[2]) - 1
                v3 = converte(valores[3]) - 1
                v4 = converte(valores[4]) - 1
                faces_quadriculares.append((v1, v2, v3, v4))

    vertices = tuple(vertices)
    faces_triangulares = tuple(faces_triangulares)
    faces_quadriculares = tuple(faces_quadriculares)

    glBegin(GL_TRIANGLES)
    for face in faces_triangulares:
        #glColor3fv(cor)
        for vertice in face:
            glVertex3fv(vertices[vertice])
    glEnd()
    
    glBegin(GL_QUADS)
    for face in faces_quadriculares:
        #glColor3fv(cor)
        for vertice in face:
            glVertex3fv(vertices[vertice])
    glEnd()
    

def Cubo():
    color = (0.6, 0.6, 0.6)

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

    faces = (
        (0, 1, 2, 3),
        (3, 2, 7, 6),
        (6, 7, 5, 4),
        (4, 5, 1, 0),
        (1, 5, 7, 2),
        (4, 0, 3, 6)
    )

    glBegin(GL_QUADS)
    for face in faces:
        #glColor3fv(color)
        for vertex in face:
            glVertex3fv(vertices[vertex])

    glEnd()

def Cilindro():
    n = 2.41421

    vertices = (
        (n, 0, 1),
        (1, 0, n),
        (-n, 0, 1),
        (-1, 0, n),
        (-n, 0, -1),
        (-1, 0, -n),
        (n, 0, -1),
        (1, 0, -n),
        (n, 10, 1),
        (1, 10, n),
        (-n, 10, 1),
        (-1, 10, n),
        (-n, 10, -1),
        (-1, 10, -n),
        (n, 10, -1),
        (1, 10, -n)   
    )
    glBegin(GL_POLYGON)
    glVertex3fv(vertices[0])
    glVertex3fv(vertices[1])
    glVertex3fv(vertices[2])
    glVertex3fv(vertices[3])
    glVertex3fv(vertices[4])
    glVertex3fv(vertices[5])
    glVertex3fv(vertices[6])
    glVertex3fv(vertices[7])
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex3fv(vertices[15])
    glVertex3fv(vertices[14])
    glVertex3fv(vertices[13])
    glVertex3fv(vertices[12])
    glVertex3fv(vertices[11])
    glVertex3fv(vertices[10])
    glVertex3fv(vertices[9])
    glVertex3fv(vertices[8])
    glEnd()

    
    glBegin(GL_QUADS)
    glVertex3fv(vertices[0])
    glVertex3fv(vertices[8])
    glVertex3fv(vertices[9])
    glVertex3fv(vertices[1])
    glEnd()
    
    glBegin(GL_QUADS)
    glVertex3fv(vertices[1])
    glVertex3fv(vertices[9])
    glVertex3fv(vertices[10])
    glVertex3fv(vertices[2])
    glEnd()
    
    glBegin(GL_QUADS)
    glVertex3fv(vertices[2])
    glVertex3fv(vertices[10])
    glVertex3fv(vertices[11])
    glVertex3fv(vertices[3])
    glEnd()
    
    glBegin(GL_QUADS)
    glVertex3fv(vertices[3])
    glVertex3fv(vertices[11])
    glVertex3fv(vertices[12])
    glVertex3fv(vertices[4])
    glEnd()
    
    glBegin(GL_QUADS)
    glVertex3fv(vertices[4])
    glVertex3fv(vertices[12])
    glVertex3fv(vertices[13])
    glVertex3fv(vertices[5])
    glEnd()
    
    glBegin(GL_QUADS)
    glVertex3fv(vertices[5])
    glVertex3fv(vertices[13])
    glVertex3fv(vertices[14])
    glVertex3fv(vertices[6])
    glEnd()
    
    glBegin(GL_QUADS)
    glVertex3fv(vertices[6])
    glVertex3fv(vertices[14])
    glVertex3fv(vertices[15])
    glVertex3fv(vertices[7])
    glEnd()
    
    glBegin(GL_QUADS)
    glVertex3fv(vertices[7])
    glVertex3fv(vertices[15])
    glVertex3fv(vertices[8])
    glVertex3fv(vertices[0])
    glEnd()

def Base():
    color = (0.6, 0.6, 0.6)

    vertices = (
        (5, -0.01, -5),
        (5, 0.01, -5),
        (-5, 0.01, -5),
        (-5, -0.01, -5),
        (5, -0.01, 5),
        (5, 0.01, 5),
        (-5, -0.01, 5),
        (-5, 0.01, 5)
    )

    faces = (
        (0, 1, 2, 3),
        (3, 2, 7, 6),
        (6, 7, 5, 4),
        (4, 5, 1, 0),
        (1, 5, 7, 2),
        (4, 0, 3, 6)
    )

    glBegin(GL_QUADS)
    for face in faces:
        #glColor3fv(color)
        for vertex in face:
            glVertex3fv(vertices[vertex])

    glEnd()

def projecao_ortogonal():    
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glOrtho(-15, 15, -15, 15, 15, 50)
    glClearColor(0.1, 0.6, 0.9, 1) # cor de background
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

def projecao_perspectiva():    
    pygame.init()
    display = (1000, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 100.0)
    glClearColor(0.1, 0.6, 0.9, 1) # cor de background
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

def projecao_obliqua():    
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glFrustum(-15, 15, -15, 15, 15, 50)
    glClearColor(0.1, 0.6, 0.9, 1) # cor de background
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    

''' Inicio '''
#projecao_ortogonal()
projecao_perspectiva()
#projecao_frustum()

#glMatrixMode(GL_PROJECTION)
#projecao = [[0]*4 for i in range(4)]


''' CAMERAS '''
'''camera osicionada a direita'''
#gluLookAt(30, 0, -25, 0, 0, -25, 10, 999999999999999999999, -25)
'''camera posicionada a esquerda'''
#gluLookAt(-30, 0, -25, 0, 0, -25, 10, 999999999999999999999, -25)
'''camera posicionada acima'''
#gluLookAt(0, 30, -25, 0, 0, -25, 0, -25, -30)

''' ILUMINACAO '''
### AMBIENTE ###
glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0.5, 0.5, 0.5))

### LUZ PONTUAL ###
'''
glEnable(GL_LIGHTING)
glLightfv(GL_LIGHT0, GL_POSITION,  (0, 0, 2, 1))
glLightfv(GL_LIGHT0, GL_AMBIENT, (1, 1, 1, 1.0))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1.0))
glLightfv(GL_LIGHT0, GL_SPECULAR, (0.5, 0.5, 0.5, 1.0))
glEnable(GL_LIGHT0)
'''
#glEnable(GL_COLOR_MATERIAL)
#glShadeModel(GL_SMOOTH)
#glShadeModel(GL_FLAT)
#glEnable(GL_DEPTH_TEST)


### LUZES SPOT ###

glPushMatrix()
glEnable(GL_LIGHTING)
glLightfv(GL_LIGHT0, GL_POSITION,  (-5, 0, -17))
glLightfv(GL_LIGHT0, GL_AMBIENT, (1, 1, 1, 1.0))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1.0))
glLightfv(GL_LIGHT0, GL_SPECULAR, (0.5, 0.5, 0.5, 1.0))
glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 2.0); # angulo de abertura
glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, (0, -1, 0)) # direção 
glLightf(GL_LIGHT0, GL_SPOT_EXPONENT, 128) # força de foco
glEnable(GL_LIGHT0)
glPopMatrix()

glPushMatrix()
glLightfv(GL_LIGHT1, GL_POSITION,  (0, 0, -17))
glLightfv(GL_LIGHT1, GL_AMBIENT, (1, 1, 1, 1.0))
glLightfv(GL_LIGHT1, GL_DIFFUSE, (1, 1, 1, 1.0))
glLightfv(GL_LIGHT1, GL_SPECULAR, (0.5, 0.5, 0.5, 1.0))
glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 2.0); # angulo de abertura
glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, (0, -1, 0)) # direção 
glLightf(GL_LIGHT1, GL_SPOT_EXPONENT, 128) # força de foco
glEnable(GL_LIGHT1)
glPopMatrix()

glPushMatrix()
glLightfv(GL_LIGHT2, GL_POSITION,  (5, 0, -17))
glLightfv(GL_LIGHT2, GL_AMBIENT, (1, 1, 1, 1.0))
glLightfv(GL_LIGHT2, GL_DIFFUSE, (1, 1, 1, 1.0))
glLightfv(GL_LIGHT2, GL_SPECULAR, (0.5, 0.5, 0.5, 1.0))
glLightf(GL_LIGHT2, GL_SPOT_CUTOFF, 2.0); # angulo de abertura
glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, (0, -1, 0)) # direção 
glLightf(GL_LIGHT2, GL_SPOT_EXPONENT, 128) # força de foco
glEnable(GL_LIGHT2)
glPopMatrix()

''' Objetos '''

glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.2, 0.1, 0.0, 1])
glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.2, 0.1, 0.0, 1])
glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0, 0, 0, 1])
glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 50)
glPushMatrix()
glTranslate(0, -7, -10)
glScale(30, 10, 30)
Base()
glPopMatrix()

glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.5, 0.5, 0.5, 1])
glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0.5, 0.5, 0.5, 1])
glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 50)
glPushMatrix()
glTranslate(1, -7, -25)
Objeto('objetos/stage.obj')
glPopMatrix()

glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0, 0, 0.1, 1])
glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0, 0, 0.1, 1])
glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0.5, 0.5, 0.5, 1])
glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 50)
glPushMatrix()
glTranslate(0, -5.6, -25)
glRotate(90, 0, 1, 0)
Objeto('objetos/drums basic.obj')
glPopMatrix()

glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.1, 0.1, 0.1, 1])
glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.1, 0.1, 0.1, 1])
glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0.5, 0.5, 0.5, 1])
glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 50)
glPushMatrix()
glTranslate(-5, -4, -25)
glScalef(0.7, 0.7, 0.7)
Objeto('objetos/teclado.obj')
glPopMatrix()

glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.1, 0.1, 0.1, 1])
glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.1, 0.1, 0.1, 1])
glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0.5, 0.5, 0.5, 1])
glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 50)
glPushMatrix()
glTranslatef(-1.2, -2.5, -20)
glRotate(-45, 1, 0, 0)
glScalef(0.01, 0.01, 0.01)
Objeto('objetos/mic.obj')
glPopMatrix()

glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.3, 0.0, 0.0, 1])
glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.3, 0.0, 0.0, 1])
glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0.5, 0.5, 0.5, 1])
glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 50)
glPushMatrix()
glTranslatef(-3.5, 2.5, -18)
glScalef(2, 2, 2)
Objeto('objetos/Slayer logo.obj')
glPopMatrix()

glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.3, 0.0, 0.0, 1])
glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.3, 0.0, 0.0, 1])
glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0.5, 0.5, 0.5, 1])
glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 50)
glPushMatrix()
glTranslatef(0, 0, -15)
glScalef(0.5, 0, 0.5)
Objeto('objetos/cilindro.obj')
glPopMatrix()

''' Loop '''
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        '''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                glTranslatef(-0.5, 0, 0)
            if event.key == pygame.K_RIGHT:
                glTranslatef(0.5, 0, 0)
            if event.key == pygame.K_UP:
                glTranslatef(0, 0.5, 0)
            if event.key == pygame.K_DOWN:
                glTranslatef(0, -0.5, 0)
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            #botao esquerdo do mouse
            if event.button == 1:
                glTranslate(0, 0, 0.5)
            #botao do meio do mouse
            if event.button == 2:
                glTranslate(0, 0, 0.5)
            #botao direito do mouse
            if event.button == 3:
                glTranslatef(0, 0, -0.5)
            #girar botao do meio do mouse para cima
            if event.button == 4:
                glTranslatef(0, 0, 0.5)
            #girar botao do meio do mouse para baixo
            if event.button == 5:
                glTranslatef(0, 0, -0.5)
'''

    #glRotatef(1, 3, 1, 1)

    #glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    pygame.display.flip()
    pygame.time.wait(10)