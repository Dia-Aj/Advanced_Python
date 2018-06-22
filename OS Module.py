import os

""" Print the current working directory -- os.getcwd() """
print(os.getcwd())

""" To navigate into anohter directory -- os.chdir('Path') """
os.chdir('F:\Python')
print(os.getcwd())

""" Print all the files and folders inside a directory """
dirs = os.listdir()
print(*dirs, sep="\t")

""" To make/remove directories and list them. """

#os.makedirs('MyTestDirctory')
dirs = os.listdir()
for d in dirs:
	if(d == 'MyTestDirctory'): print(f'Found it! {d}')

#os.rmdir('MyTestDirctory')

""" To rename files -- os.rename('Original file name', 'new name') """
#os.rename('MyTestDirctory', 'MyTestDirctoryRenamed')

""" to print a directory stats """
print()
print(os.stat('learning_logs'))

