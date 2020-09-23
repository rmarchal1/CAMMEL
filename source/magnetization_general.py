from operator import itemgetter
import os
import csv
import numpy as np
import matplotlib.pyplot as plt
from math import atan
from math import degrees
from math import sqrt
#from math import abs

def succpetibility(fichier):
        f=os.popen("grep -i -A1 'Temperature depEndence of the magnetic susceptibility calculated in' "+fichier).readlines()
        npoints=int(str.split(f[1])[0])
        f=os.popen("grep -i -A"+str(npoints+20)+" 'Temperature depEndence of the magnetic susceptibility calculated in' "+fichier).readlines()
        pos=[]
        X=[]
        Y=[]
        for i in range(0,len(f)):
                if len(str.split(f[i]))>0:
                        if str.split(f[i])[0][:3]=="---":
                                pos.append(i)
        ligne=pos[1]+1
        ecriture=open(fichier[:-4]+"_succeptibility.dat",'w')
        for i in range(0,npoints):
#       while len(str.split(f[ligne]))>0:
#               print ligne
                X.append(float(str.split(f[ligne])[1]))
#               print(str.split(f[i])[1])
                Y.append(float(str.split(f[ligne])[7]))
                ecriture.write(str.split(f[ligne])[1]+" "+str.split(f[ligne])[7]+" \n")
                ligne=ligne+1
        #print X
        ecriture.close()
        ax = plt.subplot(111)
        ax.plot(X,Y)
        
        plt.title('Magnetic Succeptibily', fontsize=16)
        plt.xlabel(r'$T (K)$', fontsize=16)
        plt.ylabel(r'$\chi_{M} * T (cm^{3}mol^{-1}K)$', fontsize=16)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_ticks_position('bottom')
#        plt.savefig('succeptibility.pdf', dpi=100)
#        plt.close()
        plt.show()
def magnetization(fichier):
        f=os.popen("grep -A4 'CALCULATION OF THE MOLAR MAGNETIZATION' "+fichier).readlines()
        npoint=0
        temp=0
        if str.split(f[3])[0]=="nH":
                npoints=int(str.split(f[3])[2])
        if str.split(f[3])[0]=="Molar":
                npoints=int(str.split(f[3])[6])         
        #print npoints
        f=os.popen("grep -A"+str(5+npoints)+" 'HIGH-FIELD POWDER MAGNETIZATION' "+fichier).readlines()
        temp=float(str.split(f[4])[3])
        X=[]
        Y=[]
        ecriture=open(fichier[:-4]+"_magnetization.dat",'w')
        for i in range(6,len(f)):
                X.append(float(str.split(f[i])[0]))
                Y.append(float(str.split(f[i])[4]))
                ecriture.write(str.split(f[i])[0]+" "+str.split(f[i])[4]+"\n")
        ax = plt.subplot(111)
        ecriture.close()
        ax.plot(X,Y)
        plt.title('Magnetization at '+'%.2f' %temp+' K', fontsize=16)
        plt.xlabel(r'$H(T)$', fontsize=16)
        plt.ylabel(r'$Magnetization (\mu_{B})$', fontsize=16)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_ticks_position('bottom')
#        plt.savefig('magnetisation.pdf',dpi=100)
#        plt.close()
        plt.show()
def ndoublet_magnetization(fichier):
        f=os.popen("grep 'CALCULATION OF PSEUDOSPIN HAMILTONIAN TENSORS FOR THE MULTIPLET' "+fichier+" | wc -l").readlines()
        ndoublet=int(str.split(f[0])[0])
        return(ndoublet)
