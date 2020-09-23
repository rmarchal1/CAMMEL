from functools import partial
from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter import filedialog
import tkinter as tk
#import tkfiledialog 
from operator import itemgetter
import os
import sys
sys.path.append('source')
import numpy as np
from pathlib import Path
from operator import itemgetter
#from lecture_output_molcas import *
#from potential import *
from extract_general import *
from magnetization_general import *
#from extraction import *
#from magnetization import *
from PIL import ImageTk, Image


class GUI(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent)   
		self.parent = parent        
		self.initUI()

	def initUI(self):
		self.tkbarrier2=[]
		self.ndoublet_barrier=0
		self.ecrire_wfn=[]
		self.wfn=[]
		self.decompo=[]
		self.ener=[]
		self.multiplet=[]
		self.kramer=''
		self.gtensor=[]
		self.color=[]
		self.barrier_range=tk.IntVar()
		self.barrier_range.set(2)
		self.ndoub_barrier_val=tk.IntVar()
		self.ndoub_barrier_val.set(0)
		self.pot_color=tk.IntVar()
		self.pot_color.set(2)
		self.ndigit_barrier=tk.IntVar()
		self.ndigit_barrier.set(0)
		self.ndoub_barrier=tk.IntVar()
		self.ndoub_barrier.set(0)
		self.multip=tk.IntVar()
		self.multip.set(1)
		self.sampling=tk.IntVar()
		self.sampling.set(60)
		self.surf=tk.IntVar()
		self.thres_extract=tk.DoubleVar()
		self.bar_xmin=tk.DoubleVar()
		self.bar_xmin.set(0.0)
		self.bar_xmax=tk.DoubleVar()
		self.bar_xmax.set(0.0)
		self.bar_ymin=tk.DoubleVar()
		self.bar_ymin.set(0.0)
		self.bar_ymax=tk.DoubleVar()
		self.bar_ymax.set(0.0)
		self.smin=tk.DoubleVar()
		self.smax=tk.DoubleVar()
		self.smin.set(0.0)
		self.smax.set(0.0)
		self.smin2=tk.DoubleVar()
		self.smax2=tk.DoubleVar()
		self.smin2.set(0.0)
		self.smax2.set(0.0)
		self.smin3=tk.DoubleVar()
		self.smax3=tk.DoubleVar()
		self.smin3.set(0.0)
		self.smax3.set(0.0)
		self.smin4=tk.DoubleVar()
		self.smax4=tk.DoubleVar()
		self.smin4.set(0.0)
		self.smax4.set(0.0)
		self.thres_extract.set(0.0)
		self.surf.set(1)
		self.easy=tk.IntVar()
		self.easy.set(2)
		self.gx=tk.IntVar()
		self.gx.set(0)
		self.gy=tk.IntVar()
		self.gy.set(0)
		self.gz=tk.IntVar()
		self.gz.set(0)
		self.type_plot=tk.IntVar()
		self.type_plot.set(1)
		self.axis=tk.IntVar()
		self.axis.set(1)
		self.coord=tk.IntVar()
		self.coord.set(4)
		self.dosspindec=tk.IntVar()
		self.dosspindec.set(0)
		self.attype=[]
		self.v = tk.IntVar()
		self.v.set(1)
		self.withaxis=tk.IntVar()
		self.supera=tk.IntVar()
		self.superb=tk.IntVar()
		self.superc=tk.IntVar()
		self.supera.set(1)
		self.superb.set(1)
		self.superc.set(1)
		self.withaxis.set(1)
		self.radius=tk.DoubleVar()
		self.radius.set(0.0)
		self.parent.title("MOLCAS Toolbox")
		self.parent.geometry("%dx%d%+d%+d" % (300, 200, 0, 0))
		self.pack(fill=BOTH, expand=1)
		self.typedecomp=tk.IntVar()
		self.typedecomp.set(1)
		self.fatdecom=[]
		self.testdict={}
		self.butnodosdec={}
		self.buttdecomptype={}
		self.fatdecom=dict()
		self.fatspin=tk.IntVar()
		self.fatspin.set(1)
		self.menubar = Menu(self.parent)
		self.parent.config(menu=self.menubar)
		
		fileMenu = Menu(self.menubar)
		self.computeMenu = Menu(self.menubar) 
		fileMenu.add_command(label="Open", command=self.onOpen)
		self.menubar.add_cascade(label="File", menu=fileMenu)
		#self.computeMenu.add_command(label="Show struct", command=self.showstruct)        
