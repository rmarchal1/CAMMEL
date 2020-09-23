#!/opt/local/bin/python3.6

try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *
except:
    print("OpenGL wrapper for python not found")

#from mpl_toolkits.mplot3d import Axes3D
#from mpl_toolkits.mplot3d.art3d import Poly3DCollection
#import matplotlib.pyplot as plt
import os
import sys
import numpy as np
from math import sqrt
import cv2
import glfw
#from Renderers.Renderer3D import *
from PIL import Image
from PIL import ImageOps

global render
name="Full potential"
name2="monopole"
name3="dipole"
name4="quadrupole"
window_name=["Full_potential","monopole","dipole","quadrupole"]
class Cube(list):
    # Constructor for the cube class
    #print('enter')
#    filename=str(sys.argv[1])[:-4]
#    print(filename)
    def __init__(selfa, *args):
        selfa.image="n"
        selfa.extend(args)
        selfa.rotate_y = 0.0
        selfa.rotate_x = 0.0
        selfa.rotate_z = 0.0
        selfa.scale = 0.4
        selfa.scale2= 0.4
        selfa.scale3=0.4
        selfa.filename=str(sys.argv[1])[:-4]
        print(selfa.filename)
#        selfa.tri=selfa[0]
#        selfa.color=selfa[1]
        selfa.translatex=0
        selfa.translatey=0
        selfa.translatez=0
        selfa.show_atlegend=0
        selfa.show_zoomvalues=0
        selfa.show_cartesian=0
        selfa.show_glegend=0
        global tkList
        tkList = glGenLists( 1 )
        glNewList( tkList, GL_COMPILE) 
#        glutSolidTeapot( 1.0 )
        glEndList( )
        #print(selfa.numat)
    # Initialize
    def glut_print(selfa, x,  y,z,  font,  text, r,  g , b , a):
    
        blending = False 
        if glIsEnabled(GL_BLEND) :
            blending = True
    
        #glEnable(GL_BLEND)
        glColor3f(1,1,1)
        glRasterPos3f(x,y,z)
        for ch in text :
            glutBitmapCharacter( font , ctypes.c_int( ord(ch) ) )
    
    
        if not blending :
            glDisable(GL_BLEND) 
    def init(selfa):
      t=1
        # Set background to black
        #glClearColor(0.0, 0.0, 0.0, 0.0)
    # Draw half of the cube with corners cut
    def draw_half4(selfa):
        glutPostRedisplay()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        pos=0.8
        if atome=='y' or atome=='s' or atome=='ynh':
           glEnable( GL_LIGHTING )
           if selfa.show_atlegend==0: 
             for i in range(0,len(atom_legend)):
                glPushMatrix()
                glTranslatef(3.15,0.85-(i*0.25), 0)
                glColor3f(atom_legend[i][2][0],atom_legend[i][2][1],atom_legend[i][2][2])
                glutSolidSphere(atom_legend[i][1]/3., 200,16)
                glPopMatrix()
                glRasterPos3f( 3.25, 0.8-(i*0.25), 0 )
                pos=pos-0.25
                for c in str.upper(atom_legend[i][0]):
                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
        if easy=='y':
         if gx+gy+gz>0:
           glPushMatrix()
           glTranslatef(selfa.translatex,selfa.translatey,selfa.translatez)
           glRotatef(selfa.rotate_y,0.,1.,0.)
           glRotatef(selfa.rotate_x,1.,0.,0.)
           glRotatef(selfa.rotate_z,0.,0.,1.)           
           if gx==1:
             glColor3f(1.0,0.0,0.0)
             i=0
             glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.0,0.0,0.0,1.0])
             v2=np.zeros(3)
             v1=np.zeros(3)
             for j in range(0,3):
                v2[j]=tensor[i][j+1]*selfa.scale3*smax4/smax
                v1[j]=-1*tensor[i][j+1]*selfa.scale3*smax4/smax
             v2r = v2 - v1
             z = np.array([0.0, 0.0, 1.0])
             ax = np.cross(z, v2r)
             l = sqrt(np.dot(v2r, v2r))
             angle = 180.0 / np.pi * np.arccos(np.dot(z, v2r) / l)
             glPushMatrix()
             glTranslatef(v1[0], v1[1], v1[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             test=gluNewQuadric()
             gluCylinder(test,0.1*selfa.scale2,0.1*selfa.scale2,l,100,100)
#             glutSolidCylinder(0.1*selfa.scale2, l, 100, 100)
             glPopMatrix()

             glPushMatrix()
             glTranslatef(v2[0], v2[1], v2[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             glutSolidCone(0.1*selfa.scale2*2.0, l/10.0, 100, 100)
             glPopMatrix()
           if gy==1:
             glColor3f(0.0,1.0,0.0)
             i=1
             glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.0,0.0,0.0,1.0])
             v2=np.zeros(3)
             v1=np.zeros(3)
             for j in range(0,3):
                v2[j]=tensor[i][j+1]*selfa.scale3*smax4/smax
                v1[j]=-1*tensor[i][j+1]*selfa.scale3*smax4/smax
             v2r = v2 - v1
             z = np.array([0.0, 0.0, 1.0])
             ax = np.cross(z, v2r)
             l = sqrt(np.dot(v2r, v2r))
             angle = 180.0 / np.pi * np.arccos(np.dot(z, v2r) / l)
             glPushMatrix()
             glTranslatef(v1[0], v1[1], v1[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             test=gluNewQuadric()
             gluCylinder(test,0.1*selfa.scale2,0.1*selfa.scale2,l,100,100)
             #glutSolidCylinder(0.1*selfa.scale2, l, 100, 100)
             glPopMatrix()
             glPushMatrix()
             glTranslatef(v2[0], v2[1], v2[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             glutSolidCone(0.1*selfa.scale2*2.0, l/10.0, 100, 100)
             glPopMatrix()
           if gz==1:
             glColor3f(0.0,0.0,1.0)
             i=2
             glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.0,0.0,0.0,1.0])
             v2=np.zeros(3)
             v1=np.zeros(3)
             for j in range(0,3):
                v2[j]=tensor[i][j+1]*selfa.scale3*smax4/smax
                v1[j]=-1*tensor[i][j+1]*selfa.scale3*smax4/smax
             v2r = v2 - v1
             z = np.array([0.0, 0.0, 1.0])
             ax = np.cross(z, v2r)
             l = sqrt(np.dot(v2r, v2r))
             angle = 180.0 / np.pi * np.arccos(np.dot(z, v2r) / l)
             glPushMatrix()
             glTranslatef(v1[0], v1[1], v1[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             test=gluNewQuadric()
             gluCylinder(test,0.1*selfa.scale2,0.1*selfa.scale2,l,100,100)
             #glutSolidCylinder(0.1*selfa.scale2, l, 100, 100)
             glPopMatrix()
             glPushMatrix()
             glTranslatef(v2[0], v2[1], v2[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             glutSolidCone(0.1*selfa.scale2*2.0, l/10.0, 100, 100)
             glPopMatrix()
           glPopMatrix()           
#          glPushMatrix()
#          glRotatef(selfa.rotate_y,0.,1.,0.)
#          glRotatef(selfa.rotate_x,1.,0.,0.)
#          glRotatef(selfa.rotate_z,0.,0.,1.)
#          glLineWidth(2.0)
#          glDisable(GL_LIGHTING)
#          glBegin(GL_LINES)
#          if gx==1:
#             glColor3f(1.0,0.0,0.0)
#             glVertex3f(0.0,0.0,0.0)
#             i=0
#             glVertex3f(tensor[i][1]*selfa.scale,tensor[i][2]*selfa.scale,tensor[i][3]*selfa.scale)
#             glVertex3f(0.0,0.0,0.0)
#             glVertex3f(-1.*tensor[i][1]*selfa.scale,-1.*tensor[i][2]*selfa.scale,-1.*tensor[i][3]*selfa.scale)
#
#          if gy==1:
#             glColor3f(0.0,1.0,0.0)
#             glVertex3f(0.0,0.0,0.0)
#             i=1
#             glVertex3f(tensor[i][1]*selfa.scale,tensor[i][2]*selfa.scale,tensor[i][3]*selfa.scale)
#             glVertex3f(0.0,0.0,0.0)
#             glVertex3f(-1.*tensor[i][1]*selfa.scale,-1.*tensor[i][2]*selfa.scale,-1.*tensor[i][3]*selfa.scale)
#
#          if gz==1:
#             glColor3f(0.0,0.0,1.0)
#             glVertex3f(0.0,0.0,0.0)
#             i=2
#             glVertex3f(tensor[i][1]*selfa.scale,tensor[i][2]*selfa.scale,tensor[i][3]*selfa.scale)
#             glVertex3f(0.0,0.0,0.0)
#             glVertex3f(-1.*tensor[i][1]*selfa.scale,-1.*tensor[i][2]*selfa.scale,-1.*tensor[i][3]*selfa.scale)
#          glEnd()
#          glPopMatrix()
        if easy=='y':
         if gx+gy+gz>0:
           pos=pos+0.25
           pos2=pos
           glEnable( GL_LIGHTING )
           glLineWidth(2.0)
#           glCallList( tkList )
           glBegin(GL_LINES)
           glNormal3f(0., 0., +1.)
           if selfa.show_glegend==0:
             if gx==1:
               glColor3f(1.0,0.0,0.0)
               glVertex3f(3.0,pos2-0.25,0.0)
               glVertex3f(3.1,pos2-0.25,0.0)
               pos2=pos2-0.25
             if gy==1:
               glColor3f(0.0,1.0,0.0)
               glVertex3f(3.0,pos2-0.25,0.0)
               glVertex3f(3.1,pos2-0.25,0.0)
               pos2=pos2-0.25
             if gz==1:
               glColor3f(0.0,0.0,1.0)
               glVertex3f(3.0,pos2-0.25,0.0)
               glVertex3f(3.1,pos2-0.25,0.0)
               pos2=pos2-0.25
           glEnd()
           glCallList( tkList )
           #glDisable( GL_LIGHTING )
           glColor3f( 0, 0, 0 )
           if selfa.show_glegend==0:
             if gx==1:
               glRasterPos3f(3.25,pos-0.25,0.0)
               pos=pos-0.25
               for c in 'gX':
                     glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
             if gy==1:
               glRasterPos3f(3.25,pos-0.25,0.0)
               pos=pos-0.25
               for c in 'gY':
                     glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
             if gz==1:
               glRasterPos3f(3.25,pos-0.25,0.0)
               pos=pos-0.25
               for c in 'gZ':
                     glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
        glColor3f(0.0 ,0., 0.99)
        glDisable( GL_LIGHTING )
#        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
#        glEnable(GL_BLEND)
        glPushMatrix()
        glTranslatef(selfa.translatex,selfa.translatey,selfa.translatez)
        glRotatef(selfa.rotate_y,0.,1.,0.)
        glRotatef(selfa.rotate_x,1.,0.,0.)
        glRotatef(selfa.rotate_z,0.,0.,1.)
        glBegin(GL_QUADS)
        for i in range(0,len(tri4)):
#          glColor4f(color4[i][0] ,color4[i][1], color4[i][2], 0.6)
#          glVertex3f(tri4[i][0][0]*selfa.scale,tri4[i][0][1]*selfa.scale,tri4[i][0][2]*selfa.scale)
#          glColor4f(color4[i][3] ,color4[i][4], color4[i][5], 0.6)
#          glVertex3f(tri4[i][1][0]*selfa.scale,tri4[i][1][1]*selfa.scale,tri4[i][1][2]*selfa.scale)
#          glColor4f(color4[i][6] ,color4[i][7], color4[i][8], 0.6)
#          glVertex3f(tri4[i][2][0]*selfa.scale,tri4[i][2][1]*selfa.scale,tri4[i][2][2]*selfa.scale)
#          glColor4f(color4[i][9] ,color4[i][10], color4[i][11], 0.6)
#          glVertex3f(tri4[i][3][0]*selfa.scale,tri4[i][3][1]*selfa.scale,tri4[i][3][2]*selfa.scale)


          glColor3f(color4[i][0] ,color4[i][1], color4[i][2])
          glVertex3f(tri4[i][0][0]*selfa.scale,tri4[i][0][1]*selfa.scale,tri4[i][0][2]*selfa.scale)
          glColor3f(color4[i][3] ,color4[i][4], color4[i][5])
          glVertex3f(tri4[i][1][0]*selfa.scale,tri4[i][1][1]*selfa.scale,tri4[i][1][2]*selfa.scale)
          glColor3f(color4[i][6] ,color4[i][7], color4[i][8])
          glVertex3f(tri4[i][2][0]*selfa.scale,tri4[i][2][1]*selfa.scale,tri4[i][2][2]*selfa.scale)
          glColor3f(color4[i][9] ,color4[i][10], color4[i][11])
          glVertex3f(tri4[i][3][0]*selfa.scale,tri4[i][3][1]*selfa.scale,tri4[i][3][2]*selfa.scale)
        glEnd()
        glPopMatrix()

#        glRasterPos3f( 0.1, -2.1, 0 )
#        glPushMatrix()
#        glRotatef(selfa.rotate_y,0.,1.,0.)
#        glRotatef(selfa.rotate_x,1.,0.,0.)
#        glRotatef(selfa.rotate_z,0.,0.,1.)
        glBegin(GL_QUADS)
        pas=(smax4-smin4)/300.0
        for i in range(0,300):
          p=smin4+float(i)*pas
          f=(p-smin4)/(smax4-smin4)
          a=(1-f)/0.25
          X=int(a)
          Y=int(255*(a-X))
          if X==0:
                  r=255
                  g=Y
                  b=0
          elif X==1:
                  r=255-Y
                  g=255
                  b=0
          elif X==2:
                  r=0
                  g=255
                  b=Y
          elif X==3:
                  r=0
                  g=255-Y
                  b=255
          else:
                  r=0
                  g=0
                  b=255
          glColor3f(r/255.,g/255.,b/255.)
#          glVertex3f(3.0,0.0,0.0)
#          glVertex3f(3.2,0.0,0.0)
          glVertex3f(3.1,1.4+float((i-1)/150),0.0)
          glVertex3f(3.4,1.4+float((i-1)/150),0.0)
          glVertex3f(3.4,1.4+float(i/150),0.0)
          glVertex3f(3.1,1.4+float(i/150),0.0)
        glEnd()
#        glPopMatrix()


#        test=max(tri4)
#        print(test)

#        glPushMatrix()
#        glRotatef(selfa.rotate_y,0.,1.,0.)
#        glRotatef(selfa.rotate_x,1.,0.,0.)
#        glRotatef(selfa.rotate_z,0.,0.,1.)        
#        glLineWidth(2.0)
#        glBegin(GL_LINES)
#        glColor3f(0.,0.,0.)
#        glVertex3f(-3.5,-3.0,-3.0)
#        glVertex3f(-3.0,-3.0,-3.0)
##        glVertex3f(-3.0,-3.0*np.cos(selfa.rotate_x*2*np.pi/360.)+3.0*np.sin(selfa.rotate_x*2*np.pi/360.),-3.0*np.sin(selfa.rotate_x*2*np.pi/360.)-3.0*np.cos(selfa.rotate_x*2*np.pi/360.))
#        glVertex3f(-3.5,-3.0,-3.0)
#        glVertex3f(-3.5,-2.5,-3.0)
##        glVertex3f(-3.5*np.cos(selfa.rotate_y*2*np.pi/360.)-3.0*np.sin(selfa.rotate_y*2*np.pi/360.),-2.5,3.5*np.sin(selfa.rotate_y*2*np.pi/360.)-3.0*np.cos(selfa.rotate_y*2*np.pi/360.))
#        glVertex3f(-3.5,-3.0,-3.0)
#        glVertex3f(-3.5*np.cos(selfa.rotate_z*2*np.pi/360.)+3.0*np.sin(selfa.rotate_z*2*np.pi/360.),-3.5*np.sin(selfa.rotate_z*2*np.pi/360.)-3.0*np.cos(selfa.rotate_z*2*np.pi/360.),-2.5)
##        glVertex3f(-3.5,-3.0,-2.5)
#        glEnd()
#        glPopMatrix()
        if cartesian=='y' and selfa.show_cartesian==0:
          x=[[-3.5,-3.5,-3.5],[-3.0,-3.5,-3.5],[-3.5,-3.0,-3.5],[-3.5,-3.5,-3.0],[-2.9,-3.5,-3.5],[-3.5,-2.9,-3.5],[-3.5,-3.5,-2.9]]
            #rotation selons z
          for i in range(0,7):
            x[i][0]=x[i][0]*np.cos(selfa.rotate_z*np.pi/180.0)-x[i][1]*np.sin(selfa.rotate_z*np.pi/180.0)
            x[i][1]=x[i][0]*np.sin(selfa.rotate_z*np.pi/180.0)+x[i][1]*np.cos(selfa.rotate_z*np.pi/180.0)
            #rotation selons x
          for i in range(0,7):
            x[i][1]=x[i][1]*np.cos(selfa.rotate_x*np.pi/180.0)-x[i][2]*np.sin(selfa.rotate_x*np.pi/180.0)
            x[i][2]=x[i][1]*np.sin(selfa.rotate_x*np.pi/180.0)+x[i][2]*np.cos(selfa.rotate_x*np.pi/180.0)
            #rotation selons x
          for i in range(0,7):
            x[i][2]=x[i][2]*np.cos(selfa.rotate_y*np.pi/180.0)-x[i][0]*np.sin(selfa.rotate_y*np.pi/180.0)
            x[i][0]=x[i][2]*np.sin(selfa.rotate_y*np.pi/180.0)+x[i][0]*np.cos(selfa.rotate_y*np.pi/180.0)
          a=-3.5-x[0][0]
          b=-3.5-x[0][1]
          d=-3.5-x[0][2]
          glLineWidth(1.0)
          glBegin(GL_LINES)
          glColor3f(0.9,0.,0.)
          for i in range(0,4):
            glVertex3f(x[0][0]+a,x[0][1]+b,x[0][2]+d)
            glVertex3f(x[1][0]+a,x[1][1]+b,x[1][2]+d)
            glVertex3f(x[0][0]+a,x[0][1]+b,x[0][2]+d)
            glVertex3f(x[2][0]+a,x[2][1]+b,x[2][2]+d)
            glVertex3f(x[0][0]+a,x[0][1]+b,x[0][2]+d)
            glVertex3f(x[3][0]+a,x[3][1]+b,x[3][2]+d)
          glEnd()
        glCallList( tkList )
        glDisable( GL_LIGHTING )
        glColor3f( 0, 0, 0 )
        if cartesian=='y' and selfa.show_cartesian==0:
          glRasterPos3f(x[4][0]+a,x[4][1]+b,x[4][2]+d)
          for c in 'x': 
                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f(x[5][0]+a,x[5][1]+b,x[5][2]+d)
          for c in 'y':
                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f(x[6][0]+a,x[6][1]+b,x[6][2]+d)
          for c in 'z':
                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
        for i in range(0,len(str(smax4))):
         if str(smax4)[i]=='.':
           ssmax4=str(smax4)[0:i+3]
#        glRasterPos3f( 0.1, -2.1, 0 )
        for i in range(0,len(str(smin4))):
         if str(smin4)[i]=='.':
           ssmin4=str(smin4)[0:i+3]
        smoy=(smax4+smin4)/2.
        smoy2=(smin4+smoy)/2.
        smoy3=(smax4+smoy)/2.
        for i in range(0,len(str(selfa.scale))):
         if str(selfa.scale)[i]=='.':
           szoom=str(selfa.scale)[0:i+3]
        for i in range(0,len(str(selfa.rotate_x))):
         if str(selfa.rotate_x)[i]=='.':
           srotx=str(selfa.rotate_x)[0:i+3]
        for i in range(0,len(str(selfa.rotate_y))):
         if str(selfa.rotate_y)[i]=='.':
           sroty=str(selfa.rotate_y)[0:i+3]
        for i in range(0,len(str(selfa.rotate_z))):
         if str(selfa.rotate_z)[i]=='.':
           srotz=str(selfa.rotate_z)[0:i+3]
        for i in range(0,len(str(selfa.scale2))):
         if str(selfa.scale2)[i]=='.':
           szoom2=str(selfa.scale2)[0:i+3]
        for i in range(0,len(str(smoy))):
         if str(smoy)[i]=='.':
           ssmoy=str(smoy)[0:i+3]
        for i in range(0,len(str(smoy2))):
         if str(smoy2)[i]=='.':
           ssmoy2=str(smoy2)[0:i+3]
        for i in range(0,len(str(smoy3))):
         if str(smoy3)[i]=='.':
           ssmoy3=str(smoy3)[0:i+3]
        glRasterPos3f( 2.98, 1.45+300./150., 0 )
        for c in ssmax4:
                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
        glRasterPos3f( 2.98, 1.17, 0 )
        for c in ssmin4:
                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        glRasterPos3f( 3.05, 1.07+300./150., 0 )
#        for c in ssmax4:
#        	glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        glRasterPos3f( 3.05, 1.07, 0 )
#        for c in ssmin4:
#                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        glRasterPos3f( 3.05, 1.07+150./150., 0 )
#        for c in ssmoy:
#                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        glRasterPos3f( 3.05, 1.07+75./150., 0 )
#        for c in ssmoy2:
#                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        glRasterPos3f( 3.05, 1.07+225./150., 0 )
#        for c in ssmoy3:
#                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
        if selfa.show_zoomvalues==0:
          glRasterPos3f( 2.0, -2.4, 0 )
          for c in 'rotat x':
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 2.0, -2.6, 0 )
          for c in 'rotat x':
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 2.0, -2.8, 0 )
          for c in 'rotat z':
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          selfa.rotate_x
          glRasterPos3f( 2.0, -3.0, 0 )
          for c in 'zoom pot':
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 2.0, -3.2, 0 )
          for c in 'zoom mol':
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 3.05, -3.0, 0 )
          for c in szoom:
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 3.05, -3.2, 0 )
          for c in szoom2:
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 3.05, -2.4, 0 )
          for c in srotx:
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 3.05, -2.6, 0 )
          for c in sroty:
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 3.05, -2.8, 0 )
          for c in srotz:
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        pos=0.8
#        if atome=='y':
#           glEnable( GL_LIGHTING )
#           for i in range(0,len(atom_legend)):
#                glPushMatrix()
#                glTranslatef(3.15,0.85-(i*0.25), 0)
#                glColor3f(atom_legend[i][2][0],atom_legend[i][2][1],atom_legend[i][2][2])
#                glutSolidSphere(atom_legend[i][1]/3., 200,16)
#                glPopMatrix()
#                glRasterPos3f( 3.25, 0.8-(i*0.25), 0 )
#                pos=pos-0.25
#                for c in str.upper(atom_legend[i][0]):
#                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          # glEnable( GL_LIGHTING )
#        if easy=='y':
#           pos=pos+0.25
#           glEnable( GL_LIGHTING )
#           glLineWidth(4.0)
#           glBegin(GL_LINES)
#           glNormal3f(0., 0., +1.)
#           glColor3f(1.0,0.0,0.0)
#           glVertex3f(3.0,pos-0.25,0.0)
#           glVertex3f(3.1,pos-0.25,0.0)
#           glColor3f(0.0,1.0,0.0)
#           glVertex3f(3.0,pos-0.5,0.0)
#           glVertex3f(3.1,pos-0.5,0.0)
#           glColor3f(0.0,0.0,1.0)
#           glVertex3f(3.0,pos-0.75,0.0)
#           glVertex3f(3.1,pos-0.75,0.0)
#           glEnd()
#           glCallList( tkList )
#           glDisable( GL_LIGHTING )
#           glColor3f( 0, 0, 0 )
#           glRasterPos3f(3.25,pos-0.25,0.0)
#           for c in 'gX':
#                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#           glRasterPos3f(3.25,pos-0.5,0.0)
#           for c in 'gY':
#                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#           glRasterPos3f(3.25,pos-0.75,0.0)
#           for c in 'gZ':
#                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )

        maxi=0.0
