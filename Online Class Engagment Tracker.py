import csv
import os

engagement_tracker = {}

#makes CSV that converts dictionary to result
def makeCSV():
	with open ('engagement.csv', 'w') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(["Name", "Comments", "Comment Count"])
		for key in engagement_tracker:
			engagement_tracker[key].insert(0,len(engagement_tracker[key]))
			engagement_tracker[key].insert(0, key)
			writer.writerow(engagement_tracker[key])

# takes current working directory and parses through it
def directoryIterator():
	directory = os.getcwd()
	transcripts = os.listdir(directory)
	for file in transcripts:
		file_name, file_extension = os.path.splitext(file)
		if(file_extension == ".vtt"):
			parse (file)
		

def parse (fileName):
	linesList = []
	dates = []
	phrases = []
	# [Training File for testing purposes] fileName = "GMT20201020-143340_2020FA_POL.transcript copy.vtt"
	#opens the textfile with purpose of reading text data and immediately closes textfile after creating a list of lines 
	with open (fileName, 'rt') as currentFile:
		#for loops iterate on each item in a sequence, and a line is an unit of data in a text file
		for currentLine in currentFile: 
			linesList.append(currentLine)

	#cleans up lines array by removing blankspaces and newlines, removes first element from each list 
	linesList = list(filter(lambda x: x not in ['', '\n'], linesList))

	#creates a speech array and date array
	for x in range(2, len(linesList) - 1, 3):
		dates.append(linesList[x])
		phrases.append(linesList[x+1])

	#creates entry in excel if the speaker is not chloe thurston
	for x in range(len(phrases)):
		if "Chloe Thurston" not in phrases[x]:
			studentPhrase = phrases[x].split()
			if len(studentPhrase) > 5 and ':' in studentPhrase[1]:
				lastName = studentPhrase[1].replace(':','')
				#sorry this is a really terrible piece of code, but I don't know how to make it more efficient, so here's what it does. 
				#setdefault checks if the dictionary has the person's full name, if it does, it returns the value, if it doesn't, it creates the name as
				# a key and returns an empty list as the value. From there, I append the rest of the spliced phrase string (minus the name) and add the time & date
				engagement_tracker.setdefault(studentPhrase[0] + " " + lastName, []).append(fileName[7:9] + "/" +fileName[9:11] + ": " + " ".join(studentPhrase[2:]))

directoryIterator()
makeCSV()
