#edit the job name in 2D and 3D materials
import os


for direct in os.listdir('.'):
    
    if os.path.isdir(direct):
        
        for comp in os.listdir(direct):
            if os.path.isdir(direct+'/'+comp):
                lines = open(direct+'/'+comp+'/submit').readlines()
                with open(direct+'/'+comp+'/submit','w') as file:
                    for line in lines:
                        if line.startswith("#PBS -N"):
                            file.write("#PBS -N 2D"+direct+comp[2:]+"\n")
                        else:
                            file.write(line)
                    


