import os
print(os.getcwd())
#os.makedirs('test')
os.chdir("F:\Python\Tutorials\\test")
print(os.getcwd())
all_files = os.listdir()

for file in all_files:
	name, ext = file.split(".")
	name = name.replace('testFile', 'File-')
	ext = ext.replace('txt', 'html')
	fileNew = '{0}.{1}'.format(name, ext)
	os.rename(file, fileNew)