#        print('atome=',atome)
        if atome=='y' or atome=='s' or atome=='ynh':
          glEnable(GL_LIGHTING)
          for i in range(0,len(extraction)):
            glPushMatrix()
            glTranslatef(selfa.translatex,selfa.translatey,selfa.translatez)
            glRotatef(selfa.rotate_y,0.,1.,0.)
            glRotatef(selfa.rotate_x,1.,0.,0.)
            glRotatef(selfa.rotate_z,0.,0.,1.)
            glColor3f(extraction[i][2][0],extraction[i][2][1],extraction[i][2][2])
            glTranslatef(extraction[i][0][0]*selfa.scale2,extraction[i][0][1]*selfa.scale2,extraction[i][0][2]*selfa.scale2)
            glutSolidSphere(extraction[i][1]*selfa.scale2, 200, 16)
#            quadratic = gluNewQuadric()
#            gluCylinder(quadratic, 3.0, 6.0, 5.0, 10, 10)
#            gluDisk(quadratic, INNER_RADIUS, OUTER_RADIUS, SLICES, LOOPS)
#            glutSolidCylinder(0.5,0.5,10,10)
            glPopMatrix()
#        glColor3f(0.0,0.0,0.0)
#        quadric=gluNewQuadric()
#        gluQuadricNormals(quadric, GLU_SMOOTH)
#        gluCylinder(quadric, radius, radius, 12.0, 32, 1)
#        gluQuadricOrientation(quadric,GLU_INSIDE)
          glDisable(GL_LIGHTING)
          glPushMatrix()
          glTranslatef(selfa.translatex,selfa.translatey,selfa.translatez)
          glRotatef(selfa.rotate_y,0.,1.,0.)
          glRotatef(selfa.rotate_x,1.,0.,0.)
          glRotatef(selfa.rotate_z,0.,0.,1.)
          glLineWidth(1.0)
          glColor3f( 0, 0, 0 )
#          glBegin(GL_LINES)
          for i in range(0,len(liaison)):
             glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.0,0.0,0.0,1.0])
             v2=np.zeros(3)
             v1=np.zeros(3)
             for j in range(0,3):
              v2[j]=extraction[liaison[i][0]][0][j]*selfa.scale2
              v1[j]=extraction[liaison[i][1]][0][j]*selfa.scale2
