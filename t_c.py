from datetime import datetime
now = datetime.now()
print ("Hi,please tell me your name: ")
name = input()
print ("Hi, %s do you accepet our terms and conditions. If yes please type Y else type N: " % name)
responce = input()
responce = responce.lower()

if responce == 'y' or responce == 'yes':
  print ("I %s, declare that I will honor the new rules"% name) 
  print (name)
  print ("%02d/%02d/%04d" % (now.day, now.month, now.year))

elif responce == 'n' or responce == 'no':
  print ("I %s, declare that I do not accepet these new rules" % name) 
  print (name)
  print ("%02d/%02d/%04d" % (now.day, now.month, now.year))
  
else:
  print ("You are just joking right?")  