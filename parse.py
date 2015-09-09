import sys
import time

#use sys.path

#class LogParser:

def follow(file):
	file.seek(0, 2)
	while True:
		line = file.readline()
		if not line:
			time.sleep(0.1)
			continue
		yield line

def find(logline, words, openfile):
	for line in logline:
		for find in words:
			if find in line:
				print("%s found in %s file" % (find, openfile))

if __name__ == '__main__':
	words = ['ERROR', 'Exception', 'deadlock']
	openfile = input("Choose file to follow: ")
	logfile = open(openfile)
	logline = follow(logfile)
	find(logline, words, openfile)