def barrier(fichier,ndoublets,ndoub_represente,ndecimal,ndoub_val,rep,xmin,xmax,ymin,ymax):
        
        f=os.popen("grep -A"+str(8+ndoublets)+" 'BARRIER' "+fichier).readlines()
        if len(f)>0:
                mult=np.zeros((ndoublets,2))
                ener=np.zeros((ndoublets,2))
                
                for i in range(9,len(f)):
                        mult[i-9][0]=float(str.split(f[i])[2])
                        mult[i-9][1]=float(str.split(f[i])[4])
                        ener[i-9][0]=float(str.split(f[i])[6])
                        ener[i-9][1]=float(str.split(f[i])[6])
                f=os.popen("grep -A"+str(5+ndoublets*4)+" 'MATRIX ELEMENTS BETWEEN STATES WITH OPPOSITE MAGNETIZATION' "+fichier).readlines()
                proba=np.zeros((ndoublets,ndoublets,2))
                doub=0
                max=0
                for i in range(6,len(f)):
                        if len(str.split(f[i]))>max:max=len(str.split(f[i]))
                for i in range(6,len(f)):
                        if len(str.split(f[i]))>max-1:
                                #print str.split(f[i]),doub
                                if str.split(f[i])[7][-1]=='-':
                                        proba[doub][doub][0]=float(str.split(f[i])[-2])
                                        proba[doub][doub][1]=float(str.split(f[i])[-2])
                                        doub=doub+1
                doub=0
                doub2=0
                for i in range(1,ndoublets):
                        #print "TESTESTEST",i
                        #print "grep -A"+str(3+(ndoublets-i)*8)+" 'MATRIX ELEMENTS BETWEEN STATES ARISING FROM NEIGHBORING MULTIPLETS: I -> I+ "+str(i)+"' "+fichier
                        f=os.popen("grep -A"+str(3+(ndoublets-i)*8)+" 'MATRIX ELEMENTS BETWEEN STATES ARISING FROM NEIGHBORING MULTIPLETS: I -> I+ "+str(i)+"' "+fichier).readlines()
                        doub=0
                        doub2=0
                        for j in range(6,len(f)):
                                if len(str.split(f[j]))>max:max=len(str.split(f[j]))
                        for j in range(4,len(f)):
                                if len(str.split(f[j]))>max-1:
                                        #print "TEST3",doub,doub+i,doub2,str.split(f[j])[-2]
                                        proba[doub][doub+i][doub2]=float(str.split(f[j])[-2])
                                        doub2=doub2+1
                                        if doub2==2:
                                                doub=doub+1
                                                doub2=0
                                                if doub+doub+i>ndoublets:
                                                        break
                                
#                proba=[]
#                for i in range(6,len(f)):
#                        if len(str.split(f[i]))>14:
#                                proba.append(float(str.split(f[i])[13]))
                maxX=0
                maxY=ener[-1][0]
                for i in range(0,len(mult)):
                        if abs(mult[i][0])>maxX:maxX=abs(mult[i][0])
                fig_x, fig_y =8,8 
                plt.figure(figsize=(fig_x, fig_y))
                ax = plt.subplot(111)
                for j in range(0,2):
                        X=[mult[0][j]-0.5,mult[0][j]+0.5]
                        Y=[ener[0][j],ener[0][j]]
                        ax.plot(X,Y,c="k",linewidth=3)
                        X=[mult[1][j]-0.5,mult[1][j]+0.5]
                        Y=[ener[1][j],ener[1][j]]
                        ax.plot(X,Y,c="k",linewidth=2)
                color="k"
                print("ndoub_represente=",ndoub_represente)
                for i in range(2,ndoublets):
                      if i<=ndoub_represente:
                            for j in range(0,2):
                            	X=[mult[i][j]-0.5,mult[i][j]+0.5]
                            	Y=[ener[i][j],ener[i][j]]
                            	#if abs(mult[i][j])<abs(mult[i-1][j]):
                            	#       ax.plot(X,Y,c=color)    
                            	#if abs(mult[i][j])>abs(mult[i-1][j]):
                            	color="k"
                            	#if color!="r":
                            	ax.plot(X,Y,c=color,linewidth=2) 
		#break
				#if color=="r":break
				#ax.plot(X,Y,c=color)
                t=0
                for i in range(0,ndoublets-1):