#		self.atlist=atome_list(self.path)
#		print(self.atlist)
#		for i in range(0,len(self.atlist)):
#		     self.fatdecom.append("")
#		self.txt = Text(self)
#		self.txt.pack(fill=BOTH, expand=1)
	
	def create_window(self,name,text):
		self.name = tk.Toplevel()
		self.name.geometry("%dx%d%+d%+d" % (800, 300, 800, 125))
		self.parent.title("Test")
		self.name.title(text)
	def create_window2(self,name,text):
		self.name = tk.Toplevel()
		self.name.geometry("%dx%d%+d%+d" % (1000, 1000, 800, 125))
		self.parent.title("Test")
		self.name.title(text)
	def create_window3(self,name,text):
		self.name = tk.Toplevel()
		self.name.geometry("%dx%d%+d%+d" % (100, 300, 1000, 525))
		self.parent.title("Test")
		self.name.title(text)
		ploti()      
		Label(name, text=text).pack(padx=30, pady=30)
#	def nothing(self):
#	   pass
	def extract_path(self, filename):
		for i in range(len(filename)-1,0,-1):
			if filename[i]=='/':
				path=filename[0:i+1]
				break
		return(path)
	def readFile(self, filename):
	
		f = open(filename, "r")
		text = f.read()
		return text
	
	def onOpen(self):
		try:
			self.menubar.delete("Compute")
		except:
			pass
		self.computeMenu = Menu(self.menubar)
		ftypes = [('Molcas output','*out *.log')]
		currentPath = os.getcwd()
		dlg = filedialog.Open(self, filetypes = ftypes)
		fl = dlg.show()
		self.fileto=fl
		#print(self.fileto)
		self.menubar.add_cascade(label="Compute", menu=self.computeMenu)
		self.kramer='y'
		self.ndoublets=ndoublet_extract(self.fileto)
		#print("TEST",self.ndoublets)
		ndoublets2=int(self.ndoublets/2)+self.ndoublets%2
		if self.ndoublets%2==1:
			self.kramer="n"
		#print(self.kramer)
		if self.kramer=="y":
			self.gtensor=extract_tensor(np.zeros((ndoublets2,3)),self.fileto)
			self.ener=energies(self.fileto,ndoublets2)
			self.wfn=extract_wfn(np.zeros((2*ndoublets2,2*ndoublets2,2)),self.fileto)
			self.decompo=extract_decomp(self.wfn,np.zeros((ndoublets2,ndoublets2)))
		else:
			self.multiplet=mult(self.ndoublets,self.fileto)
			self.gtensor=extract_tensor_nonkramer(np.zeros((len(self.multiplet),3)),self.fileto,self.multiplet,np.zeros((2*(self.ndoublets-1)+1,3)))
			#print(self.multiplet)
			self.ener=energies_nonkramer(self.fileto,2*(ndoublets2-1)+1)
			self.wfn=extract_wfn_nonkramer(np.zeros((2*(ndoublets2-1)+1,2*(ndoublets2-1)+1,2)),self.fileto)
			self.decompo=extract_decomp_nonkramer(self.wfn,np.zeros((2*(ndoublets2-1)+1,2*(ndoublets2-1)+1)))
		#print(self.decompo)
		if len(self.decompo)>0:
			self.computeMenu.add_command(label="Extract WaveFunction", state="normal", command=self.extract_window)
		else:
			self.computeMenu.add_command(label="Extract WaveFunction", state="disabled")
		f=os.popen("grep -i -A1 'Temperature depEndence of the magnetic susceptibility calculated in' "+self.fileto+" | wc -l").readlines()
		test_succept=int(f[0])
		if test_succept>0:
			self.computeMenu.add_command(label="Succeptibily", state="normal", command=self.plot_succept)
		else:
			self.computeMenu.add_command(label="Succeptibily", state="disabled")
		f=os.popen("grep 'CALCULATION OF THE MOLAR MAGNETIZATION' "+self.fileto+" | wc -l").readlines()
		test_magnet=int(f[0])
		if test_magnet>0:
			self.computeMenu.add_command(label="Magnetization", state="normal", command=self.plot_magnet)
		else:
			self.computeMenu.add_command(label="Magnetization", state="disabled")
		if self.kramer=='y':
			f=os.popen("grep 'BARRIER' "+self.fileto+" | wc -l").readlines()
			test_barrier=int(f[0])
			if test_barrier>0:
				self.computeMenu.add_command(label="Magnetization barrier", state="normal", command=self.plot_barrier_window)
			else:
				self.computeMenu.add_command(label="Magnetization barrier", state="disabled")
		f=os.popen("grep 'ATOMIC DOMAIN' "+self.fileto+" | wc -l").readlines()
		test_potential=int(f[0])
		if test_potential>0:
			self.computeMenu.add_command(label="Potential", state="normal", command=self.potential_window)
		else:
			self.computeMenu.add_command(label="Potential", state="disabled")


	def plot_barrier_window(self):
		try:
			for i in range(0,len(self.tkbarrier)):
				self.tkbarrier.destroy()
		except:
			pass

		name="Window"
		self.create_window(name,"Transition Barrier")
		self.ndoublet_barrier=ndoublet_magnetization(self.fileto)
		self.tkbarrier=[]
		self.tkbarrier.append(tk.Label(self.name, text=str(self.ndoublet_barrier)+" doublets where fouund"))
		self.tkbarrier[len(self.tkbarrier)-1].grid(row=1, column=1,columnspan=2)
		self.tkbarrier.append(tk.Label(self.name, text="How much doublet do you want to consider"))
		self.tkbarrier[len(self.tkbarrier)-1].grid(row=2, column=1)
		self.tkbarrier.append(tk.Entry(self.name, bd =5, textvariable=self.ndoub_barrier))
		self.tkbarrier[len(self.tkbarrier)-1].grid(row=2,column=2)
		self.tkbarrier.append(tk.Label(self.name, text="How much doublet do you want to consider for the values"))
		self.tkbarrier[len(self.tkbarrier)-1].grid(row=3, column=1)
		self.tkbarrier.append(tk.Entry(self.name, bd =5, textvariable=self.ndoub_barrier_val))
		self.tkbarrier[len(self.tkbarrier)-1].grid(row=3,column=2)
		self.tkbarrier.append(tk.Label(self.name, text="How much digits for the values"))
		self.tkbarrier[len(self.tkbarrier)-1].grid(row=4, column=1)
		self.tkbarrier.append(tk.Entry(self.name, bd =5, textvariable=self.ndigit_barrier))
		self.tkbarrier[len(self.tkbarrier)-1].grid(row=4,column=2)
		function_test=partial(self.bar_range,6)
		self.tkbarrier.append(tk.Label(self.name, text="Specific axis range"))
		self.tkbarrier[len(self.color)-1].grid(row=5,column=1)
		self.tkbarrier.append(tk.Radiobutton(self.name, text='Yes ', variable=self.barrier_range, value=1, command=function_test))
		self.tkbarrier[len(self.color)-1].grid(row=5,column=2)
		self.tkbarrier.append(tk.Radiobutton(self.name, text='No ', variable=self.barrier_range, value=2, command=function_test))
		self.tkbarrier[len(self.color)-1].grid(row=5,column=3)
		
		self.tkbarrier.append(tk.Button(self.name, text="Show barrier", command=self.plot_barrier))
		self.tkbarrier[len(self.tkbarrier)-1].grid(row=8,column=1,columnspan=2)


	def bar_range(self,value):
		try:
			for i in range(0,len(self.tkbarrier2)):
				self.tkbarrier2[i].destroy()
			self.tkbarrier2=[]
		except:
			pass

		if self.barrier_range.get()==1:
			self.tkbarrier2.append(tk.Label(self.name, text="xmin"))
			self.tkbarrier2[len(self.tkbarrier2)-1].grid(row=value,column=1)
			self.tkbarrier2.append(tk.Label(self.name, text="xmax"))
			self.tkbarrier2[len(self.tkbarrier2)-1].grid(row=value,column=3)
			self.tkbarrier2.append(tk.Entry(self.name, bd =5, textvariable=self.bar_xmin))	
			self.tkbarrier2[len(self.tkbarrier2)-1].grid(row=value,column=2)
			self.tkbarrier2.append(tk.Entry(self.name, bd =5, textvariable=self.bar_xmax))
			self.tkbarrier2[len(self.tkbarrier2)-1].grid(row=value,column=4)
			self.tkbarrier2.append(tk.Label(self.name, text="ymin"))
			self.tkbarrier2[len(self.tkbarrier2)-1].grid(row=value+1,column=1)
			self.tkbarrier2.append(tk.Label(self.name, text="ymax"))
			self.tkbarrier2[len(self.tkbarrier2)-1].grid(row=value+1,column=3)
			self.tkbarrier2.append(tk.Entry(self.name, bd =5, textvariable=self.bar_ymin))
			self.tkbarrier2[len(self.tkbarrier2)-1].grid(row=value+1,column=2)
			self.tkbarrier2.append(tk.Entry(self.name, bd =5, textvariable=self.bar_ymax))
			self.tkbarrier2[len(self.tkbarrier2)-1].grid(row=value+1,column=4)

	def plot_barrier(self):
				
		barrier(self.fileto,self.ndoublet_barrier,self.ndoub_barrier.get()-1,self.ndigit_barrier.get(),self.ndoub_barrier_val.get()-1,self.barrier_range.get(),self.bar_xmin.get(),self.bar_xmax.get(),self.bar_ymin.get(),self.bar_ymax.get())


	def plot_magnet(self):
		magnetization(self.fileto)

	def plot_succept(self):
		succpetibility(self.fileto)

	def des_easy(self,value):
		if self.easy.get()==1:
		  try:
		    self.rad1.destroy()
		    self.rad2.destroy()
		    self.rad3.destroy()
		    self.label.destroy()
		    self.label2.destroy()
		    self.entry.destroy()
		  except:
		    pass
		
		  self.rad1=tk.Checkbutton(self.name, text='gX ', variable=self.gx)
		  self.rad2=tk.Checkbutton(self.name, text='gY ', variable=self.gy)
		  self.rad3=tk.Checkbutton(self.name, text='gZ ', variable=self.gz)
		  self.rad1.grid(row=value+1,column=2)
		  self.rad2.grid(row=value+1,column=3)
		  self.rad3.grid(row=value+1,column=4)
		  self.label2=tk.Label(self.name, text='Which multiplet')
		  self.label2.grid(row=value+2, column=1)
		  self.entry=tk.Entry(self.name, bd =5, textvariable=self.multip)
		  self.entry.grid(row=value+2,column=2)
		  self.label=tk.Label(self.name, text="Which axis")
		  self.label.grid(row=value+1,column=1)
		else:
		  try:
		    self.rad1.destroy()
		    self.rad2.destroy()
		    self.rad3.destroy()
		    self.label.destroy()
		    self.label2.destroy()
		    self.entry.destroy()
		  except:
		    pass


	def potential_window(self):
		name="Window"
		f=os.popen("echo $CAMMEL").readlines()
		
		self.create_window2(name,"Electrostatic potential")
		self.photo = ImageTk.PhotoImage(file =str.split(f[0])[0]+'/source/cammel_color2.png')
		espace_image = tk.Canvas(self.name, width =340, height =340)
		espace_image.grid(row=1, column=1, columnspan=23,padx =10, pady =10)
		espace_image.create_image(170, 170, image =self.photo)
		tk.Label(self.name, text="Radius around the \n Lantanide atom (bohr)").grid(row=2,column=1)
		tk.Entry(self.name, bd =5, textvariable=self.radius).grid(row=2,column=2)
		tk.Label(self.name, text="How much values for \n the sampling (60 is a good compromise)").grid(row=3,column=1)
		tk.Entry(self.name, bd =5, textvariable=self.sampling).grid(row=3,column=2)
		tk.Label(self.name, text="Which surface \n for the mapping").grid(row=4,column=1)
		tk.Radiobutton(self.name, text='The potential ', variable=self.surf, value=1).grid(row=4,column=2)
		tk.Radiobutton(self.name, text='A sphere ', variable=self.surf, value=2).grid(row=4,column=3)