#             v2=[extraction[liaison[i][0]][0][0],extraction[liaison[i][0]][0][1],extraction[liaison[i][0]][0][2]]
#             v1=[extraction[liaison[j][0]][0][0],extraction[liaison[j][0]][0][1],extraction[liaison[j][0]][0][2]]
             v2r = v2 - v1
             z = np.array([0.0, 0.0, 1.0])
             ax = np.cross(z, v2r)
             l = sqrt(np.dot(v2r, v2r))
             angle = 180.0 / np.pi * np.arccos(np.dot(z, v2r) / l)
             glPushMatrix()
             glTranslatef(v1[0], v1[1], v1[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             test=gluNewQuadric()
             gluCylinder(test,0.05*selfa.scale2,0.05*selfa.scale2,l,100,100)
#             glutSolidCylinder(0.05*selfa.scale2, l, 100, 100)
             glPopMatrix()
#            glVertex3f(extraction[liaison[i][0]][0][0]*selfa.scale2,extraction[liaison[i][0]][0][1]*selfa.scale2,extraction[liaison[i][0]][0][2]*selfa.scale2)
#            glVertex3f(extraction[liaison[i][1]][0][0]*selfa.scale2,extraction[liaison[i][1]][0][1]*selfa.scale2,extraction[liaison[i][1]][0][2]*selfa.scale2)
#          glEnd()
          glPopMatrix()

#        if easy=='y':
#          glPushMatrix()
#          glRotatef(selfa.rotate_y,0.,1.,0.)
#          glRotatef(selfa.rotate_x,1.,0.,0.)
#          glRotatef(selfa.rotate_z,0.,0.,1.)
#          glLineWidth(4.0)
#          glDisable(GL_LIGHTING)
#          glBegin(GL_LINES)
#          for i in range(0,3):
#             glNormal3f(0., 0., +1.)
#             if i==0: glColor3f(0.9,0.0,0.0)
#             elif i==1: glColor3f(0.0,0.9,0.0)
#             else: glColor3f(0.0,0.0,0.9)
#             glVertex3f(0.0,0.0,0.0)
#             glVertex3f(tensor[i][1]*selfa.scale,tensor[i][2]*selfa.scale,tensor[i][3]*selfa.scale)
#             glVertex3f(0.0,0.0,0.0)
#             glVertex3f(-1.*tensor[i][1]*selfa.scale,-1.*tensor[i][2]*selfa.scale,-1.*tensor[i][3]*selfa.scale)
#          glEnd()
#          glPopMatrix()
        glDisable(GL_LIGHTING)
#        glEnable(GL_LIGHTING)
        glMatrixMode(GL_MODELVIEW)
        glFlush()
        glutSwapBuffers()
        return
    def draw_half3(selfa):
        glutPostRedisplay()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        pos=0.8
        if atome=='y' or atome=='s' or atome=='ynh':
           glEnable( GL_LIGHTING )
           if selfa.show_atlegend==0: 
             for i in range(0,len(atom_legend)):
                glPushMatrix()
                glTranslatef(3.15,0.85-(i*0.25), 0)
                glColor3f(atom_legend[i][2][0],atom_legend[i][2][1],atom_legend[i][2][2])
                glutSolidSphere(atom_legend[i][1]/3., 200,16)
                glPopMatrix()
                glRasterPos3f( 3.25, 0.8-(i*0.25), 0 )
                pos=pos-0.25
                for c in str.upper(atom_legend[i][0]):
                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
        if easy=='y':
         if gx+gy+gz>0:
           glPushMatrix()
           glTranslatef(selfa.translatex,selfa.translatey,selfa.translatez)
           glRotatef(selfa.rotate_y,0.,1.,0.)
           glRotatef(selfa.rotate_x,1.,0.,0.)
           glRotatef(selfa.rotate_z,0.,0.,1.)           
           if gx==1:
             glColor3f(1.0,0.0,0.0)
             i=0
             glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.0,0.0,0.0,1.0])
             v2=np.zeros(3)
             v1=np.zeros(3)
             for j in range(0,3):
                v2[j]=tensor[i][j+1]*selfa.scale3*abs(smax3/smax)
                v1[j]=-1*tensor[i][j+1]*selfa.scale3*abs(smax3/smax)

             v2r = v2 - v1
             z = np.array([0.0, 0.0, 1.0])
             ax = np.cross(z, v2r)
             l = sqrt(np.dot(v2r, v2r))
             angle = 180.0 / np.pi * np.arccos(np.dot(z, v2r) / l)
             glPushMatrix()
             glTranslatef(v1[0], v1[1], v1[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             test=gluNewQuadric()
             gluCylinder(test,0.1*selfa.scale2,0.1*selfa.scale2,l,100,100)
#             glutSolidCylinder(0.1*selfa.scale2, l, 100, 100)
             glPopMatrix()

             glPushMatrix()
             glTranslatef(v2[0], v2[1], v2[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             glutSolidCone(0.1*selfa.scale2*2.0, l/10.0, 100, 100)
             glPopMatrix()
           if gy==1:
             glColor3f(0.0,1.0,0.0)
             i=1
             glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.0,0.0,0.0,1.0])
             v2=np.zeros(3)
             v1=np.zeros(3)
             for j in range(0,3):
                v2[j]=tensor[i][j+1]*selfa.scale3*abs(smax3/smax)
                v1[j]=-1*tensor[i][j+1]*selfa.scale3*abs(smax3/smax)
             v2r = v2 - v1
             z = np.array([0.0, 0.0, 1.0])
             ax = np.cross(z, v2r)
             l = sqrt(np.dot(v2r, v2r))
             angle = 180.0 / np.pi * np.arccos(np.dot(z, v2r) / l)
             glPushMatrix()
             glTranslatef(v1[0], v1[1], v1[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             test=gluNewQuadric()
             gluCylinder(test,0.1*selfa.scale2,0.1*selfa.scale2,l,100,100)
#             glutSolidCylinder(0.1*selfa.scale2, l, 100, 100)
             glPopMatrix()
             glPushMatrix()
             glTranslatef(v2[0], v2[1], v2[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             glutSolidCone(0.1*selfa.scale2*2.0, l/10.0, 100, 100)
             glPopMatrix()
           if gz==1:
             glColor3f(0.0,0.0,1.0)
             i=2
             glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.0,0.0,0.0,1.0])
             v2=np.zeros(3)
             v1=np.zeros(3)
             for j in range(0,3):
                v2[j]=tensor[i][j+1]*selfa.scale3*abs(smax3/smax)
                v1[j]=-1*tensor[i][j+1]*selfa.scale3*abs(smax3/smax)
             v2r = v2 - v1
             z = np.array([0.0, 0.0, 1.0])
             ax = np.cross(z, v2r)
             l = sqrt(np.dot(v2r, v2r))
             angle = 180.0 / np.pi * np.arccos(np.dot(z, v2r) / l)
             glPushMatrix()
             glTranslatef(v1[0], v1[1], v1[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             test=gluNewQuadric()
             gluCylinder(test,0.1*selfa.scale2,0.1*selfa.scale2,l,100,100)
#             glutSolidCylinder(0.1*selfa.scale2, l, 100, 100)
             glPopMatrix()
             glPushMatrix()
             glTranslatef(v2[0], v2[1], v2[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             glutSolidCone(0.1*selfa.scale2*2.0, l/10.0, 100, 100)
             glPopMatrix()
           glPopMatrix()           
#          glPushMatrix()
#          glRotatef(selfa.rotate_y,0.,1.,0.)
#          glRotatef(selfa.rotate_x,1.,0.,0.)
#          glRotatef(selfa.rotate_z,0.,0.,1.)
#          glLineWidth(2.0)
#          glDisable(GL_LIGHTING)
#          glBegin(GL_LINES)
#          if gx==1:
#             glColor3f(1.0,0.0,0.0)
#             glVertex3f(0.0,0.0,0.0)
#             i=0
#             glVertex3f(tensor[i][1]*selfa.scale,tensor[i][2]*selfa.scale,tensor[i][3]*selfa.scale)
#             glVertex3f(0.0,0.0,0.0)
#             glVertex3f(-1.*tensor[i][1]*selfa.scale,-1.*tensor[i][2]*selfa.scale,-1.*tensor[i][3]*selfa.scale)
#
#          if gy==1:
#             glColor3f(0.0,1.0,0.0)
#             glVertex3f(0.0,0.0,0.0)
#             i=1
#             glVertex3f(tensor[i][1]*selfa.scale,tensor[i][2]*selfa.scale,tensor[i][3]*selfa.scale)
#             glVertex3f(0.0,0.0,0.0)
#             glVertex3f(-1.*tensor[i][1]*selfa.scale,-1.*tensor[i][2]*selfa.scale,-1.*tensor[i][3]*selfa.scale)
#
#          if gz==1:
#             glColor3f(0.0,0.0,1.0)
#             glVertex3f(0.0,0.0,0.0)
#             i=2
#             glVertex3f(tensor[i][1]*selfa.scale,tensor[i][2]*selfa.scale,tensor[i][3]*selfa.scale)
#             glVertex3f(0.0,0.0,0.0)
#             glVertex3f(-1.*tensor[i][1]*selfa.scale,-1.*tensor[i][2]*selfa.scale,-1.*tensor[i][3]*selfa.scale)
#          glEnd()
#          glPopMatrix()
        if easy=='y':
         if gx+gy+gz>0:
           pos=pos+0.25
           pos2=pos
           glEnable( GL_LIGHTING )
           glLineWidth(2.0)
#           glCallList( tkList )
           glBegin(GL_LINES)
           glNormal3f(0., 0., +1.)
           if selfa.show_glegend==0:
             if gx==1:
               glColor3f(1.0,0.0,0.0)
               glVertex3f(3.0,pos2-0.25,0.0)
               glVertex3f(3.1,pos2-0.25,0.0)
               pos2=pos2-0.25
             if gy==1:
               glColor3f(0.0,1.0,0.0)
               glVertex3f(3.0,pos2-0.25,0.0)
               glVertex3f(3.1,pos2-0.25,0.0)
               pos2=pos2-0.25
             if gz==1:
               glColor3f(0.0,0.0,1.0)
               glVertex3f(3.0,pos2-0.25,0.0)
               glVertex3f(3.1,pos2-0.25,0.0)
               pos2=pos2-0.25
           glEnd()
           glCallList( tkList )
           #glDisable( GL_LIGHTING )
           glColor3f( 0, 0, 0 )
           if selfa.show_glegend==0:
             if gx==1:
               glRasterPos3f(3.25,pos-0.25,0.0)
               pos=pos-0.25
               for c in 'gX':
                     glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
             if gy==1:
               glRasterPos3f(3.25,pos-0.25,0.0)
               pos=pos-0.25
               for c in 'gY':
                     glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
             if gz==1:
               glRasterPos3f(3.25,pos-0.25,0.0)
               pos=pos-0.25
               for c in 'gZ':
                     glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
        glColor3f(0.0 ,0., 0.99)
        glDisable( GL_LIGHTING )
#        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
#        glEnable(GL_BLEND)
        glPushMatrix()
        glTranslatef(selfa.translatex,selfa.translatey,selfa.translatez)
        glRotatef(selfa.rotate_y,0.,1.,0.)
        glRotatef(selfa.rotate_x,1.,0.,0.)
        glRotatef(selfa.rotate_z,0.,0.,1.)
        glBegin(GL_QUADS)
        for i in range(0,len(tri3)):
#          glColor4f(color3[i][0] ,color3[i][1], color3[i][2], 0.6)
#          glVertex3f(tri3[i][0][0]*selfa.scale,tri3[i][0][1]*selfa.scale,tri3[i][0][2]*selfa.scale)
#          glColor4f(color3[i][3] ,color3[i][4], color3[i][5], 0.6)
#          glVertex3f(tri3[i][1][0]*selfa.scale,tri3[i][1][1]*selfa.scale,tri3[i][1][2]*selfa.scale)
#          glColor4f(color3[i][6] ,color3[i][7], color3[i][8], 0.6)
#          glVertex3f(tri3[i][2][0]*selfa.scale,tri3[i][2][1]*selfa.scale,tri3[i][2][2]*selfa.scale)
#          glColor4f(color3[i][9] ,color3[i][10], color3[i][11], 0.6)
#          glVertex3f(tri3[i][3][0]*selfa.scale,tri3[i][3][1]*selfa.scale,tri3[i][3][2]*selfa.scale)


          glColor3f(color3[i][0] ,color3[i][1], color3[i][2])
          glVertex3f(tri3[i][0][0]*selfa.scale,tri3[i][0][1]*selfa.scale,tri3[i][0][2]*selfa.scale)
          glColor3f(color3[i][3] ,color3[i][4], color3[i][5])
          glVertex3f(tri3[i][1][0]*selfa.scale,tri3[i][1][1]*selfa.scale,tri3[i][1][2]*selfa.scale)
          glColor3f(color3[i][6] ,color3[i][7], color3[i][8])
          glVertex3f(tri3[i][2][0]*selfa.scale,tri3[i][2][1]*selfa.scale,tri3[i][2][2]*selfa.scale)
          glColor3f(color3[i][9] ,color3[i][10], color3[i][11])
          glVertex3f(tri3[i][3][0]*selfa.scale,tri3[i][3][1]*selfa.scale,tri3[i][3][2]*selfa.scale)
        glEnd()
        glPopMatrix()

#        glRasterPos3f( 0.1, -2.1, 0 )
#        glPushMatrix()
#        glRotatef(selfa.rotate_y,0.,1.,0.)
#        glRotatef(selfa.rotate_x,1.,0.,0.)
#        glRotatef(selfa.rotate_z,0.,0.,1.)
        glBegin(GL_QUADS)
        pas=(smax3-smin3)/300.0
        for i in range(0,300):
          p=smin3+float(i)*pas
          f=(p-smin3)/(smax3-smin3)
          a=(1-f)/0.25
          X=int(a)
          Y=int(255*(a-X))
          if X==0:
                  r=255
                  g=Y
                  b=0
          elif X==1:
                  r=255-Y
                  g=255
                  b=0
          elif X==2:
                  r=0
                  g=255
                  b=Y
          elif X==3:
                  r=0
                  g=255-Y
                  b=255
          else:
                  r=0
                  g=0
                  b=255
          glColor3f(r/255.,g/255.,b/255.)
#          glVertex3f(3.0,0.0,0.0)
#          glVertex3f(3.2,0.0,0.0)
          glVertex3f(3.1,1.4+float((i-1)/150),0.0)
          glVertex3f(3.4,1.4+float((i-1)/150),0.0)
          glVertex3f(3.4,1.4+float(i/150),0.0)
          glVertex3f(3.1,1.4+float(i/150),0.0)
        glEnd()
#        glPopMatrix()


#        test=max(tri3)
#        print(test)

#        glPushMatrix()
#        glRotatef(selfa.rotate_y,0.,1.,0.)
#        glRotatef(selfa.rotate_x,1.,0.,0.)
#        glRotatef(selfa.rotate_z,0.,0.,1.)        
#        glLineWidth(2.0)
#        glBegin(GL_LINES)
#        glColor3f(0.,0.,0.)
#        glVertex3f(-3.5,-3.0,-3.0)
#        glVertex3f(-3.0,-3.0,-3.0)
##        glVertex3f(-3.0,-3.0*np.cos(selfa.rotate_x*2*np.pi/360.)+3.0*np.sin(selfa.rotate_x*2*np.pi/360.),-3.0*np.sin(selfa.rotate_x*2*np.pi/360.)-3.0*np.cos(selfa.rotate_x*2*np.pi/360.))
#        glVertex3f(-3.5,-3.0,-3.0)
#        glVertex3f(-3.5,-2.5,-3.0)
##        glVertex3f(-3.5*np.cos(selfa.rotate_y*2*np.pi/360.)-3.0*np.sin(selfa.rotate_y*2*np.pi/360.),-2.5,3.5*np.sin(selfa.rotate_y*2*np.pi/360.)-3.0*np.cos(selfa.rotate_y*2*np.pi/360.))
#        glVertex3f(-3.5,-3.0,-3.0)
#        glVertex3f(-3.5*np.cos(selfa.rotate_z*2*np.pi/360.)+3.0*np.sin(selfa.rotate_z*2*np.pi/360.),-3.5*np.sin(selfa.rotate_z*2*np.pi/360.)-3.0*np.cos(selfa.rotate_z*2*np.pi/360.),-2.5)
##        glVertex3f(-3.5,-3.0,-2.5)
#        glEnd()
#        glPopMatrix()
        if cartesian=='y' and selfa.show_cartesian==0:
          x=[[-3.5,-3.5,-3.5],[-3.0,-3.5,-3.5],[-3.5,-3.0,-3.5],[-3.5,-3.5,-3.0],[-2.9,-3.5,-3.5],[-3.5,-2.9,-3.5],[-3.5,-3.5,-2.9]]
            #rotation selons z
          for i in range(0,7):
            x[i][0]=x[i][0]*np.cos(selfa.rotate_z*np.pi/180.0)-x[i][1]*np.sin(selfa.rotate_z*np.pi/180.0)
            x[i][1]=x[i][0]*np.sin(selfa.rotate_z*np.pi/180.0)+x[i][1]*np.cos(selfa.rotate_z*np.pi/180.0)
            #rotation selons x
          for i in range(0,7):
            x[i][1]=x[i][1]*np.cos(selfa.rotate_x*np.pi/180.0)-x[i][2]*np.sin(selfa.rotate_x*np.pi/180.0)
            x[i][2]=x[i][1]*np.sin(selfa.rotate_x*np.pi/180.0)+x[i][2]*np.cos(selfa.rotate_x*np.pi/180.0)
            #rotation selons x
          for i in range(0,7):
            x[i][2]=x[i][2]*np.cos(selfa.rotate_y*np.pi/180.0)-x[i][0]*np.sin(selfa.rotate_y*np.pi/180.0)
            x[i][0]=x[i][2]*np.sin(selfa.rotate_y*np.pi/180.0)+x[i][0]*np.cos(selfa.rotate_y*np.pi/180.0)
          a=-3.5-x[0][0]
          b=-3.5-x[0][1]
          d=-3.5-x[0][2]
          glLineWidth(1.0)
          glBegin(GL_LINES)
          glColor3f(0.9,0.,0.)
          for i in range(0,4):
            glVertex3f(x[0][0]+a,x[0][1]+b,x[0][2]+d)
            glVertex3f(x[1][0]+a,x[1][1]+b,x[1][2]+d)
            glVertex3f(x[0][0]+a,x[0][1]+b,x[0][2]+d)
            glVertex3f(x[2][0]+a,x[2][1]+b,x[2][2]+d)
            glVertex3f(x[0][0]+a,x[0][1]+b,x[0][2]+d)
            glVertex3f(x[3][0]+a,x[3][1]+b,x[3][2]+d)
          glEnd()
        glCallList( tkList )
        glDisable( GL_LIGHTING )
        glColor3f( 0, 0, 0 )
        if cartesian=='y' and selfa.show_cartesian==0:
          glRasterPos3f(x[4][0]+a,x[4][1]+b,x[4][2]+d)
          for c in 'x': 
                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f(x[5][0]+a,x[5][1]+b,x[5][2]+d)
          for c in 'y':
                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f(x[6][0]+a,x[6][1]+b,x[6][2]+d)
          for c in 'z':
                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
        for i in range(0,len(str(smax3))):
         if str(smax3)[i]=='.':
           ssmax3=str(smax3)[0:i+3]
#        glRasterPos3f( 0.1, -2.1, 0 )
        for i in range(0,len(str(smin3))):
         if str(smin3)[i]=='.':
           ssmin3=str(smin3)[0:i+3]
        smoy=(smax3+smin3)/2.
        smoy2=(smin3+smoy)/2.
        smoy3=(smax3+smoy)/2.
        for i in range(0,len(str(selfa.scale))):
         if str(selfa.scale)[i]=='.':
           szoom=str(selfa.scale)[0:i+3]
        for i in range(0,len(str(selfa.rotate_x))):
         if str(selfa.rotate_x)[i]=='.':
           srotx=str(selfa.rotate_x)[0:i+3]
        for i in range(0,len(str(selfa.rotate_y))):
         if str(selfa.rotate_y)[i]=='.':
           sroty=str(selfa.rotate_y)[0:i+3]
        for i in range(0,len(str(selfa.rotate_z))):
         if str(selfa.rotate_z)[i]=='.':
           srotz=str(selfa.rotate_z)[0:i+3]
        for i in range(0,len(str(selfa.scale2))):
         if str(selfa.scale2)[i]=='.':
           szoom2=str(selfa.scale2)[0:i+3]
        for i in range(0,len(str(smoy))):
         if str(smoy)[i]=='.':
           ssmoy=str(smoy)[0:i+3]
        for i in range(0,len(str(smoy2))):
         if str(smoy2)[i]=='.':
           ssmoy2=str(smoy2)[0:i+3]
        for i in range(0,len(str(smoy3))):
         if str(smoy3)[i]=='.':
           ssmoy3=str(smoy3)[0:i+3]
        glRasterPos3f( 2.98, 1.45+300./150., 0 )
        for c in ssmax3:
                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
        glRasterPos3f( 2.98, 1.17, 0 )
        for c in ssmin3:
                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        glRasterPos3f( 3.05, 1.07+300./150., 0 )
#        for c in ssmax3:
#        	glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        glRasterPos3f( 3.05, 1.07, 0 )
#        for c in ssmin3:
#                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        glRasterPos3f( 3.05, 1.07+150./150., 0 )
#        for c in ssmoy:
#                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        glRasterPos3f( 3.05, 1.07+75./150., 0 )
#        for c in ssmoy2:
#                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        glRasterPos3f( 3.05, 1.07+225./150., 0 )
#        for c in ssmoy3:
#                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
        if selfa.show_zoomvalues==0:
          glRasterPos3f( 2.0, -2.4, 0 )
          for c in 'rotat x':
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 2.0, -2.6, 0 )
          for c in 'rotat x':
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 2.0, -2.8, 0 )
          for c in 'rotat z':
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          selfa.rotate_x
          glRasterPos3f( 2.0, -3.0, 0 )
          for c in 'zoom pot':
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 2.0, -3.2, 0 )
          for c in 'zoom mol':
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 3.05, -3.0, 0 )
          for c in szoom:
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 3.05, -3.2, 0 )
          for c in szoom2:
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 3.05, -2.4, 0 )
          for c in srotx:
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 3.05, -2.6, 0 )
          for c in sroty:
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 3.05, -2.8, 0 )
          for c in srotz:
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        pos=0.8
#        if atome=='y':
#           glEnable( GL_LIGHTING )
#           for i in range(0,len(atom_legend)):
#                glPushMatrix()
#                glTranslatef(3.15,0.85-(i*0.25), 0)
#                glColor3f(atom_legend[i][2][0],atom_legend[i][2][1],atom_legend[i][2][2])
#                glutSolidSphere(atom_legend[i][1]/3., 200,16)
#                glPopMatrix()
#                glRasterPos3f( 3.25, 0.8-(i*0.25), 0 )
#                pos=pos-0.25
#                for c in str.upper(atom_legend[i][0]):
#                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          # glEnable( GL_LIGHTING )
#        if easy=='y':
#           pos=pos+0.25
#           glEnable( GL_LIGHTING )
#           glLineWidth(4.0)
#           glBegin(GL_LINES)
#           glNormal3f(0., 0., +1.)
#           glColor3f(1.0,0.0,0.0)
#           glVertex3f(3.0,pos-0.25,0.0)
#           glVertex3f(3.1,pos-0.25,0.0)
#           glColor3f(0.0,1.0,0.0)
#           glVertex3f(3.0,pos-0.5,0.0)
#           glVertex3f(3.1,pos-0.5,0.0)
#           glColor3f(0.0,0.0,1.0)
#           glVertex3f(3.0,pos-0.75,0.0)
#           glVertex3f(3.1,pos-0.75,0.0)
#           glEnd()
#           glCallList( tkList )
#           glDisable( GL_LIGHTING )
#           glColor3f( 0, 0, 0 )
#           glRasterPos3f(3.25,pos-0.25,0.0)
#           for c in 'gX':
#                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#           glRasterPos3f(3.25,pos-0.5,0.0)
#           for c in 'gY':
#                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#           glRasterPos3f(3.25,pos-0.75,0.0)
#           for c in 'gZ':
#                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )

        maxi=0.0
#        print('atome=',atome)
        if atome=='y' or atome=='s' or atome=='ynh':
          glEnable(GL_LIGHTING)
          for i in range(0,len(extraction)):
            glPushMatrix()
            glTranslatef(selfa.translatex,selfa.translatey,selfa.translatez)
            glRotatef(selfa.rotate_y,0.,1.,0.)
            glRotatef(selfa.rotate_x,1.,0.,0.)
            glRotatef(selfa.rotate_z,0.,0.,1.)
            glColor3f(extraction[i][2][0],extraction[i][2][1],extraction[i][2][2])
            glTranslatef(extraction[i][0][0]*selfa.scale2,extraction[i][0][1]*selfa.scale2,extraction[i][0][2]*selfa.scale2)
            glutSolidSphere(extraction[i][1]*selfa.scale2, 200, 16)
#            quadratic = gluNewQuadric()
#            gluCylinder(quadratic, 3.0, 6.0, 5.0, 10, 10)
#            gluDisk(quadratic, INNER_RADIUS, OUTER_RADIUS, SLICES, LOOPS)
#            glutSolidCylinder(0.5,0.5,10,10)
            glPopMatrix()
#        glColor3f(0.0,0.0,0.0)
#        quadric=gluNewQuadric()
#        gluQuadricNormals(quadric, GLU_SMOOTH)
#        gluCylinder(quadric, radius, radius, 12.0, 32, 1)
#        gluQuadricOrientation(quadric,GLU_INSIDE)
          glDisable(GL_LIGHTING)
          glPushMatrix()
          glTranslatef(selfa.translatex,selfa.translatey,selfa.translatez)
          glRotatef(selfa.rotate_y,0.,1.,0.)
          glRotatef(selfa.rotate_x,1.,0.,0.)
          glRotatef(selfa.rotate_z,0.,0.,1.)
          glLineWidth(1.0)
          glColor3f( 0, 0, 0 )
#          glBegin(GL_LINES)
          for i in range(0,len(liaison)):
             glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.0,0.0,0.0,1.0])
             v2=np.zeros(3)
             v1=np.zeros(3)
             for j in range(0,3):
              v2[j]=extraction[liaison[i][0]][0][j]*selfa.scale2
              v1[j]=extraction[liaison[i][1]][0][j]*selfa.scale2
