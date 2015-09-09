import sys
import time

toFind = ['ERROR', 'Exception', 'deadlock']
#use sys.path

def follow(file):
	file.seek(0, 2)
	while True:
		line = file.readline()
		if not line:
			time.sleep(0.1)
			continue
		yield line

i = input("Choose file to follow: ")

logfile = open(i)
logline = follow(logfile)


for line in logline:
	print (line, logline)
	for find in toFind:
		if find in line:
			print("%s found in %s file" % (find, i))