#		tk.Label(self.name, text="Do you want to fix specific \n extrema for the potential?").grid(row=5,column=1)
#		tk.Radiobutton(self.name, text='Yes ', variable=self.pot_color, value=1, command=self.represente_color).grid(row=5,column=2)
#		tk.Radiobutton(self.name, text='No ', variable=self.pot_color, value=2, command=self.represente_color).grid(row=5,column=3)
		self.color=[]
		self.row=6
		function_test=partial(self.des_easy,self.row)
		self.color.append(tk.Label(self.name, text="Show the easy axis?"))
		self.color[len(self.color)-1].grid(row=6,column=1)
		self.color.append(tk.Radiobutton(self.name, text='Yes ', variable=self.easy, value=1, command=function_test))
		self.color[len(self.color)-1].grid(row=6,column=2)
		self.color.append(tk.Radiobutton(self.name, text='No ', variable=self.easy, value=2, command=function_test))
		self.color[len(self.color)-1].grid(row=6,column=3)
		self.color.append(tk.Label(self.name, text="Do you want to plot"))
		self.color[len(self.color)-1].grid(row=self.row+3,column=1)
		self.color.append(tk.Radiobutton(self.name, text='The potential only ', variable=self.type_plot, value=1))
		self.color[len(self.color)-1].grid(row=self.row+3,column=2)
		self.color.append(tk.Radiobutton(self.name, text='The potential and its decomposition ', variable=self.type_plot, value=2))
		self.color[len(self.color)-1].grid(row=self.row+3,column=3)
		self.color.append(tk.Label(self.name, text="Do you want to \n see the molecule"))
		self.color[len(self.color)-1].grid(row=self.row+4,column=1)
		self.color.append(tk.Radiobutton(self.name, text='All ', variable=self.coord, value=1))
		self.color[len(self.color)-1].grid(row=self.row+4,column=2)
		self.color.append(tk.Radiobutton(self.name, text='First coordination sphere ', variable=self.coord, value=3))
		self.color[len(self.color)-1].grid(row=self.row+4,column=4)
		self.color.append(tk.Radiobutton(self.name, text='No ', variable=self.coord, value=4))
		self.color[len(self.color)-1].grid(row=self.row+4,column=5)
		self.color.append(tk.Radiobutton(self.name, text='All except H atoms', variable=self.coord, value=2))
		self.color[len(self.color)-1].grid(row=self.row+4,column=3)
		self.color.append(tk.Button(self.name, text="Map the potential", command=self.computepotential))
		self.color[len(self.color)-1].grid(row=self.row+5,column=1,columnspan=23)
		self.color.append(tk.Label(self.name, anchor="w", text="OpenGL button"))
		self.color[len(self.color)-1].grid(sticky="W",row=self.row+6,column=1,columnspan=23)
		self.color.append(tk.Label(self.name, anchor="w", text="l for removing/showing atom legend"))
		self.color[len(self.color)-1].grid(sticky="W",row=self.row+7,column=1,columnspan=23)
		self.color.append(tk.Label(self.name, anchor="w", text="z for removing/showing zoom and rotation values"))
		self.color[len(self.color)-1].grid(sticky="W",row=self.row+8,column=1,columnspan=23)
		self.color.append(tk.Label(self.name, anchor="w", text="c for removing/showing cartesian axes"))
		self.color[len(self.color)-1].grid(sticky="W",row=self.row+9,column=1,columnspan=23)
		self.color.append(tk.Label(self.name, anchor="w", text="Shift+mouse for rotation over z"))
		self.color[len(self.color)-1].grid(sticky="W",row=self.row+10,column=1,columnspan=23)
		self.color.append(tk.Label(self.name, anchor="w", text="+/- zooming and unzooming the potential"))
		self.color[len(self.color)-1].grid(sticky="W",row=self.row+11,column=1,columnspan=23)
		self.color.append(tk.Label(self.name, anchor="w", text="p/m zooming and unzooming the molecule"))
		self.color[len(self.color)-1].grid(sticky="W",row=self.row+12,column=1,columnspan=23)
		self.color.append(tk.Label(self.name, anchor="w", text="P/M zooming and unzooming the easy axis"))
		self.color[len(self.color)-1].grid(sticky="W",row=self.row+13,column=1,columnspan=23)
		self.color.append(tk.Label(self.name, anchor="w", text="h/f right/left translation"))
		self.color[len(self.color)-1].grid(sticky="W",row=self.row+14,column=1,columnspan=23)
		self.color.append(tk.Label(self.name, anchor="w", text="t/b up/down translation"))
		self.color[len(self.color)-1].grid(sticky="W",row=self.row+15,column=1,columnspan=23)
		self.color.append(tk.Label(self.name, anchor="w", text="s for a screenshot"))
		self.color[len(self.color)-1].grid(sticky="W",row=self.row+16,column=1,columnspan=23)
		self.color.append(tk.Label(self.name, anchor="w", text="g remove easy axis legend"))
		self.color[len(self.color)-1].grid(sticky="W",row=self.row+17,column=1,columnspan=23)

	def extract_window(self):
		name="Window"
		self.create_window(name,"WaveFunction Extraction")
		tk.Label(self.name, text='Threshold for the \n wavefunction coeff').grid(row=1,column=0,columnspan=4)
		tk.Entry(self.name, bd =5, textvariable=self.thres_extract).grid(row=1,column=4,columnspan=4)
		tk.Button(self.name, text="Extract", command=self.extract_output).grid(row=1,column=8,columnspan=2)
	def extract_output(self):
		#print("test thre",float(self.thres_extract.get()))
		if self.kramer=='y':
			self.ecrire_wfn=ecriture(self.decompo,self.gtensor,self.ener,float(self.thres_extract.get()),self.kramer)
		else:
			self.ecrire_wfn=ecriture_nonkramer(self.decompo,self.gtensor,self.ener,float(self.thres_extract.get()),self.kramer,self.multiplet)
		try:
			for i in range(0,len(self.tableau_extract)):
				self.tableau_extract[i].destroy()
		except:
			pass
		ecrire=[]
		maxlong=np.zeros(5)
		for i in range(0,len(self.ecrire_wfn)):
			for j in range(0,len(self.ecrire_wfn[i])-1):
				if len(self.ecrire_wfn[i][j])>maxlong[j]:maxlong[j]=len(self.ecrire_wfn[i][j])
				self.ecrire_wfn[i][j]=self.ecrire_wfn[i][j]
		for i in range(0,len(self.ecrire_wfn)):
			ecrire2=''
			for j in range(0,len(self.ecrire_wfn[i])-1):
				for k in range(len(self.ecrire_wfn[i][j]),int(maxlong[j])+2):
					self.ecrire_wfn[i][j]=self.ecrire_wfn[i][j]+" "
				ecrire2=ecrire2+self.ecrire_wfn[i][j]+'|'
			ecrire2=ecrire2+self.ecrire_wfn[i][len(self.ecrire_wfn[i])-1]
			ecrire.append(ecrire2)
			#print(ecrire2)			

		self.tableau_extract=[]
		self.tableau_extract.append(tk.Label(self.name, text='Results are printed in the'+self.fileto+'_wfn file', anchor='w', justify='left'))
		self.tableau_extract[len(self.tableau_extract)-1].grid(row=2,column=0,columnspan=23, sticky='we')
