#!/usr/bin/python
import sys, os
# Restart ################
def restart_program():
    python = sys.exedcutable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()
##########################################
""" coded by sleepyx ."""    
os.system("clear")
print " "
print " ------------------"
print " ===|sms spammer|==="
print " [01] setup new session "
print " [02] repeat last spam "
print " [03] update "
print " [00] exit "
Spammer = raw_input(" choose ")

if (Spammer == '02' or Spammer == '2'):
    print " "
    print " SMS rate: (1s - 15min)
    Delay = raw_input(" Delay: ")
    Number = raw_input(" Number: ")
    Message = raw_input(" Message: ")
    os.system("watch -n %s termux-sms-send -n %s %s " % (ดีเลกี่วิ, เบอร์มือถือ, ข้อความ))
    sys.exit()

elif (Spammer == '02' or Spammer == '2'):
    print "nocommand"

elif (Spammer == '03' or Spammer == '3'):
    os.system("git clone")

elif (Spammer == '00' or Spammer == '0'):
    print "\n[!] Exit the program......."
    sys.exit()

elif:
    print "\n[!] ERROR : Wrong input"
    time.sleep(1)
    restart_program()


