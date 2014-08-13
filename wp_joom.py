import urllib
import os
import re
from time import sleep
from datetime import date
def welcome(modulename):

  print  """
          |==========================================================|
          |======================  [ 404 ]   ========================|
          |==============[ lordnotfound404@gmail.com ]===============|
          |==========[ https://www.facebook.com/404andreas]==========|
          |==========================================================|
          |      ****      Web Hacking framwork by 404      ***      |
          |==========================================================|
        """
  print  '#######    ' + modulename

###########################################################
def serverTargeting(IP):
  welcome("perform many dork based scans")
  #fil = open(logsfilename+'.txt','a')
  #fil.write("[Info] : new target "+now.strftime("%A %d %b %Y")+"IP adress : "+IP)
  #print "[Info] : new target "+now.strftime("%A %d %b %Y")+"IP adress : "+IP
  #fil.write("[Info] : getting links from Bing")
  print " New TARGET " + IP
  print "[Info] : getting Hosted domains from Bing"
  file2 =open(IP+'hosted.txt','w')
  start=0
  end=200
  sleep(3)
  dork = 'IP:'+IP
  #print "[info]Getting Websites From Bing ... "
  while  start <= end :
    try:
      con = urllib.urlretrieve('http://www.bing.com/search?q='+dork+"&first="+str(start))
      #con = con = urllib.urlretrieve('http://www.bing.com/search?q=ip%3A41.203.11.42+%22php%3Fid%3D%22&go=&qs=ds&form=QBLH&filt=all')
      conf = open(con[0])
      readd=conf.read()
      find=re.findall('<h2><a href="(.*?)"',readd)
      start = start+10
    except IOError:
      print "[ERROR]network error "
      print "[Info]reconnecting "
      sleep(10)
      print "[Info]retrying "
    try :

      for i in range(len(find)):
       rez=find[i]
       file2.write(rez + '\n')
    except IOError:
      print "[ERROR]No result found"
  print "[Info] : links list saved in file "+IP+"hosted.txt"
  print "[Info] : getting wordpress sites from server ...."

  
  file2 =open(IP+'wp_Powred.txt','w')
  start=0
  end=200
  sleep(3)
  dork = 'IP:'+IP + "  /wp-content/"
  #print "[info]Getting Websites From Bing ... "
  while  start <= end :
    try:
      con = urllib.urlretrieve('http://www.bing.com/search?q='+dork+"&first="+str(start))
      #con = con = urllib.urlretrieve('http://www.bing.com/search?q=ip%3A41.203.11.42+%22php%3Fid%3D%22&go=&qs=ds&form=QBLH&filt=all')
      conf = open(con[0])
      readd=conf.read()
      find=re.findall('<h2><a href="(.*?)"',readd)
      start = start+10
    except IOError:
      print "[ERROR]network error "
      print "[Info]reconnecting "
      sleep(10)
      print "[Info]retrying "
    try :

      for i in range(len(find)):
       rez=find[i]
       file2.write(rez + '\n')
    except IOError:
      print "[ERROR]No result found"
  
  #getsitesbing("IP:"+IP+" /wp-content/" , 'wp_Powred' )
  print "[Info] : links list saved in file "+IP+"wp_Powred.txt"
  print "[Info] : getting joomla sites from server ...."

   
  file2 =open(IP+'joom_Powred.txt','w')
  start=0
  end=200
  sleep(3)
  dork = 'IP:'+IP +" index.php?option=com_content"
  #print "[info]Getting Websites From Bing ... "
  while  start <= end :
    try:
      con = urllib.urlretrieve('http://www.bing.com/search?q='+dork+"&first="+str(start))
      #con = con = urllib.urlretrieve('http://www.bing.com/search?q=ip%3A41.203.11.42+%22php%3Fid%3D%22&go=&qs=ds&form=QBLH&filt=all')
      conf = open(con[0])
      readd=conf.read()
      find=re.findall('<h2><a href="(.*?)"',readd)
      start = start+10
    except IOError:
      print "[ERROR]network error "
      print "[Info]reconnecting "
      sleep(10)
      print "[Info]retrying "
    try :

      for i in range(len(find)):
       rez=find[i]
       file2.write(rez + '\n')
    except IOError:
      print "[ERROR]No result found"
  
  #getsitesbing("IP:"+IP+" index.php?option=com_content" , 'joom_Powred' )

  print "[Info] : links saved in file "+IP+"joom_Powred.txt"
  print " ALL is done good luck dude !!!!! "
###########################################################
welcome("Joomla and wordpress Sites Finder")
IPadress=raw_input("[INFO] : enter IP adress  : ")
serverTargeting(IPadress)



