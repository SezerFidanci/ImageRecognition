from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
import functools 
from collections import Counter
import glob

def createExamples():
    print('Learning...')
    numberArrayExamples = open('iconArEx.txt','a')
    allFiles = glob.glob("images/imgfolder/*.png")
    for x in range(0,99):
        imgFilePath =allFiles[x]
        fileName= allFiles[x].replace('.png','')
        fileName= fileName.replace('images/imgfolder/','')
        print('>> '+fileName)
        ei = Image.open(imgFilePath)
        eiar = np.array(ei)
        eiar1 = str(eiar.tolist())
        lineToWrite = fileName+'::'+eiar1+'\n'
        numberArrayExamples.write(lineToWrite)
    print('Learning is done!')
           

            
            
def whatIcons(filePath):
    matchedAr = []
    loadExamps = open('iconArEx.txt','r').read()
    loadExamps = loadExamps.split('\n')
    
    i = Image.open(filePath)
    iar = np.array(i)
    iar1 = iar.tolist()
    
    inQuestion = str(iar1)    
    
    for eachExample in loadExamps:
        if len(eachExample) > 3:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]
            
            eachPixEx = currentAr.split('],')
            
            eachPixInQ = inQuestion.split('],')
            x=0
            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(currentNum)
                x+=1
                
    
    x= Counter(matchedAr)
    print (x)
    print('\n\nMost Like: '+str(x.most_common(1)))


#createExamples() # First run for icon set learning. This functions create will iconArEx.txt file.
#whatIcons('images/book1.png') # Second run for test. Dont forget close createExamples functions .