#		for i in range(0,len(self.ecrire_wfn)):
#			for j in range(0,len(self.ecrire_wfn[i])):
#				self.tableau_extract.append(tk.Label(self.name, text=ecrire[i], anchor='w', justify='left'))
#				self.tableau_extract[len(self.tableau_extract)-1].grid(row=i+3,column=1,columnspan=3, sticky='we')
		
		for i in range(0,len(self.ecrire_wfn)):
			col=0
			for j in range(0,len(self.ecrire_wfn[i])):
				self.tableau_extract.append(tk.Label(self.name, text=self.ecrire_wfn[i][j], anchor='w', justify='left'))
				self.tableau_extract[len(self.tableau_extract)-1].grid(row=i+3,column=col, sticky='we')
				col=col+1
				if j < len(self.ecrire_wfn[i])-1:
					self.tableau_extract.append(tk.Label(self.name, text="|", anchor='w', justify='left'))
					self.tableau_extract[len(self.tableau_extract)-1].grid(row=i+3,column=col, sticky='we')
					col=col+1
	#	pm=chr(177)
	#	maxi=np.zeros(5)
		#for i in range(0,len(self.ecrire_wfn[0])-1):
	#		maxi[i]=len(ecrire[0][i])
		ecriture2=open(self.fileto+"_wfnfile",'w')	
		for i in range(0,len(self.ecrire_wfn)):
			for j in range(0,len(self.ecrire_wfn[i])-1):
				ecriture2.write(self.ecrire_wfn[i][j]+'|')
			ecriture2.write(self.ecrire_wfn[i][len(self.ecrire_wfn[i])-1])
			ecriture2.write('\n')
