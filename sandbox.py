import os
directory = os.getcwd()
transcripts = os.listdir(directory)
for file in transcripts:
	file_name, file_extension = os.path.splitext(file)
	print(file_name)
	print(file_extension)
	print(file)