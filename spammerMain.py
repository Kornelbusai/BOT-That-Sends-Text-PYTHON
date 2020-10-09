#This bot was made for spamming people with texting applications(IT IS NOT 
# ENCOURAGED OR RECOMMANDED TO BE USED IN MALICES WAYS) 

import pyautogui, time
#Gives time for the user to click on where they want to print the text
time.sleep(5)
#make sure to change your file directory for your specific needs
f = open("ENTER THE LOCATION OF THE FILE", 'r')
for word in f:
  pyautogui.typewrite(word)
#make sure that it says press instead of TYPEWRITER or other wise it will just print "Enter"
  pyautogui.press("enter")

  
  