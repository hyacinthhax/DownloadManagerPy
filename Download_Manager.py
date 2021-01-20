#Download Manager
import os
import shutil
import schedule
import time

src = '/home/user/Downloads/'
dest = '/home/user/'
posvid = ['.mp4', '.mov', '.avi', '.flv', '.mkv', '.wmv', '.webm'] 
zipz = ['.zip', '.tar', '.bz2', '.gz']
teext = ['.txt', '.md', '.asc', '.pdf']
inst = ['.iso', '.deb']
slef = '/Desktop/Testing/Projects/DownloadManager/'

with open('specified.txt', 'r') as specif:
			text = specif.readlines()
			print(text)
			global text

def run():
	os.chdir(src)
	for file in os.listdir(src):
		file_name, file_ext = os.path.splitext(file)
		print(file_ext)
		if str(file) in str(text):
			mark = 'Documents/Specified/'
			full_dest = os.path.join(dest, mark, file)
			print(full_dest)
			print('\n')
			shutil.move(file,full_dest)
		elif str(file_ext) in zipz:
			zeep = 'Documents/Zips/'
			full_dest = os.path.join(dest, zeep, file)
			print(full_dest)
			print('\n')
			shutil.move(file,full_dest)
		elif str(file_ext) in teext:
			text1 = 'Documents/Text/'
			full_dest = os.path.join(dest, text1, file)
			print(full_dest)
			print('\n')
			shutil.move(file,full_dest)
		elif str(file_ext) in inst:
			instf = 'Documents/Installers/'
			full_dest = os.path.join(dest, instf, file)
			print(full_dest)
			print('\n')
			shutil.move(file,full_dest)
		elif str(file_ext) in posvid:
			veed = 'Videos/'
			full_dest = os.path.join(dest, veed, file)
			print(full_dest)
			print('\n')
			shutil.move(file,full_dest)

run()
schedule.every().hour.do(run)

while True:
    schedule.run_pending()
    time.sleep(1)