#             v2=[extraction[liaison[i][0]][0][0],extraction[liaison[i][0]][0][1],extraction[liaison[i][0]][0][2]]
#             v1=[extraction[liaison[j][0]][0][0],extraction[liaison[j][0]][0][1],extraction[liaison[j][0]][0][2]]
             v2r = v2 - v1
             z = np.array([0.0, 0.0, 1.0])
             ax = np.cross(z, v2r)
             l = sqrt(np.dot(v2r, v2r))
             angle = 180.0 / np.pi * np.arccos(np.dot(z, v2r) / l)
             glPushMatrix()
             glTranslatef(v1[0], v1[1], v1[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             test=gluNewQuadric()
             gluCylinder(test,0.05*selfa.scale2,0.05*selfa.scale2,l,100,100)
            # glutSolidCylinder(0.05*selfa.scale2, l, 100, 100)
             glPopMatrix()
#            glVertex3f(extraction[liaison[i][0]][0][0]*selfa.scale2,extraction[liaison[i][0]][0][1]*selfa.scale2,extraction[liaison[i][0]][0][2]*selfa.scale2)
#            glVertex3f(extraction[liaison[i][1]][0][0]*selfa.scale2,extraction[liaison[i][1]][0][1]*selfa.scale2,extraction[liaison[i][1]][0][2]*selfa.scale2)
#          glEnd()
          glPopMatrix()

#        if easy=='y':
#          glPushMatrix()
#          glRotatef(selfa.rotate_y,0.,1.,0.)
#          glRotatef(selfa.rotate_x,1.,0.,0.)
#          glRotatef(selfa.rotate_z,0.,0.,1.)
#          glLineWidth(4.0)
#          glDisable(GL_LIGHTING)
#          glBegin(GL_LINES)
#          for i in range(0,3):
#             glNormal3f(0., 0., +1.)
#             if i==0: glColor3f(0.9,0.0,0.0)
#             elif i==1: glColor3f(0.0,0.9,0.0)
#             else: glColor3f(0.0,0.0,0.9)
#             glVertex3f(0.0,0.0,0.0)
#             glVertex3f(tensor[i][1]*selfa.scale,tensor[i][2]*selfa.scale,tensor[i][3]*selfa.scale)
#             glVertex3f(0.0,0.0,0.0)
#             glVertex3f(-1.*tensor[i][1]*selfa.scale,-1.*tensor[i][2]*selfa.scale,-1.*tensor[i][3]*selfa.scale)
#          glEnd()
#          glPopMatrix()
        glDisable(GL_LIGHTING)
#        glEnable(GL_LIGHTING)
        glMatrixMode(GL_MODELVIEW)
        glFlush()
        glutSwapBuffers()
        return
    def draw_half2(selfa):
        glutPostRedisplay()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        pos=0.8
        if atome=='y' or atome=='s' or atome=='ynh':
           glEnable( GL_LIGHTING )
           if selfa.show_atlegend==0: 
             for i in range(0,len(atom_legend)):
                glPushMatrix()
                glTranslatef(3.15,0.85-(i*0.25), 0)
                glColor3f(atom_legend[i][2][0],atom_legend[i][2][1],atom_legend[i][2][2])
                glutSolidSphere(atom_legend[i][1]/3., 200,16)
                glPopMatrix()
                glRasterPos3f( 3.25, 0.8-(i*0.25), 0 )
                pos=pos-0.25
                for c in str.upper(atom_legend[i][0]):
                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
        if easy=='y':
         if gx+gy+gz>0:
           glPushMatrix()
           glTranslatef(selfa.translatex,selfa.translatey,selfa.translatez)
           glRotatef(selfa.rotate_y,0.,1.,0.)
           glRotatef(selfa.rotate_x,1.,0.,0.)
           glRotatef(selfa.rotate_z,0.,0.,1.)           
           if gx==1:
             glColor3f(1.0,0.0,0.0)
             i=0
             glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.0,0.0,0.0,1.0])
             v2=np.zeros(3)
             v1=np.zeros(3)
             for j in range(0,3):
                v2[j]=tensor[i][j+1]*selfa.scale3*abs(smax2/smax)
                v1[j]=-1*tensor[i][j+1]*selfa.scale3*abs(smax2/smax)
             v2r = v2 - v1
             z = np.array([0.0, 0.0, 1.0])
             ax = np.cross(z, v2r)
             l = sqrt(np.dot(v2r, v2r))
             angle = 180.0 / np.pi * np.arccos(np.dot(z, v2r) / l)
             glPushMatrix()
             glTranslatef(v1[0], v1[1], v1[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             test=gluNewQuadric()
             gluCylinder(test,0.1*selfa.scale2,0.1*selfa.scale2,l,100,100)
             #glutSolidCylinder(0.1*selfa.scale2, l, 100, 100)
             glPopMatrix()

             glPushMatrix()
             glTranslatef(v2[0], v2[1], v2[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             glutSolidCone(0.1*selfa.scale2*2.0, l/10.0, 100, 100)
             glPopMatrix()
           if gy==1:
             glColor3f(0.0,1.0,0.0)
             i=1
             glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.0,0.0,0.0,1.0])
             v2=np.zeros(3)
             v1=np.zeros(3)
             for j in range(0,3):
                v2[j]=tensor[i][j+1]*selfa.scale3*abs(smax2/smax)
                v1[j]=-1*tensor[i][j+1]*selfa.scale3*abs(smax2/smax)
             v2r = v2 - v1
             z = np.array([0.0, 0.0, 1.0])
             ax = np.cross(z, v2r)
             l = sqrt(np.dot(v2r, v2r))
             angle = 180.0 / np.pi * np.arccos(np.dot(z, v2r) / l)
             glPushMatrix()
             glTranslatef(v1[0], v1[1], v1[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             test=gluNewQuadric()
             gluCylinder(test,0.1*selfa.scale2,0.1*selfa.scale2,l,100,100)
             #glutSolidCylinder(0.1*selfa.scale2, l, 100, 100)
             glPopMatrix()
             glPushMatrix()
             glTranslatef(v2[0], v2[1], v2[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             glutSolidCone(0.1*selfa.scale2*2.0, l/10.0, 100, 100)
             glPopMatrix()
           if gz==1:
             glColor3f(0.0,0.0,1.0)
             i=2
             glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.0,0.0,0.0,1.0])
             v2=np.zeros(3)
             v1=np.zeros(3)
             for j in range(0,3):
                v2[j]=tensor[i][j+1]*selfa.scale3*abs(smax2/smax)
                v1[j]=-1*tensor[i][j+1]*selfa.scale3*abs(smax2/smax)
             v2r = v2 - v1
             z = np.array([0.0, 0.0, 1.0])
             ax = np.cross(z, v2r)
             l = sqrt(np.dot(v2r, v2r))
             angle = 180.0 / np.pi * np.arccos(np.dot(z, v2r) / l)
             glPushMatrix()
             glTranslatef(v1[0], v1[1], v1[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             test=gluNewQuadric()
             gluCylinder(test,0.1*selfa.scale2,0.1*selfa.scale2,l,100,100)
             #glutSolidCylinder(0.1*selfa.scale2, l, 100, 100)
             glPopMatrix()
             glPushMatrix()
             glTranslatef(v2[0], v2[1], v2[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             glutSolidCone(0.1*selfa.scale2*2.0, l/10.0, 100, 100)
             glPopMatrix()
           glPopMatrix()           
#          glPushMatrix()
#          glRotatef(selfa.rotate_y,0.,1.,0.)
#          glRotatef(selfa.rotate_x,1.,0.,0.)
#          glRotatef(selfa.rotate_z,0.,0.,1.)
#          glLineWidth(2.0)
#          glDisable(GL_LIGHTING)
#          glBegin(GL_LINES)
#          if gx==1:
#             glColor3f(1.0,0.0,0.0)
#             glVertex3f(0.0,0.0,0.0)
#             i=0
#             glVertex3f(tensor[i][1]*selfa.scale,tensor[i][2]*selfa.scale,tensor[i][3]*selfa.scale)
#             glVertex3f(0.0,0.0,0.0)
#             glVertex3f(-1.*tensor[i][1]*selfa.scale,-1.*tensor[i][2]*selfa.scale,-1.*tensor[i][3]*selfa.scale)
#
#          if gy==1:
#             glColor3f(0.0,1.0,0.0)
#             glVertex3f(0.0,0.0,0.0)
#             i=1
#             glVertex3f(tensor[i][1]*selfa.scale,tensor[i][2]*selfa.scale,tensor[i][3]*selfa.scale)
#             glVertex3f(0.0,0.0,0.0)
#             glVertex3f(-1.*tensor[i][1]*selfa.scale,-1.*tensor[i][2]*selfa.scale,-1.*tensor[i][3]*selfa.scale)
#
#          if gz==1:
#             glColor3f(0.0,0.0,1.0)
#             glVertex3f(0.0,0.0,0.0)
#             i=2
#             glVertex3f(tensor[i][1]*selfa.scale,tensor[i][2]*selfa.scale,tensor[i][3]*selfa.scale)
#             glVertex3f(0.0,0.0,0.0)
#             glVertex3f(-1.*tensor[i][1]*selfa.scale,-1.*tensor[i][2]*selfa.scale,-1.*tensor[i][3]*selfa.scale)
#          glEnd()
#          glPopMatrix()
        if easy=='y':
         if gx+gy+gz>0:
           pos=pos+0.25
           pos2=pos
           glEnable( GL_LIGHTING )
           glLineWidth(2.0)
#           glCallList( tkList )
           glBegin(GL_LINES)
           glNormal3f(0., 0., +1.)
           if selfa.show_glegend==0:
             if gx==1:
               glColor3f(1.0,0.0,0.0)
               glVertex3f(3.0,pos2-0.25,0.0)
               glVertex3f(3.1,pos2-0.25,0.0)
               pos2=pos2-0.25
             if gy==1:
               glColor3f(0.0,1.0,0.0)
               glVertex3f(3.0,pos2-0.25,0.0)
               glVertex3f(3.1,pos2-0.25,0.0)
               pos2=pos2-0.25
             if gz==1:
               glColor3f(0.0,0.0,1.0)
               glVertex3f(3.0,pos2-0.25,0.0)
               glVertex3f(3.1,pos2-0.25,0.0)
               pos2=pos2-0.25
           glEnd()
           glCallList( tkList )
           #glDisable( GL_LIGHTING )
           glColor3f( 0, 0, 0 )
           if selfa.show_glegend==0:
             if gx==1:
               glRasterPos3f(3.25,pos-0.25,0.0)
               pos=pos-0.25
               for c in 'gX':
                     glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
             if gy==1:
               glRasterPos3f(3.25,pos-0.25,0.0)
               pos=pos-0.25
               for c in 'gY':
                     glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
             if gz==1:
               glRasterPos3f(3.25,pos-0.25,0.0)
               pos=pos-0.25
               for c in 'gZ':
                     glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
        glColor3f(0.0 ,0., 0.99)
        glDisable( GL_LIGHTING )
#        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
#        glEnable(GL_BLEND)
        glPushMatrix()
        glTranslatef(selfa.translatex,selfa.translatey,selfa.translatez)
        glRotatef(selfa.rotate_y,0.,1.,0.)
        glRotatef(selfa.rotate_x,1.,0.,0.)
        glRotatef(selfa.rotate_z,0.,0.,1.)
        glBegin(GL_QUADS)
        for i in range(0,len(tri2)):
#          glColor4f(color2[i][0] ,color2[i][1], color2[i][2], 0.6)
#          glVertex3f(tri2[i][0][0]*selfa.scale,tri2[i][0][1]*selfa.scale,tri2[i][0][2]*selfa.scale)
#          glColor4f(color2[i][3] ,color2[i][4], color2[i][5], 0.6)
#          glVertex3f(tri2[i][1][0]*selfa.scale,tri2[i][1][1]*selfa.scale,tri2[i][1][2]*selfa.scale)
#          glColor4f(color2[i][6] ,color2[i][7], color2[i][8], 0.6)
#          glVertex3f(tri2[i][2][0]*selfa.scale,tri2[i][2][1]*selfa.scale,tri2[i][2][2]*selfa.scale)
#          glColor4f(color2[i][9] ,color2[i][10], color2[i][11], 0.6)
#          glVertex3f(tri2[i][3][0]*selfa.scale,tri2[i][3][1]*selfa.scale,tri2[i][3][2]*selfa.scale)


          glColor3f(color2[i][0] ,color2[i][1], color2[i][2])
          glVertex3f(tri2[i][0][0]*selfa.scale,tri2[i][0][1]*selfa.scale,tri2[i][0][2]*selfa.scale)
          glColor3f(color2[i][3] ,color2[i][4], color2[i][5])
          glVertex3f(tri2[i][1][0]*selfa.scale,tri2[i][1][1]*selfa.scale,tri2[i][1][2]*selfa.scale)
          glColor3f(color2[i][6] ,color2[i][7], color2[i][8])
          glVertex3f(tri2[i][2][0]*selfa.scale,tri2[i][2][1]*selfa.scale,tri2[i][2][2]*selfa.scale)
          glColor3f(color2[i][9] ,color2[i][10], color2[i][11])
          glVertex3f(tri2[i][3][0]*selfa.scale,tri2[i][3][1]*selfa.scale,tri2[i][3][2]*selfa.scale)
        glEnd()
        glPopMatrix()

#        glRasterPos3f( 0.1, -2.1, 0 )
#        glPushMatrix()
#        glRotatef(selfa.rotate_y,0.,1.,0.)
#        glRotatef(selfa.rotate_x,1.,0.,0.)
#        glRotatef(selfa.rotate_z,0.,0.,1.)
        glBegin(GL_QUADS)
        pas=(smax2-smin2)/300.0
        for i in range(0,300):
          p=smin2+float(i)*pas
          f=(p-smin2)/(smax2-smin2)
          a=(1-f)/0.25
          X=int(a)
          Y=int(255*(a-X))
          if X==0:
                  r=255
                  g=Y
                  b=0
          elif X==1:
                  r=255-Y
                  g=255
                  b=0
          elif X==2:
                  r=0
                  g=255
                  b=Y
          elif X==3:
                  r=0
                  g=255-Y
                  b=255
          else:
                  r=0
                  g=0
                  b=255
          glColor3f(r/255.,g/255.,b/255.)
#          glVertex3f(3.0,0.0,0.0)
#          glVertex3f(3.2,0.0,0.0)
          glVertex3f(3.1,1.4+float((i-1)/150),0.0)
          glVertex3f(3.4,1.4+float((i-1)/150),0.0)
          glVertex3f(3.4,1.4+float(i/150),0.0)
          glVertex3f(3.1,1.4+float(i/150),0.0)
        glEnd()
#        glPopMatrix()


#        test=max(tri2)
#        print(test)

#        glPushMatrix()
#        glRotatef(selfa.rotate_y,0.,1.,0.)
#        glRotatef(selfa.rotate_x,1.,0.,0.)
#        glRotatef(selfa.rotate_z,0.,0.,1.)        
#        glLineWidth(2.0)
#        glBegin(GL_LINES)
#        glColor3f(0.,0.,0.)
#        glVertex3f(-3.5,-3.0,-3.0)
#        glVertex3f(-3.0,-3.0,-3.0)
##        glVertex3f(-3.0,-3.0*np.cos(selfa.rotate_x*2*np.pi/360.)+3.0*np.sin(selfa.rotate_x*2*np.pi/360.),-3.0*np.sin(selfa.rotate_x*2*np.pi/360.)-3.0*np.cos(selfa.rotate_x*2*np.pi/360.))
#        glVertex3f(-3.5,-3.0,-3.0)
#        glVertex3f(-3.5,-2.5,-3.0)
##        glVertex3f(-3.5*np.cos(selfa.rotate_y*2*np.pi/360.)-3.0*np.sin(selfa.rotate_y*2*np.pi/360.),-2.5,3.5*np.sin(selfa.rotate_y*2*np.pi/360.)-3.0*np.cos(selfa.rotate_y*2*np.pi/360.))
#        glVertex3f(-3.5,-3.0,-3.0)
#        glVertex3f(-3.5*np.cos(selfa.rotate_z*2*np.pi/360.)+3.0*np.sin(selfa.rotate_z*2*np.pi/360.),-3.5*np.sin(selfa.rotate_z*2*np.pi/360.)-3.0*np.cos(selfa.rotate_z*2*np.pi/360.),-2.5)
##        glVertex3f(-3.5,-3.0,-2.5)
#        glEnd()
#        glPopMatrix()
        if cartesian=='y' and selfa.show_cartesian==0:
          x=[[-3.5,-3.5,-3.5],[-3.0,-3.5,-3.5],[-3.5,-3.0,-3.5],[-3.5,-3.5,-3.0],[-2.9,-3.5,-3.5],[-3.5,-2.9,-3.5],[-3.5,-3.5,-2.9]]
            #rotation selons z
          for i in range(0,7):
            x[i][0]=x[i][0]*np.cos(selfa.rotate_z*np.pi/180.0)-x[i][1]*np.sin(selfa.rotate_z*np.pi/180.0)
            x[i][1]=x[i][0]*np.sin(selfa.rotate_z*np.pi/180.0)+x[i][1]*np.cos(selfa.rotate_z*np.pi/180.0)
            #rotation selons x
          for i in range(0,7):
            x[i][1]=x[i][1]*np.cos(selfa.rotate_x*np.pi/180.0)-x[i][2]*np.sin(selfa.rotate_x*np.pi/180.0)
            x[i][2]=x[i][1]*np.sin(selfa.rotate_x*np.pi/180.0)+x[i][2]*np.cos(selfa.rotate_x*np.pi/180.0)
            #rotation selons x
          for i in range(0,7):
            x[i][2]=x[i][2]*np.cos(selfa.rotate_y*np.pi/180.0)-x[i][0]*np.sin(selfa.rotate_y*np.pi/180.0)
            x[i][0]=x[i][2]*np.sin(selfa.rotate_y*np.pi/180.0)+x[i][0]*np.cos(selfa.rotate_y*np.pi/180.0)
          a=-3.5-x[0][0]
          b=-3.5-x[0][1]
          d=-3.5-x[0][2]
          glLineWidth(1.0)
          glBegin(GL_LINES)
          glColor3f(0.9,0.,0.)
          for i in range(0,4):
            glVertex3f(x[0][0]+a,x[0][1]+b,x[0][2]+d)
            glVertex3f(x[1][0]+a,x[1][1]+b,x[1][2]+d)
            glVertex3f(x[0][0]+a,x[0][1]+b,x[0][2]+d)
            glVertex3f(x[2][0]+a,x[2][1]+b,x[2][2]+d)
            glVertex3f(x[0][0]+a,x[0][1]+b,x[0][2]+d)
            glVertex3f(x[3][0]+a,x[3][1]+b,x[3][2]+d)
          glEnd()
        glCallList( tkList )
        glDisable( GL_LIGHTING )
        glColor3f( 0, 0, 0 )
        if cartesian=='y' and selfa.show_cartesian==0:
          glRasterPos3f(x[4][0]+a,x[4][1]+b,x[4][2]+d)
          for c in 'x': 
                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f(x[5][0]+a,x[5][1]+b,x[5][2]+d)
          for c in 'y':
                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f(x[6][0]+a,x[6][1]+b,x[6][2]+d)
          for c in 'z':
                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
        for i in range(0,len(str(smax2))):
         if str(smax2)[i]=='.':
           ssmax2=str(smax2)[0:i+3]
#        glRasterPos3f( 0.1, -2.1, 0 )
        for i in range(0,len(str(smin2))):
         if str(smin2)[i]=='.':
           ssmin2=str(smin2)[0:i+3]
        smoy=(smax2+smin2)/2.
        smoy2=(smin2+smoy)/2.
        smoy3=(smax2+smoy)/2.
        for i in range(0,len(str(selfa.scale))):
         if str(selfa.scale)[i]=='.':
           szoom=str(selfa.scale)[0:i+3]
        for i in range(0,len(str(selfa.rotate_x))):
         if str(selfa.rotate_x)[i]=='.':
           srotx=str(selfa.rotate_x)[0:i+3]
        for i in range(0,len(str(selfa.rotate_y))):
         if str(selfa.rotate_y)[i]=='.':
           sroty=str(selfa.rotate_y)[0:i+3]
        for i in range(0,len(str(selfa.rotate_z))):
         if str(selfa.rotate_z)[i]=='.':
           srotz=str(selfa.rotate_z)[0:i+3]
        for i in range(0,len(str(selfa.scale2))):
         if str(selfa.scale2)[i]=='.':
           szoom2=str(selfa.scale2)[0:i+3]
        for i in range(0,len(str(smoy))):
         if str(smoy)[i]=='.':
           ssmoy=str(smoy)[0:i+3]
        for i in range(0,len(str(smoy2))):
         if str(smoy2)[i]=='.':
           ssmoy2=str(smoy2)[0:i+3]
        for i in range(0,len(str(smoy3))):
         if str(smoy3)[i]=='.':
           ssmoy3=str(smoy3)[0:i+3]
        glRasterPos3f( 2.98, 1.45+300./150., 0 )
        for c in ssmax2:
                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
        glRasterPos3f( 2.98, 1.17, 0 )
        for c in ssmin2:
                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        glRasterPos3f( 3.05, 1.07+300./150., 0 )
#        for c in ssmax2:
#        	glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        glRasterPos3f( 3.05, 1.07, 0 )
#        for c in ssmin2:
#                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        glRasterPos3f( 3.05, 1.07+150./150., 0 )
#        for c in ssmoy:
#                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        glRasterPos3f( 3.05, 1.07+75./150., 0 )
#        for c in ssmoy2:
#                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        glRasterPos3f( 3.05, 1.07+225./150., 0 )
#        for c in ssmoy3:
#                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
        if selfa.show_zoomvalues==0:
          glRasterPos3f( 2.0, -2.4, 0 )
          for c in 'rotat x':
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 2.0, -2.6, 0 )
          for c in 'rotat x':
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 2.0, -2.8, 0 )
          for c in 'rotat z':
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          selfa.rotate_x
          glRasterPos3f( 2.0, -3.0, 0 )
          for c in 'zoom pot':
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 2.0, -3.2, 0 )
          for c in 'zoom mol':
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 3.05, -3.0, 0 )
          for c in szoom:
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 3.05, -3.2, 0 )
          for c in szoom2:
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 3.05, -2.4, 0 )
          for c in srotx:
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 3.05, -2.6, 0 )
          for c in sroty:
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 3.05, -2.8, 0 )
          for c in srotz:
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        pos=0.8
#        if atome=='y':
#           glEnable( GL_LIGHTING )
#           for i in range(0,len(atom_legend)):
#                glPushMatrix()
#                glTranslatef(3.15,0.85-(i*0.25), 0)
#                glColor3f(atom_legend[i][2][0],atom_legend[i][2][1],atom_legend[i][2][2])
#                glutSolidSphere(atom_legend[i][1]/3., 200,16)
#                glPopMatrix()
#                glRasterPos3f( 3.25, 0.8-(i*0.25), 0 )
#                pos=pos-0.25
#                for c in str.upper(atom_legend[i][0]):
#                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          # glEnable( GL_LIGHTING )
#        if easy=='y':
#           pos=pos+0.25
#           glEnable( GL_LIGHTING )
#           glLineWidth(4.0)
#           glBegin(GL_LINES)
#           glNormal3f(0., 0., +1.)
#           glColor3f(1.0,0.0,0.0)
#           glVertex3f(3.0,pos-0.25,0.0)
#           glVertex3f(3.1,pos-0.25,0.0)
#           glColor3f(0.0,1.0,0.0)
#           glVertex3f(3.0,pos-0.5,0.0)
#           glVertex3f(3.1,pos-0.5,0.0)
#           glColor3f(0.0,0.0,1.0)
#           glVertex3f(3.0,pos-0.75,0.0)
#           glVertex3f(3.1,pos-0.75,0.0)
#           glEnd()
#           glCallList( tkList )
#           glDisable( GL_LIGHTING )
#           glColor3f( 0, 0, 0 )
#           glRasterPos3f(3.25,pos-0.25,0.0)
#           for c in 'gX':
#                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#           glRasterPos3f(3.25,pos-0.5,0.0)
#           for c in 'gY':
#                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#           glRasterPos3f(3.25,pos-0.75,0.0)
#           for c in 'gZ':
#                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )

        maxi=0.0
