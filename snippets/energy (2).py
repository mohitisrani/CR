import os

lines = open('xdataB2S3').read()
with open('xdataB2S3','w') as file:
    file.write( 'Name             2D_atoms  3D_atoms  ORatoms      2D_Energy          3D_Energy        Energy_OR            EF(meV)         EFOR   \n')

energy2= '    I   '
energy3= '    I   '
energy4= '    I   '
energy5= '    I   '

for comp in os.listdir('B2S3'):
     
    if os.path.isdir('B2S3/'+comp):
        x=0
        lines2 = open('B2S3/'+comp+'/POSCAR').readlines()
        atoms2 = lines2[6].split()

        atoms2 = int(atoms2[0]) +int(atoms2[1])
        elines2 = open('B2S3/'+comp+'/OUTCAR').readlines()
        for eline2 in elines2:
            el2=eline2.strip()
            if el2.startswith("free  energy   TOTEN"):
                e2 = el2.split()
                energy2 = float(e2[4])
            if  el2.startswith("reached required accuracy"):
                x=1
#        if x==0:
# if you want to calculate energy based on present iterated energy value instead of required accuracy, #tag below and line
#           energy2='     I   '
        y=0
        lines3 = open('B2S3_bulk/'+comp+'/POSCAR').readlines()
        atoms3 = lines3[6].split()
        atoms3 = int(atoms3[0]) +int(atoms3[1])
        elines3 = open('B2S3_bulk/'+comp+'/OUTCAR').readlines()
        for eline3 in elines3:
            el3=eline3.strip()
            if el3.startswith("free  energy   TOTEN"):
                e3 = el3.split()
                energy3 = float(e3[4])
            if el3.startswith("reached required accuracy"):
                y=1
        if y==0:
# if you want to calculate energy based on present iterated energy value instead of required accuracy, #tag below and above line
             energy3 = '    I   '

#OnRatio Start
	try:
		z=0
		lines4 = open('onRatio/'+comp+'/POSCAR').readlines()
		atoms4 = lines4[6].split()
   #             print atoms4
                atoms4.extend((0,0,0,0,0))
    #            print atoms4
		atoms4 = int(atoms4[0]) +int(atoms4[1])+int(atoms4[2]) +int(atoms4[4])+int(atoms4[3]) +int(atoms4[5])
		elines4 = open('onRatio/'+comp+'/OUTCAR').readlines()
		for eline4 in elines4:
		    el4=eline4.strip()
		    if el4.startswith("free  energy   TOTEN"):
			e4 = el4.split()
			energy4 = float(e4[4])
		    if el4.startswith("reached required accuracy"):
			z=1
		if z==0:
	# if you want to calculate energy based on present iterated energy value instead of required accuracy, #tag below and above line
                    energy4 = '    I   '
        except:
            energy4=           '    D   '
#OnRatio End


        try:
            energy = str((energy2/atoms2 - energy3/atoms3)*1000)
        except: energy = "   -"

        try:
            energyOR = str((energy2/atoms2- energy4/atoms4)*1000)
        except:
           
            try:
                energy41=energy4.strip()
                if energy41=='D':
                    energyOR="    D"
                    atoms4="-"
            except:
                energyOR="    -"
            
        mid0=comp[:]+'            '
        mid= mid0[:15] +'     '+ (str(atoms2)+'     ')[:5]+'     '+ (str(atoms3)+'     ')[:5]+'   '+(str(atoms4)+'    ')[:5]+'     ' + (str(energy2)+'         ')[:16]+'     '+(str(energy3)+'         ')[:16]+(str(energy4)+'            ')[:16]+'     '+(str(energy)+'                    ')[:16]+str(energyOR)
                
                
        lines = open('xdataB2S3').read()
        with open('xdataB2S3','w') as file:
            file.write(lines)
            file.write(mid+'\n')



lines = open('xdataB2S3').read()
with open('xdataB2S3','w') as file:
    file.write(lines+'\n   Hull_energies\n')


for comp in os.listdir('hull'):

    if os.path.isdir('hull/'+comp):
        x=0
        lines5 = open('hull/'+comp+'/POSCAR').readlines()
        atoms5 = lines5[6].split()
        
        atoms5.append(0)
       
        atoms5 = int(atoms5[0]) +int(atoms5[1])
        elines5 = open('hull/'+comp+'/OUTCAR').readlines()
        for eline5 in elines5:
            el5=eline5.strip()
            if el5.startswith("free  energy   TOTEN"):
                e5 = el5.split()
                energy5 = float(e5[4])
            if  el5.startswith("reached required accuracy"):
                x=1
        if x==0:
# if you want to calculate energy based on present iterated energy value instead of required accuracy, #tag below and line
            energy5='     I   '


        mid0=comp[:]+'               '
        mid= mid0[:12] +'     '+ (str(atoms5)+'        ')[:5]+'    '+(str(energy5)+'                 ')[:14]
        lines = open('xdataB2S3').read()
        with open('xdataB2S3','w') as file:
            file.write(lines)
            file.write(mid+'\n')


lines= open('xdataB2S3').readlines()
with open('xdataB2S3','w') as file:
    
    for line in lines:
        file.write(line)	
	if line.startswith('In2Te3'):
	    line1=line.split()           
	    aIn0=float(line1[1])
            try:
	        In0=float(line1[4])
            except:
                In0=line1[4]
                
	if line.startswith('B2Te3'):
	    line1=line.split()
	    B2Te30=float(line1[4])
	    aB2Te30=float(line1[1])
	     
	if line.startswith('B2Se3'):
	    line1=line.split()
	    B2Se30=float(line1[4])
	    aB2Se30=float(line1[1])

	if line.startswith('In7Te'):
	    line1=line.split()
	    In1=float(line1[2])*4/15
	    aIn1=float(line1[1])*4/15
	    
	if line.startswith('In2Te5'):
	    line1=line.split()
	    In2=float(line1[2])*1/15
	    aIn2=float(line1[1])*1/15

	if line.startswith('B '):
	    line1=line.split()
	    B1=float(line1[2])/float(line1[1])*2/5

	if line.startswith('Te  '):
	    line1=line.split()
	    Te1=float(line1[2])/float(line1[1])*3/5

	if line.startswith('Se  '):
	    line1=line.split()
	    Se1=float(line1[2])/float(line1[1])*3/5
    


    try:
	B2Te3E=((B2Te30/aB2Te30)-(B1+Te1))*1000
    except:
	B2Te3E= "   -"
    file.write('\nB2Te3       '[:10]+str(B2Te3E))

    try:
	InE=((In0/aIn0)-(In1+In2)/(aIn1+aIn2))*1000
    except:
	InE= "   -"
    file.write('\nIn2Te3       '[:10]+str(InE))

    try :
        B2Se3E=((B2Se30/aB2Se30)-(B1+Se1))*1000
    except:
        B2Se3E= "   -"
    file.write('\nB2Se3       '[:10]+str(B2Se3E)+'\n')








 