#		print(self.ecrire_wfn)


	def computepotential(self):
		if self.radius.get()!=0.0:
		   if self.surf.get()==1: surf='p'
		   else: surf='s'
		   if self.easy.get()==1: easy='y'
		   else: easy='n'
		   if self.type_plot.get()==1: type_plot='p'
		   else: type_plot='a'
		   if self.coord.get()==1: coord='y'
		   elif self.coord.get()==3: coord='s'
		   elif self.coord.get()==2: coord='ynh'
		   else: coord='n'
		   if self.axis.get()==1: axis='y'
		   else: axis='n'
#		selfa.test()
		os.system("$CAMMEL/source/prog_pot_opengl.py "+self.fileto+" "+str(self.radius.get())+" "+str(self.sampling.get())+" "+surf+" "+easy+" "+type_plot+" "+coord+" "+axis+" "+str(self.gx.get())+" "+str(self.gy.get())+" "+str(self.gz.get())+" "+str(self.multip.get()-1)+" "+str(self.smin.get())+" "+str(self.smax.get())+" "+str(self.smin2.get())+" "+str(self.smax2.get())+" "+str(self.smin3.get())+" "+str(self.smax3.get())+" "+str(self.smin4.get())+" "+str(self.smax4.get()))
		#pot_main(self.fileto,self.radius.get(),self.sampling.get(),surf,easy,type_plot,coord,axis,self.gx.get(),self.gy.get(),self.gz.get(),self.multip.get()-1,self.smin.get(),self.smax.get(),self.smin2.get(),self.smax2.get(),self.smin3.get(),self.smax3.get(),self.smin4.get(),self.smax4.get())



def main():

    root = Tk()
    ex = GUI(root)
    root.geometry("300x250+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()  



      
       

         