#        print('atome=',atome)
        if atome=='y' or atome=='s' or atome=='ynh':
          glEnable(GL_LIGHTING)
          for i in range(0,len(extraction)):
            glPushMatrix()
            glTranslatef(selfa.translatex,selfa.translatey,selfa.translatez)
            glRotatef(selfa.rotate_y,0.,1.,0.)
            glRotatef(selfa.rotate_x,1.,0.,0.)
            glRotatef(selfa.rotate_z,0.,0.,1.)
            glColor3f(extraction[i][2][0],extraction[i][2][1],extraction[i][2][2])
            glTranslatef(extraction[i][0][0]*selfa.scale2,extraction[i][0][1]*selfa.scale2,extraction[i][0][2]*selfa.scale2)
            glutSolidSphere(extraction[i][1]*selfa.scale2, 200, 16)
#            quadratic = gluNewQuadric()
#            gluCylinder(quadratic, 3.0, 6.0, 5.0, 10, 10)
#            gluDisk(quadratic, INNER_RADIUS, OUTER_RADIUS, SLICES, LOOPS)
#            glutSolidCylinder(0.5,0.5,10,10)
            glPopMatrix()
#        glColor3f(0.0,0.0,0.0)
#        quadric=gluNewQuadric()
#        gluQuadricNormals(quadric, GLU_SMOOTH)
#        gluCylinder(quadric, radius, radius, 12.0, 32, 1)
#        gluQuadricOrientation(quadric,GLU_INSIDE)
          glDisable(GL_LIGHTING)
          glPushMatrix()
          glTranslatef(selfa.translatex,selfa.translatey,selfa.translatez)
          glRotatef(selfa.rotate_y,0.,1.,0.)
          glRotatef(selfa.rotate_x,1.,0.,0.)
          glRotatef(selfa.rotate_z,0.,0.,1.)
          glLineWidth(1.0)
          glColor3f( 0, 0, 0 )
#          glBegin(GL_LINES)
          for i in range(0,len(liaison)):
             glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.0,0.0,0.0,1.0])
             v2=np.zeros(3)
             v1=np.zeros(3)
             for j in range(0,3):
              v2[j]=extraction[liaison[i][0]][0][j]*selfa.scale2
              v1[j]=extraction[liaison[i][1]][0][j]*selfa.scale2
#             v2=[extraction[liaison[i][0]][0][0],extraction[liaison[i][0]][0][1],extraction[liaison[i][0]][0][2]]
#             v1=[extraction[liaison[j][0]][0][0],extraction[liaison[j][0]][0][1],extraction[liaison[j][0]][0][2]]
             v2r = v2 - v1
             z = np.array([0.0, 0.0, 1.0])
             ax = np.cross(z, v2r)
             l = sqrt(np.dot(v2r, v2r))
             angle = 180.0 / np.pi * np.arccos(np.dot(z, v2r) / l)
             glPushMatrix()
             glTranslatef(v1[0], v1[1], v1[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             test=gluNewQuadric()
             gluCylinder(test,0.05*selfa.scale2,0.05*selfa.scale2,l,100,100)
             #glutSolidCylinder(0.05*selfa.scale2, l, 100, 100)
             glPopMatrix()
#            glVertex3f(extraction[liaison[i][0]][0][0]*selfa.scale2,extraction[liaison[i][0]][0][1]*selfa.scale2,extraction[liaison[i][0]][0][2]*selfa.scale2)
#            glVertex3f(extraction[liaison[i][1]][0][0]*selfa.scale2,extraction[liaison[i][1]][0][1]*selfa.scale2,extraction[liaison[i][1]][0][2]*selfa.scale2)
#          glEnd()
          glPopMatrix()

#        if easy=='y':
#          glPushMatrix()
#          glRotatef(selfa.rotate_y,0.,1.,0.)
#          glRotatef(selfa.rotate_x,1.,0.,0.)
#          glRotatef(selfa.rotate_z,0.,0.,1.)
#          glLineWidth(4.0)
#          glDisable(GL_LIGHTING)
#          glBegin(GL_LINES)
#          for i in range(0,3):
#             glNormal3f(0., 0., +1.)
#             if i==0: glColor3f(0.9,0.0,0.0)
#             elif i==1: glColor3f(0.0,0.9,0.0)
#             else: glColor3f(0.0,0.0,0.9)
#             glVertex3f(0.0,0.0,0.0)
#             glVertex3f(tensor[i][1]*selfa.scale,tensor[i][2]*selfa.scale,tensor[i][3]*selfa.scale)
#             glVertex3f(0.0,0.0,0.0)
#             glVertex3f(-1.*tensor[i][1]*selfa.scale,-1.*tensor[i][2]*selfa.scale,-1.*tensor[i][3]*selfa.scale)
#          glEnd()
#          glPopMatrix()
        glDisable(GL_LIGHTING)
#        glEnable(GL_LIGHTING)
        glMatrixMode(GL_MODELVIEW)
        glFlush()
        glutSwapBuffers()
        return
    def draw_half(selfa):
        glutPostRedisplay()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        pos=0.8
        if atome=='y' or atome=='s' or atome=='ynh':
           glEnable( GL_LIGHTING )
           if selfa.show_atlegend==0: 
             for i in range(0,len(atom_legend)):
                glPushMatrix()
                glTranslatef(3.15,0.85-(i*0.25), 0)
                glColor3f(atom_legend[i][2][0],atom_legend[i][2][1],atom_legend[i][2][2])
                glutSolidSphere(atom_legend[i][1]/3., 200,16)
                glPopMatrix()
                glRasterPos3f( 3.25, 0.8-(i*0.25), 0 )
                pos=pos-0.25
                for c in str.upper(atom_legend[i][0]):
                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
        if easy=='y':
         if gx+gy+gz>0:
           glPushMatrix()
           glTranslatef(selfa.translatex,selfa.translatey,selfa.translatez)
           glRotatef(selfa.rotate_y,0.,1.,0.)
           glRotatef(selfa.rotate_x,1.,0.,0.)
           glRotatef(selfa.rotate_z,0.,0.,1.)           
           if gx==1:
             glColor3f(1.0,0.0,0.0)
             i=0
             glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.0,0.0,0.0,1.0])
             v2=np.zeros(3)
             v1=np.zeros(3)
             for j in range(0,3):
                v2[j]=tensor[i][j+1]*selfa.scale3
                v1[j]=-1*tensor[i][j+1]*selfa.scale3
             v2r = v2 - v1
             z = np.array([0.0, 0.0, 1.0])
             ax = np.cross(z, v2r)
             l = sqrt(np.dot(v2r, v2r))
             angle = 180.0 / np.pi * np.arccos(np.dot(z, v2r) / l)
             glPushMatrix()
             glTranslatef(v1[0], v1[1], v1[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             test=gluNewQuadric()
             gluCylinder(test,0.1*selfa.scale2,0.1*selfa.scale2,l,100,100)
             #glutSolidCylinder(0.1*selfa.scale2, l, 100, 100)
             glPopMatrix()

             glPushMatrix()
             glTranslatef(v2[0], v2[1], v2[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             glutSolidCone(0.1*selfa.scale2*2.0, l/10.0, 100, 100)
             glPopMatrix()
           if gy==1:
             glColor3f(0.0,1.0,0.0)
             i=1
             glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.0,0.0,0.0,1.0])
             v2=np.zeros(3)
             v1=np.zeros(3)
             for j in range(0,3):
                v2[j]=tensor[i][j+1]*selfa.scale3
                v1[j]=-1*tensor[i][j+1]*selfa.scale3
             v2r = v2 - v1
             z = np.array([0.0, 0.0, 1.0])
             ax = np.cross(z, v2r)
             l = sqrt(np.dot(v2r, v2r))
             angle = 180.0 / np.pi * np.arccos(np.dot(z, v2r) / l)
             glPushMatrix()
             glTranslatef(v1[0], v1[1], v1[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             test=gluNewQuadric()
             gluCylinder(test,0.1*selfa.scale2,0.1*selfa.scale2,l,100,100)
             #glutSolidCylinder(0.1*selfa.scale2, l, 100, 100)
             glPopMatrix()
             glPushMatrix()
             glTranslatef(v2[0], v2[1], v2[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             glutSolidCone(0.1*selfa.scale2*2.0, l/10.0, 100, 100)
             glPopMatrix()
           if gz==1:
             glColor3f(0.0,0.0,1.0)
             i=2
             glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.0,0.0,0.0,1.0])
             v2=np.zeros(3)
             v1=np.zeros(3)
             for j in range(0,3):
                v2[j]=tensor[i][j+1]*selfa.scale3
                v1[j]=-1*tensor[i][j+1]*selfa.scale3
             v2r = v2 - v1
             z = np.array([0.0, 0.0, 1.0])
             ax = np.cross(z, v2r)
             l = sqrt(np.dot(v2r, v2r))
             angle = 180.0 / np.pi * np.arccos(np.dot(z, v2r) / l)
             glPushMatrix()
             glTranslatef(v1[0], v1[1], v1[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             test=gluNewQuadric()
             gluCylinder(test,0.1*selfa.scale2,0.1*selfa.scale2,l,100,100)
             #glutSolidCylinder(0.1*selfa.scale2, l, 100, 100)
             glPopMatrix()
             glPushMatrix()
             glTranslatef(v2[0], v2[1], v2[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             glutSolidCone(0.1*selfa.scale2*2.0, l/10.0, 100, 100)
             glPopMatrix()
           glPopMatrix()           
#          glPushMatrix()
#          glRotatef(selfa.rotate_y,0.,1.,0.)
#          glRotatef(selfa.rotate_x,1.,0.,0.)
#          glRotatef(selfa.rotate_z,0.,0.,1.)
#          glLineWidth(2.0)
#          glDisable(GL_LIGHTING)
#          glBegin(GL_LINES)
#          if gx==1:
#             glColor3f(1.0,0.0,0.0)
#             glVertex3f(0.0,0.0,0.0)
#             i=0
#             glVertex3f(tensor[i][1]*selfa.scale,tensor[i][2]*selfa.scale,tensor[i][3]*selfa.scale)
#             glVertex3f(0.0,0.0,0.0)
#             glVertex3f(-1.*tensor[i][1]*selfa.scale,-1.*tensor[i][2]*selfa.scale,-1.*tensor[i][3]*selfa.scale)
#
#          if gy==1:
#             glColor3f(0.0,1.0,0.0)
#             glVertex3f(0.0,0.0,0.0)
#             i=1
#             glVertex3f(tensor[i][1]*selfa.scale,tensor[i][2]*selfa.scale,tensor[i][3]*selfa.scale)
#             glVertex3f(0.0,0.0,0.0)
#             glVertex3f(-1.*tensor[i][1]*selfa.scale,-1.*tensor[i][2]*selfa.scale,-1.*tensor[i][3]*selfa.scale)
#
#          if gz==1:
#             glColor3f(0.0,0.0,1.0)
#             glVertex3f(0.0,0.0,0.0)
#             i=2
#             glVertex3f(tensor[i][1]*selfa.scale,tensor[i][2]*selfa.scale,tensor[i][3]*selfa.scale)
#             glVertex3f(0.0,0.0,0.0)
#             glVertex3f(-1.*tensor[i][1]*selfa.scale,-1.*tensor[i][2]*selfa.scale,-1.*tensor[i][3]*selfa.scale)
#          glEnd()
#          glPopMatrix()
        if easy=='y':
         if gx+gy+gz>0:
           pos=pos+0.25
           pos2=pos
           glEnable( GL_LIGHTING )
           glLineWidth(2.0)
#           glCallList( tkList )
           glBegin(GL_LINES)
           glNormal3f(0., 0., +1.)
           if selfa.show_glegend==0:
             if gx==1:
               glColor3f(1.0,0.0,0.0)
               glVertex3f(3.0,pos2-0.25,0.0)
               glVertex3f(3.1,pos2-0.25,0.0)
               pos2=pos2-0.25
             if gy==1:
               glColor3f(0.0,1.0,0.0)
               glVertex3f(3.0,pos2-0.25,0.0)
               glVertex3f(3.1,pos2-0.25,0.0)
               pos2=pos2-0.25
             if gz==1:
               glColor3f(0.0,0.0,1.0)
               glVertex3f(3.0,pos2-0.25,0.0)
               glVertex3f(3.1,pos2-0.25,0.0)
               pos2=pos2-0.25
           glEnd()
           glCallList( tkList )
           #glDisable( GL_LIGHTING )
           glColor3f( 0, 0, 0 )
           if selfa.show_glegend==0:
             if gx==1:
               glRasterPos3f(3.25,pos-0.25,0.0)
               pos=pos-0.25
               for c in 'gX':
                     glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
             if gy==1:
               glRasterPos3f(3.25,pos-0.25,0.0)
               pos=pos-0.25
               for c in 'gY':
                     glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
             if gz==1:
               glRasterPos3f(3.25,pos-0.25,0.0)
               pos=pos-0.25
               for c in 'gZ':
                     glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
        glColor3f(0.0 ,0., 0.99)
        glDisable( GL_LIGHTING )
#        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
#        glEnable(GL_BLEND)
        glPushMatrix()
        glTranslatef(selfa.translatex,selfa.translatey,selfa.translatez)
        glRotatef(selfa.rotate_y,0.,1.,0.)
        glRotatef(selfa.rotate_x,1.,0.,0.)
        glRotatef(selfa.rotate_z,0.,0.,1.)
        glBegin(GL_QUADS)
        for i in range(0,len(tri)):
#          glColor4f(color[i][0] ,color[i][1], color[i][2], 0.6)
#          glVertex3f(tri[i][0][0]*selfa.scale,tri[i][0][1]*selfa.scale,tri[i][0][2]*selfa.scale)
#          glColor4f(color[i][3] ,color[i][4], color[i][5], 0.6)
#          glVertex3f(tri[i][1][0]*selfa.scale,tri[i][1][1]*selfa.scale,tri[i][1][2]*selfa.scale)
#          glColor4f(color[i][6] ,color[i][7], color[i][8], 0.6)
#          glVertex3f(tri[i][2][0]*selfa.scale,tri[i][2][1]*selfa.scale,tri[i][2][2]*selfa.scale)
#          glColor4f(color[i][9] ,color[i][10], color[i][11], 0.6)
#          glVertex3f(tri[i][3][0]*selfa.scale,tri[i][3][1]*selfa.scale,tri[i][3][2]*selfa.scale)


          glColor3f(color[i][0] ,color[i][1], color[i][2])
          glVertex3f(tri[i][0][0]*selfa.scale,tri[i][0][1]*selfa.scale,tri[i][0][2]*selfa.scale)
          glColor3f(color[i][3] ,color[i][4], color[i][5])
          glVertex3f(tri[i][1][0]*selfa.scale,tri[i][1][1]*selfa.scale,tri[i][1][2]*selfa.scale)
          glColor3f(color[i][6] ,color[i][7], color[i][8])
          glVertex3f(tri[i][2][0]*selfa.scale,tri[i][2][1]*selfa.scale,tri[i][2][2]*selfa.scale)
          glColor3f(color[i][9] ,color[i][10], color[i][11])
          glVertex3f(tri[i][3][0]*selfa.scale,tri[i][3][1]*selfa.scale,tri[i][3][2]*selfa.scale)
        glEnd()
        glPopMatrix()

#        glRasterPos3f( 0.1, -2.1, 0 )
#        glPushMatrix()
#        glRotatef(selfa.rotate_y,0.,1.,0.)
#        glRotatef(selfa.rotate_x,1.,0.,0.)
#        glRotatef(selfa.rotate_z,0.,0.,1.)
        glBegin(GL_QUADS)
        pas=(smax-smin)/300.0
        for i in range(0,300):
          p=smin+float(i)*pas
          f=(p-smin)/(smax-smin)
          a=(1-f)/0.25
          X=int(a)
          Y=int(255*(a-X))
          if X==0:
                  r=255
                  g=Y
                  b=0
          elif X==1:
                  r=255-Y
                  g=255
                  b=0
          elif X==2:
                  r=0
                  g=255
                  b=Y
          elif X==3:
                  r=0
                  g=255-Y
                  b=255
          else:
                  r=0
                  g=0
                  b=255
          glColor3f(r/255.,g/255.,b/255.)
#          glVertex3f(3.0,0.0,0.0)
#          glVertex3f(3.2,0.0,0.0)
          glVertex3f(3.1,1.4+float((i-1)/150),0.0)
          glVertex3f(3.4,1.4+float((i-1)/150),0.0)
          glVertex3f(3.4,1.4+float(i/150),0.0)
          glVertex3f(3.1,1.4+float(i/150),0.0)
        glEnd()
#        glPopMatrix()


#        test=max(tri)
#        print(test)

#        glPushMatrix()
#        glRotatef(selfa.rotate_y,0.,1.,0.)
#        glRotatef(selfa.rotate_x,1.,0.,0.)
#        glRotatef(selfa.rotate_z,0.,0.,1.)        
#        glLineWidth(2.0)
#        glBegin(GL_LINES)
#        glColor3f(0.,0.,0.)
#        glVertex3f(-3.5,-3.0,-3.0)
#        glVertex3f(-3.0,-3.0,-3.0)
##        glVertex3f(-3.0,-3.0*np.cos(selfa.rotate_x*2*np.pi/360.)+3.0*np.sin(selfa.rotate_x*2*np.pi/360.),-3.0*np.sin(selfa.rotate_x*2*np.pi/360.)-3.0*np.cos(selfa.rotate_x*2*np.pi/360.))
#        glVertex3f(-3.5,-3.0,-3.0)
#        glVertex3f(-3.5,-2.5,-3.0)
##        glVertex3f(-3.5*np.cos(selfa.rotate_y*2*np.pi/360.)-3.0*np.sin(selfa.rotate_y*2*np.pi/360.),-2.5,3.5*np.sin(selfa.rotate_y*2*np.pi/360.)-3.0*np.cos(selfa.rotate_y*2*np.pi/360.))
#        glVertex3f(-3.5,-3.0,-3.0)
#        glVertex3f(-3.5*np.cos(selfa.rotate_z*2*np.pi/360.)+3.0*np.sin(selfa.rotate_z*2*np.pi/360.),-3.5*np.sin(selfa.rotate_z*2*np.pi/360.)-3.0*np.cos(selfa.rotate_z*2*np.pi/360.),-2.5)
##        glVertex3f(-3.5,-3.0,-2.5)
#        glEnd()
#        glPopMatrix()
        if cartesian=='y' and selfa.show_cartesian==0:
          x=[[-3.5,-3.5,-3.5],[-3.0,-3.5,-3.5],[-3.5,-3.0,-3.5],[-3.5,-3.5,-3.0],[-2.9,-3.5,-3.5],[-3.5,-2.9,-3.5],[-3.5,-3.5,-2.9]]
            #rotation selons z
          for i in range(0,7):
            x[i][0]=x[i][0]*np.cos(selfa.rotate_z*np.pi/180.0)-x[i][1]*np.sin(selfa.rotate_z*np.pi/180.0)
            x[i][1]=x[i][0]*np.sin(selfa.rotate_z*np.pi/180.0)+x[i][1]*np.cos(selfa.rotate_z*np.pi/180.0)
            #rotation selons x
          for i in range(0,7):
            x[i][1]=x[i][1]*np.cos(selfa.rotate_x*np.pi/180.0)-x[i][2]*np.sin(selfa.rotate_x*np.pi/180.0)
            x[i][2]=x[i][1]*np.sin(selfa.rotate_x*np.pi/180.0)+x[i][2]*np.cos(selfa.rotate_x*np.pi/180.0)
            #rotation selons x
          for i in range(0,7):
            x[i][2]=x[i][2]*np.cos(selfa.rotate_y*np.pi/180.0)-x[i][0]*np.sin(selfa.rotate_y*np.pi/180.0)
            x[i][0]=x[i][2]*np.sin(selfa.rotate_y*np.pi/180.0)+x[i][0]*np.cos(selfa.rotate_y*np.pi/180.0)
          a=-3.5-x[0][0]
          b=-3.5-x[0][1]
          d=-3.5-x[0][2]
          glLineWidth(1.0)
          glBegin(GL_LINES)
          glColor3f(0.9,0.,0.)
          for i in range(0,4):
            glVertex3f(x[0][0]+a,x[0][1]+b,x[0][2]+d)
            glVertex3f(x[1][0]+a,x[1][1]+b,x[1][2]+d)
            glVertex3f(x[0][0]+a,x[0][1]+b,x[0][2]+d)
            glVertex3f(x[2][0]+a,x[2][1]+b,x[2][2]+d)
            glVertex3f(x[0][0]+a,x[0][1]+b,x[0][2]+d)
            glVertex3f(x[3][0]+a,x[3][1]+b,x[3][2]+d)
          glEnd()
        glCallList( tkList )
        glDisable( GL_LIGHTING )
        glColor3f( 0, 0, 0 )
        if cartesian=='y' and selfa.show_cartesian==0:
          glRasterPos3f(x[4][0]+a,x[4][1]+b,x[4][2]+d)
          for c in 'x': 
                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f(x[5][0]+a,x[5][1]+b,x[5][2]+d)
          for c in 'y':
                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f(x[6][0]+a,x[6][1]+b,x[6][2]+d)
          for c in 'z':
                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
        for i in range(0,len(str(smax))):
         if str(smax)[i]=='.':
           ssmax=str(smax)[0:i+3]
#        glRasterPos3f( 0.1, -2.1, 0 )
        for i in range(0,len(str(smin))):
         if str(smin)[i]=='.':
           ssmin=str(smin)[0:i+3]
        smoy=(smax+smin)/2.
        smoy2=(smin+smoy)/2.
        smoy3=(smax+smoy)/2.
        for i in range(0,len(str(selfa.scale))):
         if str(selfa.scale)[i]=='.':
           szoom=str(selfa.scale)[0:i+3]
        for i in range(0,len(str(selfa.rotate_x))):
         if str(selfa.rotate_x)[i]=='.':
           srotx=str(selfa.rotate_x)[0:i+3]
        for i in range(0,len(str(selfa.rotate_y))):
         if str(selfa.rotate_y)[i]=='.':
           sroty=str(selfa.rotate_y)[0:i+3]
        for i in range(0,len(str(selfa.rotate_z))):
         if str(selfa.rotate_z)[i]=='.':
           srotz=str(selfa.rotate_z)[0:i+3]
        for i in range(0,len(str(selfa.scale2))):
         if str(selfa.scale2)[i]=='.':
           szoom2=str(selfa.scale2)[0:i+3]
        for i in range(0,len(str(smoy))):
         if str(smoy)[i]=='.':
           ssmoy=str(smoy)[0:i+3]
        for i in range(0,len(str(smoy2))):
         if str(smoy2)[i]=='.':
           ssmoy2=str(smoy2)[0:i+3]
        for i in range(0,len(str(smoy3))):
         if str(smoy3)[i]=='.':
           ssmoy3=str(smoy3)[0:i+3]
        glRasterPos3f( 2.98, 1.45+300./150., 0 )
        for c in ssmax:
                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
        glRasterPos3f( 2.98, 1.17, 0 )
        for c in ssmin:
                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        glRasterPos3f( 3.05, 1.07+300./150., 0 )
#        for c in ssmax:
#        	glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        glRasterPos3f( 3.05, 1.07, 0 )
#        for c in ssmin:
#                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        glRasterPos3f( 3.05, 1.07+150./150., 0 )
#        for c in ssmoy:
#                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        glRasterPos3f( 3.05, 1.07+75./150., 0 )
#        for c in ssmoy2:
#                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        glRasterPos3f( 3.05, 1.07+225./150., 0 )
#        for c in ssmoy3:
#                glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
        if selfa.show_zoomvalues==0:
          glRasterPos3f( 2.0, -2.4, 0 )
          for c in 'rotat x':
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 2.0, -2.6, 0 )
          for c in 'rotat x':
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 2.0, -2.8, 0 )
          for c in 'rotat z':
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          selfa.rotate_x
          glRasterPos3f( 2.0, -3.0, 0 )
          for c in 'zoom pot':
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 2.0, -3.2, 0 )
          for c in 'zoom mol':
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 3.05, -3.0, 0 )
          for c in szoom:
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 3.05, -3.2, 0 )
          for c in szoom2:
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 3.05, -2.4, 0 )
          for c in srotx:
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 3.05, -2.6, 0 )
          for c in sroty:
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          glRasterPos3f( 3.05, -2.8, 0 )
          for c in srotz:
                  glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#        pos=0.8
#        if atome=='y':
#           glEnable( GL_LIGHTING )
#           for i in range(0,len(atom_legend)):
#                glPushMatrix()
#                glTranslatef(3.15,0.85-(i*0.25), 0)
#                glColor3f(atom_legend[i][2][0],atom_legend[i][2][1],atom_legend[i][2][2])
#                glutSolidSphere(atom_legend[i][1]/3., 200,16)
#                glPopMatrix()
#                glRasterPos3f( 3.25, 0.8-(i*0.25), 0 )
#                pos=pos-0.25
#                for c in str.upper(atom_legend[i][0]):
#                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
          # glEnable( GL_LIGHTING )
#        if easy=='y':
#           pos=pos+0.25
#           glEnable( GL_LIGHTING )
#           glLineWidth(4.0)
#           glBegin(GL_LINES)
#           glNormal3f(0., 0., +1.)
#           glColor3f(1.0,0.0,0.0)
#           glVertex3f(3.0,pos-0.25,0.0)
#           glVertex3f(3.1,pos-0.25,0.0)
#           glColor3f(0.0,1.0,0.0)
#           glVertex3f(3.0,pos-0.5,0.0)
#           glVertex3f(3.1,pos-0.5,0.0)
#           glColor3f(0.0,0.0,1.0)
#           glVertex3f(3.0,pos-0.75,0.0)
#           glVertex3f(3.1,pos-0.75,0.0)
#           glEnd()
#           glCallList( tkList )
#           glDisable( GL_LIGHTING )
#           glColor3f( 0, 0, 0 )
#           glRasterPos3f(3.25,pos-0.25,0.0)
#           for c in 'gX':
#                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#           glRasterPos3f(3.25,pos-0.5,0.0)
#           for c in 'gY':
#                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
#           glRasterPos3f(3.25,pos-0.75,0.0)
#           for c in 'gZ':
#                   glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )

        maxi=0.0
#        print('atome=',atome)
        if atome=='y' or atome=='s' or atome=='ynh':
          glEnable(GL_LIGHTING)
          for i in range(0,len(extraction)):
            glPushMatrix()
            glTranslatef(selfa.translatex,selfa.translatey,selfa.translatez)
            glRotatef(selfa.rotate_y,0.,1.,0.)
            glRotatef(selfa.rotate_x,1.,0.,0.)
            glRotatef(selfa.rotate_z,0.,0.,1.)
            glColor3f(extraction[i][2][0],extraction[i][2][1],extraction[i][2][2])
            glTranslatef(extraction[i][0][0]*selfa.scale2,extraction[i][0][1]*selfa.scale2,extraction[i][0][2]*selfa.scale2)
            glutSolidSphere(extraction[i][1]*selfa.scale2, 200, 16)
#            quadratic = gluNewQuadric()
#            gluCylinder(quadratic, 3.0, 6.0, 5.0, 10, 10)
#            gluDisk(quadratic, INNER_RADIUS, OUTER_RADIUS, SLICES, LOOPS)
#            glutSolidCylinder(0.5,0.5,10,10)
            glPopMatrix()
#        glColor3f(0.0,0.0,0.0)
#        quadric=gluNewQuadric()
#        gluQuadricNormals(quadric, GLU_SMOOTH)
#        gluCylinder(quadric, radius, radius, 12.0, 32, 1)
#        gluQuadricOrientation(quadric,GLU_INSIDE)
          glDisable(GL_LIGHTING)
          glPushMatrix()
          glTranslatef(selfa.translatex,selfa.translatey,selfa.translatez)
          glRotatef(selfa.rotate_y,0.,1.,0.)
          glRotatef(selfa.rotate_x,1.,0.,0.)
          glRotatef(selfa.rotate_z,0.,0.,1.)
          glLineWidth(1.0)
          glColor3f( 0, 0, 0 )
#          glBegin(GL_LINES)
          for i in range(0,len(liaison)):
             glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.0,0.0,0.0,1.0])
             v2=np.zeros(3)
             v1=np.zeros(3)
             for j in range(0,3):
              v2[j]=extraction[liaison[i][0]][0][j]*selfa.scale2
              v1[j]=extraction[liaison[i][1]][0][j]*selfa.scale2
