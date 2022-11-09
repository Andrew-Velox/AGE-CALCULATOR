########IMPORTS#######
import os
import sys
import time
import datetime

########Printer########
class printer:
  def __init__(self,xx):
    for e in xx + '\n':
      sys.stdout.write(e)
      sys.stdout.flush()
      time.sleep(0.003)

##########LOGO#############

logo = ("""\033[1;31m 
     ██▒   █▓▓█████  ██▓     ▒█████  ▒██   ██▒
    ▓██░   █▒▓█   ▀ ▓██▒    ▒██▒  ██▒▒▒ █ █ ▒░
     ▓██  █▒░▒███   ▒██░    ▒██░  ██▒░░  █   ░
      ▒██ █░░▒▓█  ▄ ▒██░    ▒██   ██░ ░ █ █ ▒ 
       ▒▀█░  ░▒████▒░██████▒░ ████▓▒░▒██▒ ▒██▒
       \033[1;30m░ ▐░  ░░ ▒░ ░░ ▒░▓  ░░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
       ░ ░░   ░ ░  ░░ ░ ▒  ░  ░ ▒ ▒░ ░░   ░▒ ░
         ░░     ░     ░ ░   ░ ░ ░ ▒   ░    ░  
          ░     ░  ░    ░  ░    ░ ░   ░    ░  
         ░                                    
    	     
    \033[1;30m╔══════════════════════════════════════════╗
    ║  \033[1;35mAuthor   : \033[1;31m𝙑𝙀𝙇𝙊𝙓                     \033[1;30m   ║    
    ║  \033[1;35mGithub   : \033[1;31mAndrew-Velox                \033[1;30m ║        
    ║  \033[1;35mTelegram : \033[1;31mV3l0X                        \033[1;30m║       
    ║  \033[1;35mVersion  : \033[1;32m0.1             \033[1;30m             ║    
    ╚══════════════════════════════════════════╝
              
                \033[1;31m》\033[1;32m》\033[1;34m》\033[1;32mAGE-CAL\033[1;34m《\033[1;32m《\033[1;31m《\033[1;32m
""")

##########Text-slide############
def s_msg(i):
	for e in i + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
print(" ")
s_msg("\t  \033[1;32mTOOL IS OPENING........✔")
time.sleep(2)


def menu():
	os.system("clear")
	os.system("xdg-open https://github.com/Andrew-Velox")
	time.sleep(2)
	printer(logo)
	print("")
	print(50*"\033[1;34m-")
	print("")
	
########### inputs ###########	
	try:
	  u_year = int(input("\t \033[1;32m[•] Which \033[1;35mYear \033[1;32mDo You Born:- \033[1;35m"))
	  u_month = int(input("\n\t \033[1;32m[•] Which \033[1;35mMonth \033[1;32mDo You Born:- \033[1;35m"))
	  if u_month > 12 or u_month < 1:
	    s_msg("\n\t\t \033[1;31mWrong Input ✘✘")
	    time.sleep(2)
	    menu()
	  
	  u_day = int(input("\n\t \033[1;32m[•] Which \033[1;35mDay \033[1;32mYou Born:- \033[1;35m"))
	  print("")
	  print(50*"\033[1;34m-")
	  if u_day > 31 or u_day < 1:
	    s_msg("\n\t\t \033[1;31mWrong Input ✘✘")
	    time.sleep(2)
	    menu()
	  
########### CURRENT DATE ########	  
	  now = datetime.datetime.now()
	  present_year = int(now.strftime("%Y"))
	  present_month = int(now.strftime("%m"))
	  present_day = int(now.strftime("%d"))
	except:
	  s_msg("\n\t\t \033[1;31mWrong Input ✘✘")
	  time.sleep(0.3)
	  menu()
	  
########### EQUATION #########	  
	try:
	  if u_year <= present_year:
	    age = present_year - u_year
	    month = present_month - u_month
	    day = present_day - u_day
	    mth = 12
	    ds = 30
######### if-else instatement ########
	    if month <0:
	      yr = age - 1
	      mo = mth + month
	    else:
	      yr = age
	      mo = month
	    if day <0:
	      mon = mo - 1
	      dth = ds + day
	    else:
	      mon = mo
	      dth = day
	      
########## Result #######৳৳#
	    print("")
	    s_msg(f" \033[1;32m--- You Are\033[1;35m {yr} \033[1;32mYears \033[1;35m{mon} \033[1;32mMonths \033[1;35m{dth} \033[1;32mDays Old ✔")
	    print("")
	    print(50*"\033[1;34m-")
	    u_i = input("\n \033[1;34mPress Enter to return back:- ")
	    if u_i in [""," "]:
	      time.sleep(0.3)
	      menu()
	    if u_i in ["1","2"]:
	      os.system("python b_year_dec.py")
	    else:
	      s_msg("\n\n\t\t \033[1;35mGOODBYE 👋")
	    
	except OSError as e:
	  s_msg("\n Wrong Input..........")
	  e()
if __name__=='__main__':
  os.system("git pull")
  menu()