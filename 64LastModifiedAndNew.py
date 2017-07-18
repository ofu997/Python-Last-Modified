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
#print(myfiles)
#print("age of python file: ")
#print(datetime.datetime.fromtimestamp(os.path.getmtime("python63filemoving.py")))
#print("age of txt file: ")
#print(datetime.datetime.fromtimestamp(os.path.getmtime(src+"1.txt")))

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


'''
#research
#https://stackoverflow.com/questions/12131766/python-date-time-comparison-using-timestamps-timedelta

# SAVE THIS
now = datetime.datetime.now()
print(now)
filename=input("write name of file")
#osFunction=os.path.getmtime(filename)
then = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
tdelta = now - then
print(tdelta)
seconds = tdelta.total_seconds()
# can't get total_hours, why?
print(seconds)

if seconds > (60*60*24):
  print("old")
else:
  print("newer")
'''
'''

'''
'''
now = datetime.datetime.now()
print(now)
filename=input("write name of python file: ")

## if recently created, it must have been
## recently modified as well, so using getmtime()

osFunction=os.path.getmtime(filename)
then = datetime.datetime.fromtimestamp(osFunction)
tdelta = now - then
print(tdelta)
seconds = tdelta.total_seconds()
# can't get total_hours, why?
print(seconds)

if seconds > (60*60*24):
  print("old")
else:
  print("newer")

'''

'''
f = os.path.getctime("64LastModifiedAndNew.py")
f2=datetime.datetime.fromtimestamp(f)
print(f2)
print(type(f2))
# disc f3=datetime.strptime(f2, "%Y-%m-%d")
'''
'''
print(f3)
print(type(f3))
'''
'''

g = os.path.getctime("vampire.py")
g2=datetime.datetime.fromtimestamp(g)
print(g2)
print(type(g2))

now=datetime.datetime.today()
print(now)
print(type(now))

d1=now-g2
print("d1: ")
print(d1)
print(type(d1))

if d1.total_hours > timedelta(hours=24):
  print("old")
else:
  print("new")
  
# dif1=d1.total_hours()

# print(d1)
'''



