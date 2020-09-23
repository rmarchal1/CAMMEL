from operator import itemgetter
import os
import numpy as np


def extract_tensor(ten,fich):
        for i in range(0,len(ten)):
                f=os.popen("grep -A20 'CALCULATION OF PSEUDOSPIN HAMILTONIAN TENSORS FOR THE MULTIPLET "+str(i+1)+"' "+fich).readlines()
                for j in range(0,len(f)):
                        if len(str.split(f[j]))>0:
                                if str.split(f[j])[0]=="MAIN":
                                        ten[i][0]=float(str.split(f[j+2])[2])
                                        ten[i][1]=float(str.split(f[j+3])[2])
                                        ten[i][2]=float(str.split(f[j+4])[2])
                                        break
        #print ten
        return(ten)

def extract_tensor_nonkramer(ten,fich,mult,ten2):
        for i in range(0,len(ten)):
                f=os.popen("grep -A20 'CALCULATION OF PSEUDOSPIN HAMILTONIAN TENSORS FOR THE MULTIPLET "+str(i+1)+"' "+fich).readlines()
                for j in range(0,len(f)):
                        if len(str.split(f[j]))>0:
                                if str.split(f[j])[0]=="MAIN":
                                        ten[i][0]=float(str.split(f[j+2])[2])
                                        ten[i][1]=float(str.split(f[j+3])[2])
                                        ten[i][2]=float(str.split(f[j+4])[2])
                                        break
        #print ten
        for i in range(0,len(mult)):
                #print mult[i]-1,len(ten),i,len(ten2)
                for j in range(0,3):
                        ten2[i][j]=ten[int(mult[i])-1][j]
        return(ten2)


def energies(fichier,ndoublets):
        f=os.popen("grep -A"+str(1+ndoublets*2)+" 'LOW-LYING SPIN-ORBIT ENERGIES:' "+fichier).readlines()
        version=0
        energies=np.zeros(ndoublets)
        try:
                float(str.split(f[1])[0])
                version=80
                energies[0]=float(str.split(f[1])[0])
                doub=1
                t=0
                for i in range(1,len(f)):
                        for j in range(0,len(str.split(f[i]))):
                                if float(str.split(f[i])[j])!=energies[doub-1]:
                                        energies[doub]=float(str.split(f[i])[j])
                                        doub=doub+1
                                        if doub==ndoublets:
                                                t=1
                                                break
                        if t==1:break
        except:
                version=84
                energies[0]=float(str.split(f[1])[-1])
                doub=1
                for i in range(1,len(f)):
                        if float(str.split(f[i])[-1])!=energies[doub-1]:
                                energies[doub]=float(str.split(f[i])[-1])
                                doub=doub+1
                                if doub==ndoublets:
                                        t=1
                                        break
                        
        doub=1
        return(energies)

def energies_nonkramer(fichier,ndoublets):
        f=os.popen("grep -A"+str(1+ndoublets*2)+" 'LOW-LYING SPIN-ORBIT ENERGIES:' "+fichier).readlines()
        version=0
        energies=np.zeros(ndoublets)
        try:
                float(str.split(f[1])[0])
                version=80
                energies[0]=float(str.split(f[1])[0])
                doub=1
                t=0
                for i in range(1,len(f)):
                        for j in range(0,len(str.split(f[i]))):
                                if float(str.split(f[i])[j])!=energies[doub-1]:
                                        energies[doub]=float(str.split(f[i])[j])
                                        doub=doub+1
                                        if doub==ndoublets:
                                                t=1
                                                break
                        if t==1:break
        except:
                version=84
                energies[0]=float(str.split(f[1])[-1])
                doub=1
                for i in range(1,len(f)):
                        if float(str.split(f[i])[-1])!=energies[doub-1]:
                                energies[doub]=float(str.split(f[i])[-1])
                                doub=doub+1
                                if doub==ndoublets:
                                        t=1
                                        break

        doub=1
        return(energies)
                

def ndoublet_extract(fich):
#        print("debut ndoub")
        f=os.popen("grep '| JM > |' "+fich).readlines()
        #os.system("grep '| JM > |' "+fich)
#        print("TESTSA",f)
        return(int(str.split(f[len(f)-1])[-2]))

