# -*- coding: utf-8 -*-
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
os.system('clear')
print """
\033[1;91m
 __  __        ____  _____  _  _______  ___   ___  
 |  \/  |      |  _ \|  __ \| |/ /  __ \|__ \ / _ \ 
 | \  / |_ __  | |_) | |  | | ' /| |__) |  ) | (_) |
 | |\/| | '__| |  _ <| |  | |  < |  _  /  / / > _ < 
 | |  | | |_   | |_) | |__| | . \| | \ \ / /_| (_) |
 |_|  |_|_(_)  |____/|_____/|_|\_\_|  \_\____|\___/ 
                                                    
                                                    

                          """
print("create \033[1;92mMr. BDKR28")

time.sleep(3)
print ""
print ""

CorrectUsername = "Mr.BDKR28"
CorrectPassword = "MR. BDKR28"

loop = 'true'
while (loop == 'true'):
    username = raw_input("Tool Username : ")
    if (username == CorrectUsername):
    	password = raw_input("Tool Password : ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:BDKR28_SANA_FAROOQ
            os.system('xdg-open https://www.facebook.com/ctfsolution')
            
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;93mWrong Password"
            os.system('xdg-open https://www.facebook.com/ctfsolution')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://www.facebook.com/ctfsolution')
        
        
os.system('clear')
      
        
os.system ('python ....')