#             v2=[extraction[liaison[i][0]][0][0],extraction[liaison[i][0]][0][1],extraction[liaison[i][0]][0][2]]
#             v1=[extraction[liaison[j][0]][0][0],extraction[liaison[j][0]][0][1],extraction[liaison[j][0]][0][2]]
             v2r = v2 - v1
             z = np.array([0.0, 0.0, 1.0])
             ax = np.cross(z, v2r)
             l = sqrt(np.dot(v2r, v2r))
             angle = 180.0 / np.pi * np.arccos(np.dot(z, v2r) / l)
             glPushMatrix()
             glTranslatef(v1[0], v1[1], v1[2])
             glRotatef(angle, ax[0], ax[1], ax[2])
             test=gluNewQuadric()
             gluCylinder(test,0.05*selfa.scale2,0.05*selfa.scale2,l,100,100)
             #glutSolidCylinder(0.05*selfa.scale2, l, 100, 100)
             glPopMatrix()
#            glVertex3f(extraction[liaison[i][0]][0][0]*selfa.scale2,extraction[liaison[i][0]][0][1]*selfa.scale2,extraction[liaison[i][0]][0][2]*selfa.scale2)
#            glVertex3f(extraction[liaison[i][1]][0][0]*selfa.scale2,extraction[liaison[i][1]][0][1]*selfa.scale2,extraction[liaison[i][1]][0][2]*selfa.scale2)
#          glEnd()
          glPopMatrix()

#        if easy=='y':
#          glPushMatrix()
#          glRotatef(selfa.rotate_y,0.,1.,0.)
#          glRotatef(selfa.rotate_x,1.,0.,0.)
#          glRotatef(selfa.rotate_z,0.,0.,1.)
#          glLineWidth(4.0)
#          glDisable(GL_LIGHTING)
#          glBegin(GL_LINES)
#          for i in range(0,3):
#             glNormal3f(0., 0., +1.)
#             if i==0: glColor3f(0.9,0.0,0.0)
#             elif i==1: glColor3f(0.0,0.9,0.0)
#             else: glColor3f(0.0,0.0,0.9)
#             glVertex3f(0.0,0.0,0.0)
#             glVertex3f(tensor[i][1]*selfa.scale,tensor[i][2]*selfa.scale,tensor[i][3]*selfa.scale)
#             glVertex3f(0.0,0.0,0.0)
#             glVertex3f(-1.*tensor[i][1]*selfa.scale,-1.*tensor[i][2]*selfa.scale,-1.*tensor[i][3]*selfa.scale)
#          glEnd()
#          glPopMatrix()
        glDisable(GL_LIGHTING)
#        glEnable(GL_LIGHTING)
        glMatrixMode(GL_MODELVIEW)
        glFlush()
        glutSwapBuffers()
        #if selfa.image=='y':
        #     glfw.init()
        #     DISPLAY_WIDTH = 900
        #     DISPLAY_HEIGHT = 900
        #     glfw.window_hint(glfw.VISIBLE, False)
        #     window = glfw.create_window(DISPLAY_WIDTH, DISPLAY_HEIGHT, "hidden window", None, None)
        #     glfw.make_context_current(window)
        #     image_buffer = glReadPixels(0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT, OpenGL.GL.GL_RGB, OpenGL.GL.GL_UNSIGNED_BYTE)
        #     image = np.frombuffer(image_buffer, dtype=np.uint8).reshape(DISPLAY_WIDTH, DISPLAY_HEIGHT, 3)
        #     cv2.imwrite("image.png", image)
        return
    # The display function
    def display(selfa):
        

        # Draw half the cube with corners cut
#        selfa.draw_half(False)

        # Draw a mirror image of the above half cube
#        selfa.draw_half(True)
        selfa.draw_half()
    # The reshape function
    def reshape(selfa, w, h):
       test=0
    # The keyboard controls
    def mouse(selfa, button, state, x, y):
       global action, xStart, yStart
       if (button==GLUT_LEFT_BUTTON):
           if (glutGetModifiers() == GLUT_ACTIVE_SHIFT):
               action = "MOVE_EYE_2"
           else:
               action = "MOVE_EYE"
       elif (button==GLUT_MIDDLE_BUTTON):
           action = "TRANS"
       elif (button==GLUT_RIGHT_BUTTON):
           action = "ZOOM"
       xStart = x
       yStart = y

    def motion(selfa, x, y):
        global zoom, xStart, yStart, xRotate, yRotate, zRotate, xTrans, yTrans
        if (action=="MOVE_EYE"):
            selfa.rotate_x += x - xStart
            selfa.rotate_y -= y - yStart
        elif (action=="MOVE_EYE_2"):
            selfa.rotate_z += y - yStart
        elif (action=="TRANS"):
            xTrans += x - xStart
            yTrans += y - yStart
        elif (action=="ZOOM"):
            selfa.scale -= y - yStart
            #print(y - yStart)
            #if  > 150.:
            #    zoom = 150.
            #elif zoom < 1.1:
            #    zoom = 1.1
        else:
            print("unknown action\n", action)
        xStart = x
        yStart = y 
        glutPostRedisplay()

    def special(selfa, key, x, y):
         z=0
         z=glutGetModifiers()
#         print(key,chr(key))
         if key == GLUT_KEY_UP and z==0: selfa.rotate_x = selfa.rotate_x + 2.5
         if key == GLUT_KEY_DOWN and z==0: selfa.rotate_x = selfa.rotate_x - 2.5
         if key == GLUT_KEY_LEFT and z==0: selfa.rotate_z = selfa.rotate_z + 2.5
         if key == GLUT_KEY_RIGHT and z==0: selfa.rotate_z = selfa.rotate_z - 2.5
         
         if key == GLUT_KEY_LEFT and z==1: selfa.rotate_y = selfa.rotate_y + 2.5
         if key == GLUT_KEY_RIGHT and z==1: selfa.rotate_y = selfa.rotate_y - 2.5
         if key == 104 and z==0 : selfa.scale=selfa.scale*1.1
         if key == 105 and z==0 : selfa.scale=selfa.scale*0.9
        # if key == 104 and z==1 : selfa.scale2=selfa.scale2*1.1
        # if key == 105 and z==1 : selfa.scale2=selfa.scale2*0.9
         if key == 112: selfa.scale2=selfa.scale2*1.1
         if key == 109 : selfa.scale2=selfa.scale2*0.9
         if key == 80 and z==1 : selfa.scale3=selfa.scale3*1.1
         if key == 77 and z==1 : selfa.scale3=selfa.scale3*0.9
         if chr(key) == 'r': selfa.scale2=selfa.scale
         #if key == GLUT_KEY_UP and z==1: selfa.translatez=selfa.translatez+0.2
         #if key == GLUT_KEY_DOWN and z==1: selfa.translatez=selfa.translatez-0.2
         #if key == GLUT_KEY_UP and z==4: selfa.translatey=selfa.translatey+0.2
         #if key == GLUT_KEY_DOWN and z==4: selfa.translatey=selfa.translatey-0.2
         #if key == GLUT_KEY_RIGHT and z==4: selfa.translatex=selfa.translatex+0.2
         #if key == GLUT_KEY_LEFT and z==4: selfa.translatex=selfa.translatex-0.2
         if key == 27:
