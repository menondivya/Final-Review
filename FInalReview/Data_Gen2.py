import csv 
import random
from time import time
import datetime
import time
fieldnames = ["xvalue", "Building1Flame", "Building2Flame", "Building3Flame", "Building4Flame", "Building5Flame"]


with open('Example7.csv', 'w') as csv_file:
	csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	csv_writer.writeheader()

while True:

	with open('Example7.csv', 'a') as csv_file:
		csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames )
		#x_value = time.strftime("%H:%M")
		#x = datetime.datetime.now()
		#xvalue = x.strftime("%X")	
		#xvalue = time.time()	
		xvalue = int(round(time.time()))		
		Building1Flame = random.randint(0,1)
		Building2Flame = random.randint(0,1)
		Building3Flame = random.randint(0,1)
		Building4Flame = random.randint(0,1)
		Building5Flame = random.randint(0,1)
		info = {
		"xvalue": xvalue,
		"Building1Flame": Building1Flame,
		"Building2Flame": Building2Flame,
		"Building3Flame": Building3Flame,
		"Building4Flame": Building4Flame,
		"Building5Flame": Building5Flame
		}

		csv_writer.writerow(info)
		print(xvalue, Building1Flame, Building2Flame, Building3Flame, Building4Flame, Building5Flame)
	
	time.sleep(1)
