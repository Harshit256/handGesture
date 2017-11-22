from PIL import Image
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import style
import cv2
style.use('ggplot')



def createExams():
	numbers=range(1,1330)
	numberArrayExamples = open('AKnumArEx.txt','a')
	for i in numbers:
		imgfilepath='Marcel-Train/A/A-train'+str('{0:04}'.format(i))+'.ppm'
		img = cv2.imread(imgfilepath, 1)
		eia=cv2.resize(img,(64,64))

		hsv = cv2.cvtColor(eia, cv2.COLOR_BGR2HSV)
		lower_range = np.array([4,100,100])
		upper_range = np.array([18,255,255])
		mask = cv2.inRange(hsv, lower_range, upper_range)
		eiarl=str(mask.tolist())
		lineToWrite = 'A::'+eiarl+'\n'
		numberArrayExamples.write(lineToWrite)
		
		


	numbers=range(1,488)
	numberArrayExamples = open('AKnumArEx.txt','a')
	for i in numbers:
		imgfilepath='Marcel-Train/B/B-train'+str('{0:03}'.format(i))+'.ppm'
		img = cv2.imread(imgfilepath, 1)
		eia=cv2.resize(img,(64,64))

		hsv = cv2.cvtColor(eia, cv2.COLOR_BGR2HSV)
		lower_range = np.array([4,100,100])
		upper_range = np.array([18,255,255])
		mask = cv2.inRange(hsv, lower_range, upper_range)
		eiarl=str(mask.tolist())

		lineToWrite = 'B::'+eiarl+'\n'
		numberArrayExamples.write(lineToWrite)


	numbers=range(1,573)
	numberArrayExamples = open('AKnumArEx.txt','a')
	for i in numbers:
		imgfilepath='Marcel-Train/C/C-train'+str('{0:03}'.format(i))+'.ppm'
		img = cv2.imread(imgfilepath, 1)
		eia=cv2.resize(img,(64,64))

		hsv = cv2.cvtColor(eia, cv2.COLOR_BGR2HSV)
		lower_range = np.array([4,100,100])
		upper_range = np.array([18,255,255])
		mask = cv2.inRange(hsv, lower_range, upper_range)
		eiarl=str(mask.tolist())

		lineToWrite = 'C::'+eiarl+'\n'
		numberArrayExamples.write(lineToWrite)


	numbers=range(1,655)
	numberArrayExamples = open('AKnumArEx.txt','a')
	for i in numbers:
		imgfilepath='Marcel-Train/Five/Five-train'+str('{0:03}'.format(i))+'.ppm'
		img = cv2.imread(imgfilepath, 1)
		eia=cv2.resize(img,(64,64))

		hsv = cv2.cvtColor(eia, cv2.COLOR_BGR2HSV)
		lower_range = np.array([4,100,100])
		upper_range = np.array([18,255,255])
		mask = cv2.inRange(hsv, lower_range, upper_range)
		eiarl=str(mask.tolist())

		lineToWrite = 'F::'+eiarl+'\n'
		numberArrayExamples.write(lineToWrite)


	numbers=range(1,1396)
	numberArrayExamples = open('AKnumArEx.txt','a')
	for i in numbers:
		imgfilepath='Marcel-Train/Point/Point-train'+str('{0:04}'.format(i))+'.ppm'
		img = cv2.imread(imgfilepath, 1)
		eia=cv2.resize(img,(64,64))
E
		hsv = cv2.cvtColor(eia, cv2.COLOR_BGR2HSV)
		lower_range = np.array([4,100,100])
		upper_range = np.array([18,255,255])
		mask = cv2.inRange(hsv, lower_range, upper_range)
		eiarl=str(mask.tolist())

		lineToWrite = 'P::'+eiarl+'\n'
		numberArrayExamples.write(lineToWrite)


	numbers=range(1,436)
	numberArrayExamples = open('AKnumArEx.txt','a')
	for i in numbers:
		imgfilepath='Marcel-Train/V/V-train'+str('{0:03}'.format(i))+'.ppm'
		img = cv2.imread(imgfilepath, 1)
		eia=cv2.resize(img,(64,64))

		hsv = cv2.cvtColor(eia, cv2.COLOR_BGR2HSV)
		lower_range = np.array([4,100,100])
		upper_range = np.array([18,255,255])
		mask = cv2.inRange(hsv, lower_range, upper_range)
		eiarl=str(mask.tolist())

		lineToWrite = 'V::'+eiarl+'\n'
		numberArrayExamples.write(lineToWrite)

#createExams()

def WhatGesIsThis(filepath):
	
	matchedAr=[]
	loadExamps=open('AKnumArEx.txt','r').read()
	loadExamps = loadExamps.split('\n')
	img = cv2.imread(filepath, 1)
	eia=cv2.resize(img,(64,64))

	hsv = cv2.cvtColor(eia, cv2.COLOR_BGR2HSV)
	lower_range = np.array([4,100,100])
	upper_range = np.array([18,255,255])
	mask = cv2.inRange(hsv, lower_range, upper_range)
	iarl=mask.tolist()

	inQuestion = str(iarl)
	for eachExample in loadExamps:
		if len(eachExample)>3:
			splitEx = eachExample.split('::')
			currentNum = splitEx[0]
			currentAr = splitEx[1]
			eachPixEx = currentAr.split(',')
			eachPixInQ = inQuestion.split(',')
	
			

	
			x = 0
			while x < len(eachPixEx):
				if eachPixEx[x] == eachPixInQ[x] and eachPixInQ[x]==255:
					matchedAr.append(str(currentNum))
				x+=1

	x = Counter(matchedAr)
	#print(x)
	for i in x:
		key=x[i]
		if i=='A':
			x[i]=x[i]/5443584
		elif i=='B':
			x[i]=x[i]/1994752
		elif i=='C':
			x[i]=x[i]/2342912
		elif i=='F':
			x[i]=x[i]/2678784
		elif i=='P':
			x[i]=x[i]/5713920
		elif i=='V':
			x[i]=x[i]/1781760

	#print(x)




#WhatGesIsThis('cross_validation_data/32.ppm')
	return x
	# graphX = []
	# graphY = []

	# ylimi = 0

	# for eachThing in x:
	# 	graphX.append(eachThing)
	# 	graphY.append(x[eachThing])
	    


	# fig = plt.figure()
	# ax1 = plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4)
	# ax2 = plt.subplot2grid((4,4),(1,0), rowspan=3,colspan=4)

	# ax1.imshow(iar)
	# ax2.bar(graphX,graphY,align='center')
	# plt.ylim(25000)

	# #maximum value to be shown on x-axis
	# xloc = plt.MaxNLocator(5)

	# ax2.xaxis.set_major_locator(xloc)

	# plt.show()


 results=range(1,225)
cross=open('vali.csv','a')
diction={}
for i in results:
	estFilePath='test_data/'+str(i)+'.ppm'
	diction=WhatGesIsThis('cross_validation_data/32.ppm')
	maxi=max(diction,key=diction.get)
	lineToWrite=str(i)+'.ppm,'+maxi+'\n'
	cross.write(lineToWrite)