#            exit()
#             glutDestroyWindow("test")
             exit()
             #glutLeaveMainLoop()
             
         elif chr(key) == 'q':
             exit()
         #print(chr(key),key)
         glutPostRedisplay()
         return(key)




    def keyboard(selfa, key, x, y):
         z=0
         z=glutGetModifiers()
#         print(key,chr(key))
#         if key == GLUT_KEY_UP and z==0: selfa.rotate_x = selfa.rotate_x + 10
#         if key == GLUT_KEY_DOWN and z==0: selfa.rotate_x = selfa.rotate_x - 10
#         if key == GLUT_KEY_LEFT and z==0: selfa.rotate_z = selfa.rotate_z + 10
#         if key == GLUT_KEY_RIGHT and z==0: selfa.rotate_z = selfa.rotate_z - 10
#    
#         if key == GLUT_KEY_LEFT and z==1: selfa.rotate_y = selfa.rotate_y + 10
#         if key == GLUT_KEY_RIGHT and z==1: selfa.rotate_y = selfa.rotate_y - 10
#         if key == 104 and z==0 : selfa.scale=selfa.scale*1.1
#         if key == 105 and z==0 : selfa.scale=selfa.scale*0.9
#         if key == 104 and z==1 : selfa.scale2=selfa.scale2*1.1
#         if key == 105 and z==1 : selfa.scale2=selfa.scale2*0.9
#         if chr(key) == 'r': selfa.scale2=selfa.scale
#         if key == GLUT_KEY_UP and z==1: selfa.translatez=selfa.translatez+0.2
#         if key == GLUT_KEY_DOWN and z==1: selfa.translatez=selfa.translatez-0.2
#         if key == GLUT_KEY_UP and z==4: selfa.translatey=selfa.translatey+0.2
#         if key == GLUT_KEY_DOWN and z==4: selfa.translatey=selfa.translatey-0.2
#         if key == GLUT_KEY_RIGHT and z==4: selfa.translatex=selfa.translatex+0.2
#         if key == GLUT_KEY_LEFT and z==4: selfa.translatex=selfa.translatex-0.2
         if ord(key) == 27:
##            exit()
##             glutDestroyWindow("test")
             exit()
#             #glutLeaveMainLoop()
#
         elif ord(key) == 113 or ord(key)==81:
             exit()
         elif ord(key) == 43 and z==1:selfa.scale=selfa.scale*1.1
         elif ord(key) == 45 and z==0:selfa.scale=selfa.scale*0.9
#         elif ord(key) == 43 and z==1:selfa.scale2=selfa.scale2*1.1
#         elif ord(key) == 45 and z==1:selfa.scale2=selfa.scale2*0.9
#         elif ord(key) == 95 : selfa.scale2=selfa.scale2*0.9
         elif ord(key) == 112:selfa.scale2=selfa.scale2*1.1
         elif ord(key) == 109:selfa.scale2=selfa.scale2*0.9
         if ord(key) == 80 and z==1 : selfa.scale3=selfa.scale3*1.1
         if ord(key) == 77 and z==1 : selfa.scale3=selfa.scale3*0.9
         if ord(key)== 116 : selfa.translatey=selfa.translatey+0.5
         if ord(key)== 98 : selfa.translatey=selfa.translatey-0.5
         if ord(key)== 104 : selfa.translatex=selfa.translatex+0.5
         if ord(key)== 102 : selfa.translatex=selfa.translatex-0.5
         if ord(key)== 115 :
             #print(plot_type)
             #print(glutGetWindow())
             #if glutGetWindow()==4:
             #   print("quadrupole")
             #glutSetWindow(1)
             width, height = 800, 800
            # glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
            # glutInitWindowSize(width, height)
            # glutCreateWindow(b"OpenGL Offscreen")
            # glutHideWindow()
             #print("ICI",selfa.filename)
             wind_index=1
             if plot_type=="a":
                 wind_index=4
             for i in range(0,wind_index):
                 glutSetWindow(i+1)
                 #width, height = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
                 glPixelStorei(GL_PACK_ALIGNMENT, 1)
                 data = glReadPixels(0, 0, width, height, GL_RGBA, GL_UNSIGNED_BYTE)
                 image = Image.frombytes("RGBA", (width, height), data)
                 image = ImageOps.flip(image) # in my case image is flipped top-bottom for some reason
                 image.save(selfa.filename+window_name[i]+'.tiff', 'TIFF', compression="None")
             #image.save('glut.jpg','JPEG',quality=95)
             #selfa.image="y"
             #width, height = 300, 300
             #global render
             #render = SceneRenderer(width, height)
             #render.Render()

             #glPixelStorei(GL_PACK_ALIGNMENT, 1)
             #data = glReadPixels(0, 0, width, height, GL_RGBA, GL_UNSIGNED_BYTE)
             #image = Image.frombytes("RGBA", (width, height), data)
             #image = ImageOps.flip(image) # in my case image is flipped top-bottom for some reason
             #image.save('glut1.png', 'PNG')
#             glfw.init()
#             DISPLAY_WIDTH = 900
#             DISPLAY_HEIGHT = 900
#             glfw.window_hint(glfw.VISIBLE, False)
#             window = glfw.create_window(DISPLAY_WIDTH, DISPLAY_HEIGHT, "hidden window", None, None)
#             glfw.make_context_current(window)
#             image_buffer = glReadPixels(0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT, OpenGL.GL.GL_RGB, OpenGL.GL.GL_UNSIGNED_BYTE)
#             image = np.frombuffer(image_buffer, dtype=np.uint8).reshape(DISPLAY_WIDTH, DISPLAY_HEIGHT, 3)
#             cv2.imwrite("image.png", image)
#         if ord(key)== 107 : selfa.translatez=selfa.translatez+0.5
#         if ord(key)== 106 : selfa.translatez=selfa.translatez-0.5
         elif ord(key) == 114: 
           selfa.rotate_x=0.0
           selfa.rotate_y=0.0
           selfa.rotate_z=0.0
           selfa.scale2=0.4
           selfa.scale=0.4
         print(key,ord(key))
         if ord(key)==108:
           if selfa.show_atlegend==0:selfa.show_atlegend=1
           else: selfa.show_atlegend=0
         if ord(key)==122:
           if selfa.show_zoomvalues==0:selfa.show_zoomvalues=1
           else:selfa.show_zoomvalues=0           
         if ord(key)==99:
           if selfa.show_cartesian==0:selfa.show_cartesian=1
           else: selfa.show_cartesian=0
         if ord(key)==103:
           if selfa.show_glegend==0:selfa.show_glegend=1
           else: selfa.show_glegend=0
         glutPostRedisplay()
         return(key)
# The main function
def main_plot_struct(tri,color,tri2,color2,tri3,color3,tri4,color4,smin,smax,smin2,smax2,smin3,smax3,smin4,smax4,plot_type,cartesian,extraction,liaison,atome,atom_legend,tensor,easy,gx,gy,gz,filename):
    
    # Initialize OpenGL
#    glutInit(sys.argv)
#
#    # Set display mode
#    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
#
#    # Set size and position of window size
#    glutInitWindowSize(400, 400)
#    glutInitWindowPosition(100, 100)
#
#    # Create window with given title
#
#
#    # Instantiate the cube
#    
    #print('enter')
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE + GLUT_RGB + GLUT_DEPTH)
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(350, 200)

    glutCreateWindow(name)

    glClearColor(0.99, 0.99, 0.99, 1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    lightZeroPosition = [10., 4., 10., 1.]
    lightZeroColor = [0.8, 1.0, 0.8, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    cube = Cube(tri,color,tri2,color2,tri3,color3,smin,smax,smin2,smax2,smin3,smax3,smin4,smax4,plot_type,cartesian,extraction,liaison,atome,atom_legend,tensor,easy,gx,gy,gz,fichier)
    glutDisplayFunc(cube.draw_half)
    glutReshapeFunc(cube.reshape)
    glutKeyboardFunc(cube.keyboard)
    glutSpecialFunc(cube.special)
    glutMouseFunc(cube.mouse)
    glutMotionFunc(cube.motion)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40., 1., 1., 40.)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, 0, 10,
              0, 0, 0,
              0, 1, 0)
    if plot_type=='a':
      glutInitWindowSize(800, 800)
      glutCreateWindow(name2)
      glClearColor(0.99, 0.99, 0.99, 1.)
      glShadeModel(GL_SMOOTH)
      glEnable(GL_CULL_FACE)
      glEnable(GL_COLOR_MATERIAL)
      glEnable(GL_DEPTH_TEST)
      glEnable(GL_LIGHTING)
      lightZeroPosition = [10., 4., 10., 1.]
      lightZeroColor = [0.8, 1.0, 0.8, 1.0]
      glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
      glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
      glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
      glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
      glEnable(GL_LIGHT0)
      glutInitWindowPosition(650, 200)
      glutDisplayFunc(cube.draw_half2)
      glutKeyboardFunc(cube.keyboard)
      glutSpecialFunc(cube.special)
      glutReshapeFunc(cube.reshape)
      glutMouseFunc(cube.mouse)
      glutMotionFunc(cube.motion)
      glMatrixMode(GL_PROJECTION)
      gluPerspective(40., 1., 1., 40.)
      glMatrixMode(GL_MODELVIEW)
      gluLookAt(0, 0, 10,
                0, 0, 0,
                0, 1, 0)
      glutCreateWindow(name3)
      glClearColor(0.99, 0.99, 0.99, 1.)
      glShadeModel(GL_SMOOTH)
      glEnable(GL_CULL_FACE)
      glEnable(GL_COLOR_MATERIAL)
      glEnable(GL_DEPTH_TEST)
      glEnable(GL_LIGHTING)
      lightZeroPosition = [10., 4., 10., 1.]
      lightZeroColor = [0.8, 1.0, 0.8, 1.0]
      glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
      glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
      glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
      glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
      glEnable(GL_LIGHT0)
      glutInitWindowPosition(650, 200)
      glutDisplayFunc(cube.draw_half3)
      glutKeyboardFunc(cube.keyboard)
      glutSpecialFunc(cube.special)
      glutReshapeFunc(cube.reshape)
      glutMouseFunc(cube.mouse)
      glutMotionFunc(cube.motion)
      glMatrixMode(GL_PROJECTION)
      gluPerspective(40., 1., 1., 40.)
      glMatrixMode(GL_MODELVIEW)
      gluLookAt(0, 0, 10,
                0, 0, 0,
                0, 1, 0)
      glutCreateWindow(name4)
      glClearColor(0.99, 0.99, 0.99, 1.)
      glShadeModel(GL_SMOOTH)
      glEnable(GL_CULL_FACE)
      glEnable(GL_COLOR_MATERIAL)
      glEnable(GL_DEPTH_TEST)
      glEnable(GL_LIGHTING)
      lightZeroPosition = [10., 4., 10., 1.]
      lightZeroColor = [0.8, 1.0, 0.8, 1.0]
      glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
      glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
      glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
      glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
      glEnable(GL_LIGHT0)
      glutInitWindowPosition(650, 200)
      glutDisplayFunc(cube.draw_half4)
      glutKeyboardFunc(cube.keyboard)
      glutSpecialFunc(cube.special)
#      glutSpecialFunc(cube.special)
      glutReshapeFunc(cube.reshape)
      glutMouseFunc(cube.mouse)
      glutMotionFunc(cube.motion)
      glMatrixMode(GL_PROJECTION)
      gluPerspective(40., 1., 1., 40.)
      glMatrixMode(GL_MODELVIEW)
      gluLookAt(0, 0, 10,
                0, 0, 0,
                0, 1, 0)
    glutMainLoop() 
    
#    glutInit(sys.argv)
#    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
#    glutInitWindowSize(800, 800)
#    glutInitWindowPosition(350, 200)
#
#    glutCreateWindow(name)
#
#    glClearColor(0.99, 0.99, 0.99, 1.)
#    glShadeModel(GL_SMOOTH)
#    glEnable(GL_CULL_FACE)
#    glEnable(GL_DEPTH_TEST)
#    glEnable(GL_LIGHTING)
##    lightZeroPosition = [10., 4., 10., 1.]
##    lightZeroColor = [0.8, 1.0, 0.8, 1.0]
##    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
##    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
##    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
##    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
#    glEnable(GL_LIGHTING)
##    glEnable(GL_COLOR_MATERIAL)
##    gluPerspective(60.0, 1.0, 0.1, 100.0)
#    glEnable(GL_LIGHT0)
#    cube = Cube(coord,dist,attype,numat,VDW,RGB,tri,trim,showmol)
#    glutDisplayFunc(cube.draw_half)
#    #glutReshapeFunc(cube.reshape)
#    check=glutSpecialFunc(cube.special)
#    glMatrixMode(GL_PROJECTION)
#    gluPerspective(60.0, 1.0, 0.1, 100.0)
##    gluPerspective(40., 1., 1., 40.)
#    glMatrixMode(GL_MODELVIEW)
#    gluLookAt(0., 0., 5., 0., 0., 0., 0., 1., 0.)
##    gluLookAt(0, 0, 10,
##              0, 0, 0,
##              0, 1, 0)
#    glPushMatrix()
#    glutMainLoop()
    return
#
#    cube.init()
#
#    # The callback for display function
#    glutDisplayFunc(cube.display)
#
#    # The callback for reshape function
#    glutReshapeFunc(cube.reshape)
#
#    # The callback function for keyboard controls
#    check=glutSpecialFunc(cube.special)
#    
#    # Start the main loop
#    glutMainLoop()
    return


def cal_color(p,smin,smax):                
                f=(p-smin)/(smax-smin)
                a=(1-f)/0.25
                X=int(a)
                Y=int(255*(a-X))
                if X==0:
                        r=255
                        g=Y
                        b=0
                elif X==1:
                        r=255-Y
                        g=255
                        b=0
                elif X==2:
                        r=0
                        g=255
                        b=Y
                elif X==3:
                        r=0
                        g=255-Y
                        b=255
                else:
                        r=0
                        g=0
                        b=255
                return(r/255.,g/255.,b/255.)
def sphere_to_cart(r,theta,phi):
	return([r*np.sin(phi)*np.cos(theta),r*np.sin(phi)*np.sin(theta),r*np.cos(phi)])
def check_coord(f,i):
	coord=[]
	for j in range(3,len(str.split(f[i]))-2):
		#print(len(str.split(f[i])[j]),str.split(f[i])[j])
		if len(str.split(f[i])[j])<15:
			coord.append(float(str.split(f[i])[j]))
		else:
			num=[]
			for k in range(3,len(str.split(f[i])[j])):
				if str.split(f[i])[j][k]=='-':
					num.append(k)
					#break
			#print(str.split(f[i])[j][:num-1],str.split(f[i])[j][num:])
			coord.append(float(str.split(f[i])[j][:num[0]-1]))
			for k in range(1,len(num)):
				coord.append(float(str.split(f[i])[j][num[k-1]:num[k]-1]))
			coord.append(float(str.split(f[i])[j][num[len(num)-1]:]))
			#print('coord',coord)
	return(coord)
def check_dipole(f,i):
	dipole=[]
	for j in range(0,len(str.split(f[i]))):
		if len(str.split(f[i])[j])<15:
			dipole.append(float(str.split(f[i])[j]))
		else:
			num=[]
			for k in range(3,len(str.split(f[i])[j])):
				if str.split(f[i])[j][k]=='-':
					num.append(k)
					#break
			dipole.append(float(str.split(f[i])[j][:num[0]-1]))
			for k in range(1,len(num)):
				dipole.append(float(str.split(f[i])[j][num[k-1]:num[k]-1]))
			dipole.append(float(str.split(f[i])[j][num[len(num)-1]:]))
			#print('dipole',dipole)
	return(dipole)
def check_qad(f,i):
	quad=[]
	for j in range(0,len(str.split(f[i]))):
		if len(str.split(f[i])[j])<15:
			quad.append(float(str.split(f[i])[j]))
		else:
			num=[]
			for k in range(3,len(str.split(f[i])[j])):
				if str.split(f[i])[j][k]=='-':
					num.append(k)
					#break
			quad.append(float(str.split(f[i])[j][:num[0]-1]))
			for k in range(1,len(num)):
				quad.append(float(str.split(f[i])[j][num[k-1]:num[k]-1]))
			quad.append(float(str.split(f[i])[j][num[len(num)-1]:]))
			#print('quad',quad)
	return(quad)
def extract_atomic_domain(fichier):
        atom_lourd=['LA','CE','PR','ND','PM','SM','EU','GD','TB','DY','HO','ER','TM','YB','LU']
        f=os.popen("grep -A18 'ATOMIC DOMAIN' "+fichier).readlines()
        atomic=[]
        lourd=''
        for i in range(0,len(f)):
                if len(str.split(f[i]))>0:
                        if str.split(f[i])[0]=='ATOMIC':
                                at=str.split(f[i])[2]
                                num=len(at)
                                test=0
                                for j in range(0,len(at)):
                                        if at[j].isdigit():
                                                num=j
                                                test=1
                                                break
                                if test==1:
                                        at2=at[:num]
                                else: at2=at
                                #print(at2,at)
                                test=0
                                for j in range(0,len(atom_lourd)):
                                        if at2==atom_lourd[j]:
                                                test=test+1
                                                center=[float(str.split(f[i+2])[3]),float(str.split(f[i+2])[4]),float(str.split(f[i+2])[5])]
                                                lourd=at2
    #                                            print("test lourd",lourd,"atome=",at2)
                                if test==0:
                                        coord=check_coord(f,i+2)
                                        dipole=check_dipole(f,i+11)
                                        quad=check_qad(f,i+16)
                                        atomic.append([at2,coord,float(str.split(f[i+4])[3]),dipole,quad])
#                                        atomic.append([at2,[float(str.split(f[i+2])[3]),float(str.split(f[i+2])[4]),float(str.split(f[i+2])[5])],float(str.split(f[i+4])[3]),[float(str.split(f[i+11])[0]),float(str.split(f[i+11])[1]),float(str.split(f[i+11])[2])],[float(str.split(f[i+16])[0]),float(str.split(f[i+16])[1]),float(str.split(f[i+16])[2]),float(str.split(f[i+16])[3]),float(str.split(f[i+16])[4]),float(str.split(f[i+16])[5])]])
        if center[0]!=0.0 or center[1]!=0.0 or center[2]!=0:
                for j in range(0,len(atomic)):
                        for k in range(0,3):
                                atomic[j][1][k]=atomic[j][1][k]-center[k]
        return([atomic,lourd])