def extract_wfn(wfn,fichier):
        f=os.popen("grep -A"+str(len(wfn)+1)+" '| JM > ' "+fichier).readlines()
        doublet=0
        values=[]
        for i in range(0,len(f)):
                if not "--" in str.split(f[i])[0] and not "| JM >" in f[i]:
                                f[i]=f[i].replace("|"," | ")
                                values.append(f[i])
        #print values
        nvalues=0
        values_new=[]
        for i in range(0,len(str.split(values[0]))-1):
                
                if not "%" in str.split(values[0])[i+1]:
                        try:
                                float(str.split(values[0])[i])
                                nvalues=nvalues+1
                                
                        except:
                                pass
                
        #print nvalues
        ngroup=int(len(wfn)/(0.5*nvalues))
        size=int(len(wfn)/ngroup)
        #print ngroup
        ligne=0
        value_pos=0
        for i in range(0,ngroup):
                #wave=0
                for k in range(0,len(wfn)):
                        wave=0
                        comp=0
                        for j in range(0,len(str.split(values[ligne]))-1):      
                                if not "%" in str.split(values[ligne])[j+1]:
                                        try:
                                                wfn[i*size+wave][k][comp]=float(str.split(values[ligne])[j])
                                                #if i==0:
                                                #       print float(str.split(values[ligne])[j]),i*ngroup+wave,
                                                comp=comp+1
                                                
                                                
                                                if comp==2:
                                                        comp=0
                                                        wave=wave+1
                                        except:
                                                pass
                        ligne=ligne+1
#       for i in range(ngroup*size,len(wfn)):
        if len(wfn)%ngroup !=0:
                for k in range(0,len(wfn)):
                        wave=0
                        comp=0
                        for j in range(0,len(str.split(values[ligne]))-1):
                                if not "%" in str.split(values[ligne])[j+1]:
                                        try:
                                                wfn[ngroup*size+wave][k][comp]=float(str.split(values[ligne])[j])
                                                comp=comp+1
                                                if comp==2:
                                                        comp=0
                                                        wave=wave+1
                                        except:
                                                pass
                        ligne=ligne+1

        #for i in range(0,len(wfn)):
#               print "WAVE ",i
#               for j in range(0,len(wfn)):
#                       print wfn[i][j]
        return(wfn)


def extract_decomp(wfn,decomp):
        wave=0
        for i in range(0,len(wfn),2):
                for j in range(0,len(decomp)):
                        for k in range(0,2):
                                decomp[wave][j]=decomp[wave][j]+(wfn[i][j][k]**2)*100.0
                                decomp[wave][j]=decomp[wave][j]+(wfn[i][len(wfn)-1-j][k]**2)*100.0
                wave=wave+1
        for i in range(0,len(decomp)):
                tot=0
                #print "decomp ",i+1,decomp[i]
                for j in range(0,len(decomp)):
                        tot=tot+decomp[i][j]
                #print "TOT",tot
        return(decomp)
def extract_wfn_nonkramer(wfn,fichier):
        f=os.popen("grep -A"+str(len(wfn)+1)+" '| JM > ' "+fichier).readlines()
        doublet=0
        values=[]
        for i in range(0,len(f)):
                if not "--" in str.split(f[i])[0] and not "| JM >" in f[i]:
                                f[i]=f[i].replace("|"," | ")
                                values.append(f[i])
        #print values
        nvalues=0
        values_new=[]
        for i in range(1,len(str.split(values[0]))-1):
                
                if not "%" in str.split(values[0])[i+1]:
                        try:
                                int(str.split(values[0])[i])
                                
                        except:
                                try:
                                        float(str.split(values[0])[i])
                                        nvalues=nvalues+1
                                        
                                except:
                                        pass
                
        #print "nvalues=",nvalues
        ngroup=int(len(wfn)/(0.5*nvalues))
        size=int(len(wfn)/ngroup)
        #print ngroup
        ligne=0
        value_pos=0
        #print "nvalues=",nvalues,ngroup
        for i in range(0,ngroup):
                #wave=0
                for k in range(0,len(wfn)):
                        wave=0
                        comp=0
                        for j in range(1,len(str.split(values[ligne]))-1):      
                                if not "%" in str.split(values[ligne])[j+1]:
                                        try:
                                                int(str.split(values[ligne])[j])
                                        except:
                                                try:
                                                        wfn[i*size+wave][k][comp]=float(str.split(values[ligne])[j])
                                                        #if i==0:
                                                        #       print float(str.split(values[ligne])[j]),i*ngroup+wave,
                                                        comp=comp+1
                                                        
                                                        
                                                        if comp==2:
                                                                comp=0
                                                                wave=wave+1
                                                except:
                                                        pass
                        ligne=ligne+1