#                        if abs(mult[i+1][0])>abs(mult[i][0]):
#                                t=i
#                                break
                         t=ndoub_represente # RAJOUTER

                for i in range(0,ndoublets):
                       if i<=ndoub_represente:
                              if i>t:
                              	break
                              for j in range(i,ndoublets):
                                  if j<=ndoub_represente:
                                       if j>t:
                                       	break
                                       if j==i:
                                       	X=[-1.0*abs(mult[i][0])+0.5,abs(mult[i][0])-0.5]
                                       	Y=[ener[i][0],ener[i][0]]
                                       	ax.plot(X,Y,c="r",linestyle=":")
                                       	pB=np.array((mult[i][0],ener[i][0]))
                                       	pA=np.array((mult[i][1],ener[i][0]))
                                       	pC = (pA+pB)/2
                                       	dx, dy = pA-pB
                                       	x_min, x_max = plt.xlim()
                                       	y_min, y_max = plt.ylim()
                                       	Dx = dx * fig_x / (x_max - x_min)
                                       	Dy = dy * fig_y / (y_max - y_min)
                                       	ecart=y_max/100.0
                                       	angle = (180/np.pi)*np.arctan( Dy / Dx)
                                        if i<=ndoub_val:
                                       	   ax.text((mult[i][1]+mult[i][0])/2,ener[i][0]+ecart,"{val:7.{i}f}".format(i=ndecimal, val=proba[i][j][0]),color='r',fontsize=10,horizontalalignment='center')
         #,rotation=-25.)
                                       elif j==i+1:
                                       	X=[-1.0*abs(mult[i][0])-0.5,-1.0*abs(mult[j][0])-0.5]
                                       	Y=[ener[i][0],ener[j][0]]
                                       	ax.plot(X,Y,c="b",linestyle=":")
                                       	#angle=np.arctan2(((-1.0*abs(mult[j][0])-0.5)-(-1.0*abs(mult[i][0])-0.5)),(ener[j][0]-ener[i][0]))
                                       	#angle=angle*180.0/np.pi
                                       	pB=np.array((X[0],Y[0]))
                                       	pA=np.array((X[1],Y[1]))
                                       	pC = (pA+pB)/2
                                       	dx, dy = pA-pB
                                       	x_min, x_max = plt.xlim()
                                       	y_min, y_max = plt.ylim()
                                       	ecart=y_max/100.0
                                       	ecart_x=x_max/15.0
                                       	Dx = dx * fig_x / (x_max - x_min)
                                       	Dy = dy * fig_y / (y_max - y_min)
                                       	angle = (180/np.pi)*np.arctan( Dy / Dx)
                                       	
                                       	#print angle,'%.2f' %proba[i][j][0],X,Y
                                        if j<=ndoub_val:
                                       	   ax.text(-1.0*ecart_x+(X[0]+X[1])/2,((Y[0]+Y[1])/2)+ecart,"{val:7.{i}f}".format(i=ndecimal, val=proba[i][j][0]),color='b',fontsize=10,horizontalalignment='center',verticalalignment='center',bbox=dict(boxstyle="square",
                   ec=(1., 1., 1.),
                   fc=(1., 1., 1.),
                   )
         )
                                       	X=[-1.0*abs(mult[i][0])+0.5,abs(mult[j][0])+0.5]
                                       	Y=[ener[i][0],ener[j][0]]
                                       	ax.plot(X,Y,c="g",linestyle=":")
                                       	#angle=np.arctan2(X[1]-X[0],Y[1]-Y[0])
                                       	#angle=angle*180.0/np.pi
                                       	pB=np.array((X[0],Y[0]))
                                       	pA=np.array((X[1],Y[1]))
                                       	pC = (pA+pB)/2
                                       	dx, dy = pA-pB
                                       	x_min, x_max = plt.xlim()
                                       	y_min, y_max = plt.ylim()
                                       	Dx = dx * fig_x / (x_max - x_min)
                                       	Dy = dy * fig_y / (y_max - y_min)
                                       	angle = (180/np.pi)*np.arctan( Dy / Dx)
                                       	#print angle,'%.2f' %proba[i][j][1],X,Y
                                        if j<=ndoub_val:
                                       	   ax.text(ecart_x+(X[0]+X[1])/2,((Y[0]+Y[1])/2)-ecart,"{val:7.{i}f}".format(i=ndecimal, val=proba[i][j][1]),color='g',fontsize=10,horizontalalignment='center',bbox=dict(boxstyle="square",
                   ec=(1., 1., 1.),
                   fc=(1., 1., 1.),
                   )
         )
                                       #elif j==i+2:
                                       #	X=[abs(mult[i][0])+0.5,abs(mult[j][0])+0.5]
                                       #	#X=[-1.0*abs(mult[i][0])-0.5,-1.0*abs(mult[j][0])-0.5]
                                       #	Y=[ener[i][0],ener[j][0]]
                                       #	ax.plot(X,Y,c="c",linestyle=":")
                                       #	#angle=np.arctan2(((-1.0*abs(mult[j][0])-0.5)-(-1.0*abs(mult[i][0])-0.5)),(ener[j][0]-ener[i][0]))
                                       #	#angle=angle*180.0/np.pi
                                       #	pB=np.array((X[0],Y[0]))
                                       #	pA=np.array((X[1],Y[1]))
                                       #	pC = (pA+pB)/2
                                       #	dx, dy = pA-pB
                                       #	x_min, x_max = plt.xlim()
                                       #	y_min, y_max = plt.ylim()
                                       #	ecart=y_max/100.0
                                       #	ecart_x=x_max/15.0
                                       #	Dx = dx * fig_x / (x_max - x_min)
                                       #	Dy = dy * fig_y / (y_max - y_min)
                                       #	angle = (180/np.pi)*np.arctan( Dy / Dx)
                                       #
                                       #	#print angle,'%.2f' %proba[i][j][0],X,Y
                                       #	ax.text(-1.0*ecart_x+(X[0]+X[1])/2,((Y[0]+Y[1])/2)+ecart,"{val:7.{i}f}".format(i=ndecimal, val=proba[i][j][0]),color='c',fontsize=10,horizontalalignment='center',verticalalignment='center')
                                       #	X=[abs(mult[i][0])-0.5,-1.0*abs(mult[j][0])-0.5]
                                       #	Y=[ener[i][0],ener[j][0]]
                                       #	ax.plot(X,Y,c="m",linestyle=":")
                                       #	#angle=np.arctan2(X[1]-X[0],Y[1]-Y[0])
                                       #	#angle=angle*180.0/np.pi
                                       #	pB=np.array((X[0],Y[0]))
                                       #	pA=np.array((X[1],Y[1]))
                                       #	pC = (pA+pB)/2
                                       #	dx, dy = pA-pB
                                       #	x_min, x_max = plt.xlim()
                                       #	y_min, y_max = plt.ylim()
                                       #	Dx = dx * fig_x / (x_max - x_min)
                                       #	Dy = dy * fig_y / (y_max - y_min)
                                       #	angle = (180/np.pi)*np.arctan( Dy / Dx)
                                       #	#print angle,'%.2f' %proba[i][j][1],X,Y
                                       #	ax.text(ecart_x+(X[0]+X[1])/2,((Y[0]+Y[1])/2)+ecart,"{val:7.{i}f}".format(i=ndecimal, val=proba[i][j][1]),color='m',fontsize=10,horizontalalignment='center')
                #ax.set_xlim([-4,4])
                #ax.set_ylim([0,600])
#                plt.savefig('barrier.pdf', dpi=100)
                plt.title('Transition Barrier', fontsize=16)
                plt.ylabel(r'$Energy(cm^{-1})$', fontsize=16)
                plt.xlabel(r'$M(\mu_{B})$', fontsize=16)
                #ax.spines['right'].set_visible(False)
                #ax.spines['top'].set_visible(False)
                if rep==1:
                   ax.set_xlim(xmin, xmax)
                   ax.set_ylim(ymin, ymax)
                ax.yaxis.set_ticks_position('left')
                ax.xaxis.set_ticks_position('bottom')

                plt.show()
def main_mag(fichier):        
        #print "Name of the output file"
        #fichier=raw_input("")
        ndoublets=ndoublet(fichier)
        #print "found ",str(ndoublets)," doublets"
        succpetibility(fichier)
        magnetization(fichier)
        if ndoublets%2==0:
                barrier(fichier,ndoublets)
        #else:
         #       print "THIS IS A NON KRAMER STATE SO NO BARRIER WILL BE CALCULATED"