def sphere_to_cart(r,theta,phi):
        return([r*np.sin(phi)*np.cos(theta),r*np.sin(phi)*np.sin(theta),r*np.cos(phi)])

def computepot(donnee,nstep,radius,n):
        theta=np.zeros((nstep,nstep))
        phi=np.zeros((nstep,nstep))
        resultat=np.zeros((nstep,nstep,7))
        totmin=10**6
        totmax=-1*10**6
        for i in range(0,nstep):
                for j in range(0,nstep):
                        theta[i][j]=i*(2*np.pi/n)
                        phi[i][j]=j*(np.pi/n)
                        coord=sphere_to_cart(radius,theta[i][j],phi[i][j])
                        mono=0.
                        dipo=0.
                        quad=0.
                        tot=0.
                        for k in range(0,len(donnee)):
                                X=np.zeros(3)
                                D=np.zeros(3)
#                                Q=[[donnee[i][4][0],donnee[i][4][1],donnee[i][4][2]],[donnee[i][4][1],donnee[i][4][3],donnee[i][4][4]],[donnee[i][4][2],donnee[i][4][4],donnee[i][4][5]]]
                                Q=np.zeros((3,3))
                                Q[0][0]=donnee[k][4][0]
                                Q[0][1]=donnee[k][4][1]
                                Q[1][0]=Q[0][1]
                                Q[0][2]=donnee[k][4][2]
                                Q[2][0]=Q[0][2]
                                Q[1][1]=donnee[k][4][3]
                                Q[1][2]=donnee[k][4][4]
                                Q[2][1]=Q[1][2]
                                Q[2][2]=donnee[k][4][5]
                                dist=sqrt((donnee[k][1][0]-coord[0])**2+(donnee[k][1][1]-coord[1])**2+(donnee[k][1][2]-coord[2])**2)
                                for l in range(0,3):
                                        X[l]=(donnee[k][1][l]-coord[l])/dist
                                        D[l]=donnee[k][3][l]
                                mono=mono+(donnee[k][2]/dist)
                                dipo=dipo+(np.dot(D,X)/dist**2)
                                quad=quad+(np.dot(X,np.matmul(Q,X))/(2*dist**3))
                                #if i==1 and j==1 and k==0: 
                                #  print("TEST",X,donnee[k][2],D,Q,donnee[k][2]/dist,np.dot(D,X)/dist**2,np.dot(X,np.matmul(Q,X))/(2*dist**3))
                                #if i==0 and j==0:
                                  #print(k)
                                  #print(Q)
                        tot=mono+dipo+quad
                        #if i==1 and j==1: print("TEST2",tot,coord,theta[i][j],phi[i][j])
                        if tot<totmin:totmin=tot
                        if tot>totmax:totmax=tot 
                        #if i==0 and j==0: print(radius,nstep,tot,mono,dipo,quad)
                        resultat[i][j][0]=coord[0]
                        resultat[i][j][1]=coord[1]
                        resultat[i][j][2]=coord[2]
                        resultat[i][j][3]=tot
                        resultat[i][j][4]=mono
                        resultat[i][j][5]=dipo
                        resultat[i][j][6]=quad

        #print("MIN MAX",totmin,totmax)
        return(resultat)


#print("Name of the Molcas output")
fichier=str(sys.argv[1])
#print(fichier)
f=os.popen("grep 'ATOMIC DOMAIN' "+fichier+" | wc -l").readlines()
if int(str.split(f[0])[0])<2: 
	#print("You calculation have not used the Loprop section and thus CAMMEL cannot compute the potential")
	exit()
#print("Radius around the Lanthanide atom")
radius=float(sys.argv[2])
#print("Number of values of Theta and Phi around the Lanthanide atom (60 should give a quite good description)")
n1=int(sys.argv[3])
#print("Do you prefer to consider the surface for the potential mapping as a sphere or as the potential (s/p)")
surface_pot=str(sys.argv[4])
#print("do you want to display the easy axis (y/n)")
easy=str(sys.argv[5])
#print("Would you like to see only the full potential (answer p) or also its decomposition in term of charge, dipole and quadrupole contributions (answer a) (a/p)")
plot_type=str(sys.argv[6])
#print("do you want to display the first coordination sphere atoms (y/n)")
atome=str(sys.argv[7])
#print("Would you like to see the cartesian axis?")
cartesian=str(sys.argv[8])
gx=int(str(sys.argv[9]))
gy=int(str(sys.argv[10]))
gz=int(str(sys.argv[11]))
multiplet=int(str(sys.argv[12]))
smin_fix=float(sys.argv[13])
smax_fix=float(sys.argv[14])
smin2_fix=float(sys.argv[15])
smax2_fix=float(sys.argv[16])
smin3_fix=float(sys.argv[17])
smax3_fix=float(sys.argv[18])
smin4_fix=float(sys.argv[19])
smax4_fix=float(sys.argv[20])
n=n1+1
extractio=extract_atomic_domain(fichier)
#print("test resultat extract_atomic_domain",extractio)
extraction=extractio[0]
atome_lourd=extractio[1]
potential=computepot(extraction,n,radius,n1)
#print('potential',potential[0][0])
#f=os.popen('cat potential.dat').readlines()
#n=int(sqrt(len(f)-1))
#g=os.popen('cat monopole.dat').readlines()
#h=os.popen('cat dipole.dat').readlines()
#w=os.popen('cat quadrupole.dat').readlines()
pot=np.zeros((n,n,3))
pot2=np.zeros((n,n))
mono=np.zeros((n,n,3))
potmono=np.zeros((n,n))
dipo=np.zeros((n,n,3))
potdipo=np.zeros((n,n))
quad=np.zeros((n,n,3))
potquad=np.zeros((n,n))
i=0
#print('surface_pot=',surface_pot)
potmin=10**5
potmax=-1*10**5
for j in range(0,n):
	for k in range(0,n):
		theta=j*(2*np.pi/float(n1))
		phi=k*(np.pi/float(n1))
		if surface_pot=='p':
			r=abs(potential[j][k][3])
			r2=abs(potential[j][k][4])
			r3=abs(potential[j][k][5])
			r4=abs(potential[j][k][6])
		else:
			r=radius
			r2=radius
			r3=radius
			r4=radius
		c=sphere_to_cart(r,theta,phi)
		d=sphere_to_cart(r2,theta,phi)
		e=sphere_to_cart(r3,theta,phi)
		f1=sphere_to_cart(r4,theta,phi)
		pot[j][k][0]=c[0]
		pot[j][k][1]=c[1]
		pot[j][k][2]=c[2]
		mono[j][k][0]=d[0]
		mono[j][k][1]=d[1]
		mono[j][k][2]=d[2]
		dipo[j][k][0]=e[0]
		dipo[j][k][1]=e[1]
		dipo[j][k][2]=e[2]
		quad[j][k][0]=f1[0]
		quad[j][k][1]=f1[1]
		quad[j][k][2]=f1[2] 
		pot2[j][k]=potential[j][k][3]
	#	if pot2[j][k]<potmin:
	#		potmin=pot2[j][k]
	#		posmin=[j,k]
	#	if pot2[j][k]>potmax:
	#		potmax=pot2[j][k]
	#		posmax=[j,k]
		potmono[j][k]=potential[j][k][4]
		potdipo[j][k]=potential[j][k][5]
		potquad[j][k]=potential[j][k][6]
		i=i+1

if smin_fix==0.0 and smax_fix==0.0:
	smin=np.min(pot2)
	smax=np.max(pot2)
else:
	smin=smin_fix
	smax=smax_fix
smin2=smin2_fix
smax2=smax2_fix
smin3=smin3_fix
smax3=smax3_fix
smin4=smin4_fix
smax4=smax4_fix
if smin2_fix==0.0 and smax2_fix==0.0:
	smin2=np.min(potmono)
	smax2=np.max(potmono)
if smin3_fix==0.0 and smax3_fix==0.0:
	smin3=np.min(potdipo)
	smax3=np.max(potdipo)
if smin4_fix==0.0 and smax4_fix==0.0:
	smin4=np.min(potquad)
	smax4=np.max(potquad)
locmin=(np.unravel_index(pot2.argmin(), pot2.shape))
locmax=(np.unravel_index(pot2.argmax(), pot2.shape))
tri=[]
tri2=[]
tri3=[]
tri4=[]
xmin=10**6
ymin=10**6
zmin=10**6
xmax=-10**6
ymax=-10**6
zmax=-10**6
#fig = plt.figure()
#ax = Axes3D(fig)
color=[]
color2=[]
color3=[]
color4=[]
for i in range(1,n):
	for j in range(1,n):
#		x=[pot[i][j][0],pot[i-1][j][0],pot[i-1][j-1][0],pot[i][j-1][0]]
#		y=[pot[i][j][1],pot[i-1][j][1],pot[i-1][j-1][1],pot[i][j-1][1]]
#		z=[pot[i][j][2],pot[i-1][j][2],pot[i-1][j-1][2],pot[i][j-1][2]]
#		verts = [list(zip(x, y, z))]
#		#ax.add_collection3d(Poly3DCollection(verts,edgecolors='b',facecolors='r'))
#		if min(x)<xmin:xmin=min(x)
#		if min(y)<ymin:ymin=min(y)
#		if min(z)<zmin:zmin=min(z)
#		if max(x)>xmax:xmax=max(x)
#		if max(y)>ymax:ymax=max(y)
#		if max(z)>zmax:zmax=max(z)
		potmoy=(pot2[i][j]+pot2[i-1][j]+pot2[i-1][j-1]+pot2[i][j-1])/4.0
		potmoy2=(potmono[i][j]+potmono[i-1][j]+potmono[i-1][j-1]+potmono[i][j-1])/4.0
		potmoy4=(potquad[i][j]+potquad[i-1][j]+potquad[i-1][j-1]+potquad[i][j-1])/4.0
		potmoy3=(potdipo[i][j]+potdipo[i-1][j]+potdipo[i-1][j-1]+potdipo[i][j-1])/4.0
		c=cal_color(pot2[i][j],smin,smax)
		d=cal_color(pot2[i-1][j],smin,smax)
		e=cal_color(pot2[i-1][j-1],smin,smax)
		f=cal_color(pot2[i][j-1],smin,smax)
		color.append([c[0],c[1],c[2],d[0],d[1],d[2],e[0],e[1],e[2],f[0],f[1],f[2]])
		c=cal_color(potmono[i][j],smin2,smax2)
		d=cal_color(potmono[i-1][j],smin2,smax2)
		e=cal_color(potmono[i-1][j-1],smin2,smax2)
		f=cal_color(potmono[i][j-1],smin2,smax2)
		color2.append([c[0],c[1],c[2],d[0],d[1],d[2],e[0],e[1],e[2],f[0],f[1],f[2]])
		c=cal_color(potdipo[i][j],smin3,smax3)
		d=cal_color(potdipo[i-1][j],smin3,smax3)
		e=cal_color(potdipo[i-1][j-1],smin3,smax3)
		f=cal_color(potdipo[i][j-1],smin3,smax3)
		color3.append([c[0],c[1],c[2],d[0],d[1],d[2],e[0],e[1],e[2],f[0],f[1],f[2]])
		c=cal_color(potquad[i][j],smin4,smax4)
		d=cal_color(potquad[i-1][j],smin4,smax4)
		e=cal_color(potquad[i-1][j-1],smin4,smax4)
		f=cal_color(potquad[i][j-1],smin4,smax4)
		color4.append([c[0],c[1],c[2],d[0],d[1],d[2],e[0],e[1],e[2],f[0],f[1],f[2]])
#		ax.add_collection3d(Poly3DCollection(verts,edgecolors=(r/255.,g/255.,b/255.),facecolors=(r/255.,g/255.,b/255.)))
		tri.append([[pot[i][j][0],pot[i][j][1],pot[i][j][2]],[pot[i-1][j][0],pot[i-1][j][1],pot[i-1][j][2]],[pot[i-1][j-1][0],pot[i-1][j-1][1],pot[i-1][j-1][2]],[pot[i][j-1][0],pot[i][j-1][1],pot[i][j-1][2]]])
		tri2.append([[mono[i][j][0],mono[i][j][1],mono[i][j][2]],[mono[i-1][j][0],mono[i-1][j][1],mono[i-1][j][2]],[mono[i-1][j-1][0],mono[i-1][j-1][1],mono[i-1][j-1][2]],[mono[i][j-1][0],mono[i][j-1][1],mono[i][j-1][2]]])
		tri3.append([[dipo[i][j][0],dipo[i][j][1],dipo[i][j][2]],[dipo[i-1][j][0],dipo[i-1][j][1],dipo[i-1][j][2]],[dipo[i-1][j-1][0],dipo[i-1][j-1][1],dipo[i-1][j-1][2]],[dipo[i][j-1][0],dipo[i][j-1][1],dipo[i][j-1][2]]])
		tri4.append([[quad[i][j][0],quad[i][j][1],quad[i][j][2]],[quad[i-1][j][0],quad[i-1][j][1],quad[i-1][j][2]],[quad[i-1][j-1][0],quad[i-1][j-1][1],quad[i-1][j-1][2]],[quad[i][j-1][0],quad[i][j-1][1],quad[i][j-1][2]]])
#ax.set_xlim(xmin,xmax)
#ax.set_ylim(ymin,ymax)
#ax.set_zlim(zmin,zmax)
#print(tri[0])
#print(np.min(tri),np.max(tri),np.min(tri2),np.max(tri2))
testa="test"
extraction2=extraction
extraction=[]
center=-1
f=os.popen('cat $CAMMEL/source/atom-list').readlines()
#print('center=',str.lower(atome_lourd))
cov_center=0.0
for i in range(1,len(f)):
	if str.lower(str.split(f[i])[0])==str.lower(atome_lourd):
		cov_center=float(str.split(f[i])[2])*1.89

for i in range(0,len(extraction2)):
	cov=0.0
	vdv=0.0
	for j in range(1,len(f)):
		if str.lower(str.split(f[j])[0])==str.lower(extraction2[i][0]):
			cov=float(str.split(f[j])[2])*1.89
			vdw=float(str.split(f[j])[3])*1.89/8.0
			rgb=[float(str.split(f[j])[4])/255.,float(str.split(f[j])[5])/255.,float(str.split(f[j])[6])/255.]
			break
	if atome=='s':
		dista=sqrt((extraction2[i][1][0]**2+extraction2[i][1][1]**2+extraction2[i][1][2]**2))
		if dista<(cov+cov_center)*1.1:
			extraction.append([extraction2[i][1],vdw,rgb,cov,str.lower(extraction2[i][0])])
	else: extraction.append([extraction2[i][1],vdw,rgb,cov,str.lower(extraction2[i][0])])
#print("test extraction",extraction)
if atome=='ynh':
	extraction3=extraction
	extraction=[]
	for i in range(0,len(extraction3)):
		if extraction3[i][-1]!='h' and extraction3[i][-1]!='H':
			extraction.append(extraction3[i])
liaison=[]
atom_legend=[]
#print(extraction)
atom_legend.append([extraction[0][4],extraction[0][1],extraction[0][2]])
dist=np.zeros((len(extraction),len(extraction)))

for i in range(0,len(extraction)):
	test=0
	dist[i][i]=1000
	for j in range(0,len(atom_legend)):
		if extraction[i][4]==atom_legend[j][0]: test=1
	if test==0:atom_legend.append([extraction[i][4],extraction[i][1],extraction[i][2]])
	for j in range(i+1,len(extraction)):
		dist[i][j]=sqrt((extraction[i][0][0]-extraction[j][0][0])**2+(extraction[i][0][1]-extraction[j][0][1])**2+(extraction[i][0][2]-extraction[j][0][2])**2)
		dist[j][i]=dist[i][j]
		#if dista<(extraction[i][3]+extraction[j][3])*1.05: liaison.append([i,j])
distmin=np.min(dist)
for i in range(0,len(extraction)):
	for j in range(i+1,len(extraction)):
		if dist[i][j]<(extraction[i][3]+extraction[j][3])*1.1: liaison.append([i,j])
#		if dist[i][j]<1.25*distmin: liaison.append([i,j])
f=os.popen("grep 'g TENSOR:' "+fichier+" | wc -l").readlines()
ntens=int(str.split(f[0])[0])
tensor2=np.zeros((ntens,3,4))
f=os.popen("grep -A10 'g TENSOR:' "+fichier).readlines()
tens=0
for i in range(0,len(f)):
	if len(str.split(f[i]))>1:
		if str.split(f[i])[0]=='gX':
			for j in range(0,3):
				tensor2[tens][j][0]=float(str.split(f[i+j])[2])
				for k in range(1,4):
					tensor2[tens][j][k]=float(str.split(f[i+j])[5+k])
			tens=tens+1
tensor=np.zeros((3,4))
for i in range(0,3):
	for j in range(0,4):
		tensor[i][j]=tensor2[multiplet][i][j]
#for i in range(6,9):
#	tensor[i-6][0]=float(str.split(f[i])[2])
#	for j in range(1,4):
#		tensor[i-6][j]=float(str.split(f[i])[5+j])



#if float(smin)>smax:
#	locmax=locmin
longueur=abs(np.max(pot))
if abs(np.min(pot))>longueur:longueur=abs(np.min(pot))
longueur=longueur*2.0
#sssmin=float(smin)
#sssmax=float(smax)
#if sssmin>sssmax: 
#	locmax=locmin
#	sssmax=sssmin
#theta=locmax[0]*(2*np.pi/float(n1))
#phi=locmax[1]*(np.pi/float(n1))
#r=abs(sssmax)
#c=sphere_to_cart(r,theta,phi)
##distmax=sqrt(c[0]**2+c[1]**2+c[2]**2)
#distmax=0.0
#for i in range(0,len(c)):
#	if abs(c[i])>distmax:distmax=abs(c[i])
#
for j in range(0,3):
#	longueur2=longueur/sqrt(tensor[j][1]**2+tensor[j][2]**2+tensor[j][3]**2)
	for i in range(1,4):
		tensor[j][i]=tensor[j][i]*longueur

#print(smin,smax,smin_fix,smax_fix)
print(fichier[:-4])
main_plot_struct(tri,color,tri2,color2,tri3,color3,tri4,color4,smin,smax,smin2,smax2,smin3,smax3,smin4,smax4,plot_type,cartesian,extraction,liaison,atome,atom_legend,tensor,easy,gx,gy,gz,fichier[:-4])
#plt.show()