#       for i in range(ngroup*size,len(wfn)):
        if len(wfn)%ngroup !=0:
                for k in range(0,len(wfn)):
                        wave=0
                        comp=0
                        for j in range(1,len(str.split(values[ligne]))-1):
                                if not "%" in str.split(values[ligne])[j+1]:
                                        try:
                                                int(str.split(values[ligne])[j])
                                        except:
                                                try:
                                                        wfn[ngroup*size+wave][k][comp]=float(str.split(values[ligne])[j])
                                                        comp=comp+1
                                                        if comp==2:
                                                                comp=0
                                                                wave=wave+1
                                                except:
                                                        pass
                        ligne=ligne+1

#       for i in range(0,len(wfn)):
#               print "WAVE ",i
#               for j in range(0,len(wfn)):
#                       print wfn[i][j]
        return(wfn)

def extract_decomp_nonkramer(wfn,decomp):
        wave=0
        #print "TESTSA",int(len(decomp)/2)
        for i in range(0,len(wfn)):
                for j in range(0,int(len(decomp)/2)):
                        
                        for k in range(0,2):
                                decomp[i][j]=decomp[i][j]+(wfn[i][j][k]**2)*100.0
                                decomp[i][j]=decomp[i][j]+(wfn[i][len(wfn)-j-1][k]**2)*100.0
                for k in range(0,2):
                        decomp[i][int(len(decomp)/2)]=decomp[i][int(len(decomp)/2)]+(wfn[i][int(len(decomp)/2)][k]**2)*100.0
#               print "WFN=",wfn[i]
                #print "decomp=",decomp[i]
#       print "TEST DECOMP",int(len(decomp)/2)
#       for i in range(0,len(wfn)):
#               
#               for j in range(0,int(len(decomp)/2)+1):
#                       for k in range(0,2):
#                               decomp[wave][j]=decomp[wave][j]+(wfn[i][j][k]**2)*100.0
#                               decomp[wave][j]=decomp[wave][j]+(wfn[i][len(wfn)-1-j][k]**2)*100.0
#               for k in range(0,2):
#                       decomp[wave][int(len(decomp)/2)+1]=decomp[wave][int(len(decomp)/2)+1]+(wfn[i][int(len(decomp)/2)+1][k]**2)*100.0
#               wave=wave+1
#       
#       for i in range(0,len(decomp)):
#               tot=0
#               #print "decomp ",i+1,decomp[i]
#               for j in range(0,len(decomp)):
#                       tot=tot+decomp[i][j]
#               #print "TOT",tot
        return(decomp)

def ecriture(decomp,tensor,ener,thre,kram):
        #ecriture=open("extract.txt",'wb')
        ecrire=[]
        ecrire.append(["doublet "," E(cm-1) ","   gx   ","   gy   ","   gz   "," WFT"])
        wfnout=[]
        #decomp=sorted(decomp,reverse=True)
        #print(len(decomp)*2,kram)
        decomp2=[]
        STATE=[]
        if kram=='y':
                for i in range(len(decomp)*2-1,0,-2):
                        #print str(i)+'/2'
                        STATE.append(str(i)+'/2')
        else:
                for i in range((len(decomp)-1)/2,-1,-1):
                        #print str(i)
                        STATE.append(str(i))
        #print STATE
        for i in range(0,len(decomp)):
                wfnout2=""
                decomp3=[]
                #print decomp[i]
                for j in range(0,len(decomp)):
                        #print "TESTS",len(decomp[i])
                        decomp3.append([STATE[j],decomp[i][j]])
                decomp3=sorted(decomp3,key=itemgetter(1),reverse=True)
                decomp2.append(decomp3)
