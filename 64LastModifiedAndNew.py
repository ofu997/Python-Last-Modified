import os
import datetime
import shutil

print ( "~ This tool copies all files modified or created within 24 hours")
print( " from a source folder to a destination folder ~")

srcRaw = input("~ What is your source folder? ~  ")

src = srcRaw.replace('\\','//')

dstRaw = input("~ What is your destination folder? ~  \n")

dst = dstRaw.replace('\\','//')


# If srcRaw and dstRaw are not in C:\xx\xx format:
#for HARD-CODING USE: src = "C:\\Users\\Oliver\\Desktop\\folder_A"
# FOR HARD-CODING USE: dst = "C:\\Users\\Oliver\\Desktop\\folder_B"

src="C://Users//Oliver//Desktop//folder_A//"
dst="C://Users//Oliver//Desktop//folder_B//"

myfiles = os.listdir(src)

def Copier(src,dst):
  now = datetime.datetime.now()
  for file in myfiles:
    osFunction = os.path.getmtime(src+file)
    ageInSeconds = datetime.datetime.fromtimestamp(osFunction)
    difference = now - ageInSeconds
    differenceSec = difference.total_seconds()
    if differenceSec > (24*60*60):
      print( file + " is older than 24 hours.\n" )
    else:
      shutil.copy( src+file , dst )
      print( "The document " + file + " has been copied to " + dst + "  !~*\n") 

Copier(src,dst)





