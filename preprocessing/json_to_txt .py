from glob import glob
import json

path = './TrainDataset/json/'
asd = ['shapes','imagePath','imageHeight','imageWidth']
#['points','group_id'

for pa in glob(path+'*.json'):
	json_data = open(pa).read()
	data = json.loads(json_data)
	xy = []
	wh = []
	pathimg = ''
	height = 0
	width = 0
	group_id = []
	for k ,v in data.items():
		if k ==asd[1]:
			pathimg = data[k]
			
		if k ==asd[2]:
			height = int(data[k])
			
		if k ==asd[3]:
			width = int(data[k])
		if k ==asd[0]:
			for i in data[k]:
				print(i['group_id'],i['points'],'\n')
				group_id.append(i['group_id'])
				max1 = max(i['points'][0][0],i['points'][2][0])
				max2 = max(i['points'][0][1],i['points'][2][1])
				min1 = min(i['points'][0][0],i['points'][2][0])
				min2 = min(i['points'][0][1],i['points'][2][1])
				x = min1 + int((max1-min1)/2)
				y = min2 + int((max2-min2)/2)
				
				max1 = max(i['points'][1][0],i['points'][0][0])
				max2 = max(i['points'][3][1],i['points'][0][1])
				min1 = min(i['points'][1][0],i['points'][0][0])
				min2 = min(i['points'][3][1],i['points'][0][1])
				w = max1-min1
				h = max2-min2
				xy.append((x,y))
				wh.append((w,h))
	f1 =open('./TWStreet/labels/'+pathimg+'.txt','w')
	for z,x,c in zip(group_id,xy,wh):
		if z == 255:
			# ~ print('z = ',z)
			continue
		if z==None:
			# ~ print('z = ',z)
			continue
		print(pathimg,z,x,width)
		print('x = ',round(x[0]/width,3),'y = ',round(x[1]/height,3))
		print('w = ',round(c[0]/width,3),'h = ',round(c[1]/height,3))
		xc = round(x[0]/width,3)
		w = round(c[0]/width,3)
		yc = round(x[1]/height,3)
		h = round(c[1]/height,3)
		xmax = (2*xc*width + w*width)/2
		xmin = (2*xc*width - w*width)/2
		ymax = (2*yc*height + h*height)/2
		ymin = (2*yc*height - h*height)/2
		# (min, min) (max, min) (max, max) (min, max)
		print('(%f, %f) (%f, %f) (%f, %f) (%f, %f)'%(xmin,ymin,xmax,ymin,xmax,ymax,xmin,ymax))
		## ~ f1.write(str(z)+' ')
		f1.write(str(0)+' ')
		f1.write(str(round(x[0]/width,3))+' ')
		f1.write(str(round(x[1]/height,3))+' ')
		f1.write(str(round(c[0]/width,3))+' ')
		f1.write(str(round(c[1]/height,3))+' ')
		f1.write('\n')
	
	f1.close()
	
	