#       print "TESTS"
        ecrirewfn=[]
        #pm='\xc2\xb1'
        pm=chr(177)
        maxi=np.zeros(5)
        for i in range(0,len(ecrire[0])-1):
                maxi[i]=len(ecrire[0][i])
        #print "len decomp2",len(decomp2)
        for i in range(0,len(decomp2)):
                ecrirewfn2=''
                for j in range(0,len(decomp2)):
                        if decomp2[i][j][1]>thre:ecrirewfn2=ecrirewfn2+'%4.1f' %decomp2[i][j][1]+' '+pm+' '+decomp2[i][j][0]+'> + '
                #print ecrirewfn2[:-2]
                ecrirewfn.append(ecrirewfn2)
                #print i,ecrirewfn2[:-2]
                #ecriture.write(ecrirewfn2+"\n")
                #print(tensor[i])
                if len(str(i+1))>maxi[0]:maxi[0]=len(str(i+1))
                #print "TESTS",len(decomp2),len(ener)
                #print "TESTS",ener[i]
                if len(' '+'%5.1f' %ener[i]+' ')>maxi[1]:maxi[1]=len(' '+'%4.1f' %ener[i]+' ')
                if len(' '+'%4.1f' %tensor[i][0]+' ')>maxi[2]:maxi[2]=len(' '+'%4.1f' %tensor[i][0]+' ')
                if len(' '+'%4.1f' %tensor[i][1]+' ')>maxi[3]:maxi[3]=len(' '+'%4.1f' %tensor[i][1]+' ')
                if len(' '+'%4.1f' %tensor[i][2]+' ')>maxi[4]:maxi[4]=len(' '+'%4.1f' %tensor[i][2]+' ')
                ecrire.append([str(i+1),' '+'%5.1f' %ener[i]+' ',' '+'%4.1f' %tensor[i][0]+' ',' '+'%4.1f' %tensor[i][1]+' ',' '+'%4.1f' %tensor[i][2]+' ',' '+ecrirewfn2[:-2]])
        for i in range(0,len(ecrire)):
                for j in range(0,len(ecrire[i])-1):
                        if j<5:
                                if len(ecrire[i][j])<maxi[j]:
                                        for k in range(len(ecrire[i][j]),int(maxi[j])):
                                                ecrire[i][j]=ecrire[i][j]+" "
#                        ecriture.write(ecrire[i][j]+"|")
#                ecriture.write(ecrire[i][-1])
#                ecriture.write("\n")
        return(ecrire)

def mult(ndoublets,fichier):
#        print("debut mmult")
        mult=np.zeros(ndoublets)
        mult2=np.zeros(ndoublets)
        for i in range(0,len(mult)):
                mult[i]=1
                mult2[i]=1
        f=os.popen("grep 'CALCULATION OF PSEUDOSPIN HAMILTONIAN TENSORS FOR THE MULTIPLET' "+fichier).readlines()
#        print(len(mult))
        pos=0
        for i in range(0,len(f)):
                multi=0
                #print f[i]
                if "/" in str.split(f[i])[-1]:
                        
                        multi=2.0*(float(str.split(f[i])[-1][0])/float(str.split(f[i])[-1][-2]))+1
                else:
                        multi=2*int(str.split(f[i])[-1][-2])+1
                mult[int(str.split(f[i])[8])-1]=multi
                
        #print "mult",mult
        pos=0
        multiplet=1
        for i in range(0,len(mult)):
                for j in range(0,int(mult[i])):
                        if pos<len(mult2):
                                
                                mult2[pos]=multiplet
                        pos=pos+1
                multiplet=multiplet+1
        #print "mult2",mult2
        return(mult2)


def ecriture_nonkramer(decomp,tensor,ener,thre,kram,multiplet):
        #ecriture=open("extract.txt",'wb')
        ecrire=[]
        ecrire.append(["multiplet "," E(cm-1) ","   gx   ","   gy   ","   gz   "," WFT"])
        wfnout=[]
        #decomp=sorted(decomp,reverse=True)
        #print(len(decomp)*2,kram)
        decomp2=[]
        STATE=[]
        if kram=='y':
                for i in range(len(decomp)*2-1,0,-2):
                        #print str(i)+'/2'
                        STATE.append(str(i)+'/2')
        else:
                #print(decomp,len(decomp))
                for i in range(int((len(decomp)-1)/2),-1,-1):
                        #print str(i)
                        STATE.append(str(i))
        #print STATE
        for i in range(0,len(decomp)):
                wfnout2=""
                decomp3=[]
                #print decomp[i]
                for j in range(0,len(STATE)):
                        #print "TESTS",len(decomp[i])
                        decomp3.append([STATE[j],decomp[i][j]])
                decomp3=sorted(decomp3,key=itemgetter(1),reverse=True)
                decomp2.append(decomp3)
#       print "TESTS"
        ecrirewfn=[]
#        pm='\xc2\xb1'
        pm=chr(177)
        maxi=np.zeros(5)
        for i in range(0,len(ecrire[0])-1):
                maxi[i]=len(ecrire[0][i])
        #print "len decomp2",len(decomp2)
        for i in range(0,len(decomp2)):
                ecrirewfn2=''
                for j in range(0,len(STATE)):
                        if decomp2[i][j][1]>thre:ecrirewfn2=ecrirewfn2+'%4.1f' %decomp2[i][j][1]+' '+pm+' '+decomp2[i][j][0]+'> + '
                #print ecrirewfn2[:-2]
                ecrirewfn.append(ecrirewfn2)
                #print i,ecrirewfn2[:-2]
                #ecriture.write(ecrirewfn2+"\n")
                #print(tensor[i])
                if len(str(i+1))>maxi[0]:maxi[0]=len(str(i+1))
                #print "TESTS",len(decomp2),len(ener)
                #print "TESTS",ener[i]
                if len(' '+'%5.1f' %ener[i]+' ')>maxi[1]:maxi[1]=len(' '+'%4.1f' %ener[i]+' ')
                if len(' '+'%4.1f' %tensor[i][0]+' ')>maxi[2]:maxi[2]=len(' '+'%4.1f' %tensor[i][0]+' ')
                if len(' '+'%4.1f' %tensor[i][1]+' ')>maxi[3]:maxi[3]=len(' '+'%4.1f' %tensor[i][1]+' ')
                if len(' '+'%4.1f' %tensor[i][2]+' ')>maxi[4]:maxi[4]=len(' '+'%4.1f' %tensor[i][2]+' ')
                ecrire.append([str(int(multiplet[i])),' '+'%5.1f' %ener[i]+' ',' '+'%4.1f' %tensor[i][0]+' ',' '+'%4.1f' %tensor[i][1]+' ',' '+'%4.1f' %tensor[i][2]+' ',' '+ecrirewfn2[:-2]])
        longmax=0
#       for i in range(0,len(ecrire)):
#               longu=0
#               for j in range(0,len(ecrire[i])):
#                       longu=longu+len(ecrire[i][j])
#               if longu+5>longmax:longmax=longu+5

        for i in range(0,len(ecrire)):
                for j in range(0,len(ecrire[i])-1):
                        if j<5:
                                if len(ecrire[i][j])<maxi[j]:
                                        for k in range(len(ecrire[i][j]),int(maxi[j])):
                                                ecrire[i][j]=ecrire[i][j]+" "
        for i in range(0,len(ecrire)):
                longu=0
                for j in range(0,len(ecrire[i])):
                        longu=longu+len(ecrire[i][j])
                if longu+5>longmax:longmax=longu+5
#        for i in range(0,len(ecrire)):
#                if i>1:
                        #print multiplet[i-1],multiplet[i-2]
#                        if multiplet[i-1]>multiplet[i-2]:
#                                for j in range(0,longmax):
#                                        ecriture.write("-")
#                                ecriture.write("\n")
#                for j in range(0,len(ecrire[i])-1):
 #                       ecriture.write(ecrire[i][j]+"|")
 #               ecriture.write(ecrire[i][-1])
 #               ecriture.write("\n")
        return(ecrire)

def main_extract(fichier,thre):        
	#print "Name of the output file"
	fichier=raw_input("")
	ndoublets2=ndoublet(fichier)
	kramer="y"
	if ndoublets2%2==1:
	        kramer="n"
	 #       print "NON KRAMER"
	#else:
	#        print "KRAMER"
	ndoublets=int(ndoublets2/2)+ndoublets2%2
	#print ndoublets," found"
	if kramer=="n":
	        mult=mult(ndoublets2)
	if kramer=="y":
	        ener=energies(fichier,kramer,ndoublets)
	else:
	        ener=energies_nonkramer(fichier,kramer,2*(ndoublets-1)+1)
	if kramer=="y":
	        tensor=np.zeros((ndoublets,3))
	        tensor=extract_tensor(tensor,fichier)
	else:
	        #tensor2=np.zeros((ndoublets,3))
	        tensor2=np.zeros((len(mult),3))
	        tensor=np.zeros((2*(ndoublets-1)+1,3))
	        tensor=extract_tensor_nonkramer(tensor2,fichier,mult,tensor)
	if kramer=="y":
	        wfn=np.zeros((2*ndoublets,2*ndoublets,2))
	        wfn=extract_wfn(wfn,fichier)
	        decomp=np.zeros((ndoublets,ndoublets))
	        decomp=extract_decomp(wfn,decomp)
	if kramer=="n":
	        wfn=np.zeros((2*(ndoublets-1)+1,2*(ndoublets-1)+1,2))
	        wfn=extract_wfn_nonkramer(wfn,fichier)
	#       for i in range(0,len(wfn)):
	#               print i+1,wfn[i]
	#       decomp=np.zeros((ndoublets,ndoublets))
	        decomp=np.zeros((2*(ndoublets-1)+1,2*(ndoublets-1)+1))
	        decomp=extract_decomp_nonkramer(wfn,decomp)
	#print "len decomp",len(decomp)
	#print "THRESHOLD of WFN output (%)"
	thre=float(raw_input(""))
	if kramer=="y":
	        ecriture(decomp,tensor,ener,thre,kramer)
	else:
	        ecriture_nonkramer(decomp,tensor,ener,thre,kramer,mult)
