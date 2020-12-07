#!/usr/bin/python2
# coding=utf-8
import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool

#### WARNA RANDOM ####
P  = '\033[1;97m'  # putih
M  = '\033[1;91m' # merah
H  = '\033[1;92m' # hijau
K = '\033[1;93m' # kuning
B  = '\033[1;94m' # biru
U  = '\033[1;95m' # ungu
O = '\033[1;96m' # biru muda

my_color = [P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)

try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 crack.py")
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

os.system("clear")
done = False
def animate():
    for c in itertools.cycle(['\033[1;91m|', '\033[1;93m/', '\033[1;92m─', '\033[1;94m\\']):
        if done:
            break
        sys.stdout.write('\r\033[1;96mYayanXD ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c )
        sys.stdout.flush()
        time.sleep(0.1)
 
t = threading.Thread(target=animate)
t.start()
 
time.sleep(5)
done = True

def keluar():
	print "\033[1;97m{\033[1;91m!\033[1;97m} Keluar"
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
#########LOGO#########
logo = """ 

\033[1;91m┈┈┈╱▔▔▔▔▔▔╲┈╭━━━╮┈┈ \033[1;94mFuck Fb System.
\033[1;91m┈┈▕┈╭━╮╭━╮┈▏┃    ┃┈┈
\033[1;91m┈┈▕┈┃╭╯╰╮┃┈▏╰┳━━╯┈┈
\033[1;91m┈┈▕┈╰╯╭╮╰╯┈▏┈┃┈┈┈┈┈ 
\033[1;97m┈┈▕┈┈┈┃┃┈┈┈▏━╯┈┈┈┈┈
\033[1;97m┈┈▕┈┈┈╰╯┈┈┈▏┈┈┈┈┈┈┈
\033[1;97m┈┈▕╱╲╱╲╱╲╱╲▏┈┈┈┈┈┈┈
\033[1;94m──────────────────────────────────────────────────
\033[1;95m{\033[1;96m×\033[1;95m} \033[1;93mAuthor         \033[1;91m: \033[1;96mYayanXD
\033[1;95m{\033[1;96m×\033[1;95m} \033[1;93mInstagram      \033[1;91m: \033[1;96m@yayanxd_
\033[1;95m{\033[1;96m×\033[1;95m} \033[1;93mGroup Facebook \033[1;91m: \033[1;96mHacker Termux Indonesia
\033[1;94m──────────────────────────────────────────────────"""

logo1 = """
\033[1;91m┈┈┈╱▔▔▔▔▔▔╲┈╭━━━╮┈┈ \033[1;94mFuck Fb System.
\033[1;91m┈┈▕┈╭━╮╭━╮┈▏┃    ┃┈┈
\033[1;91m┈┈▕┈┃╭╯╰╮┃┈▏╰┳━━╯┈┈
\033[1;91m┈┈▕┈╰╯╭╮╰╯┈▏┈┃┈┈┈┈┈
\033[1;97m┈┈▕┈┈┈┃┃┈┈┈▏━╯┈┈┈┈┈
\033[1;97m┈┈▕┈┈┈╰╯┈┈┈▏┈┈┈┈┈┈┈
\033[1;97m┈┈▕╱╲╱╲╱╲╱╲▏┈┈┈┈┈┈┈

\033[1;96m▇▇▇▇▇ \033[1;91mGrup Facebook \033[1;97mHacker Termux Indonesia \033[1;96m▇▇▇▇▇"""
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []


CorrectUsername = "Yayan"
CorrectPassword = "crack"


loop = 'true'
while (loop == 'true'):
    os.system('clear')
    print logo1
    jalan("")
    jalan("\033[1;92mSudahkan Anda Mendapatkan Username And Password...")
    jalan("Untuk Login Tools? Kalo Tidak Punya Ngasal Saja")
    jalan("Nanti Di alihkan Ke YouTube")
    print "\033[1;94m──────────────────────────────────────────────────"
    username = raw_input("\x1b[1;96m{\x1b[1;93m☆\x1b[1;96m} \x1b[1;97mUsername \x1b[1;96m>>>> \x1b[1;92m")
    if (username == CorrectUsername):
    	password = raw_input("\x1b[1;96m{\x1b[1;93m☆\x1b[1;96m} \x1b[1;97mPassword \x1b[1;96m>>>> \x1b[1;92m")
        if (password == CorrectPassword):
            print "Orang Yang Paling Gans Adalah " + username
            loop = 'false'
        else:
            print "Upps Salah:("
            os.system('xdg-open https://www.Youtube.com/UCsdJQbRf0xpvwaDu1rqgJuA')
            os.system('clear') 
    else:
        print "Upps Salah:("
        os.system('xdg-open https://www.Youtube.com/UCsdJQbRf0xpvwaDu1rqgJuA')
        os.system('clear')

###### MASUK ######
def masuk():
	os.system('clear')
	print logo
	print 50* "\033[1;94m─"
	print "\033[1;97m{\033[1;92m01\033[1;97m} Login Via Token Facebook"
	print "\033[1;97m{\033[1;92m02\033[1;97m} Login Via Cokies Facebook"
	print "\033[1;97m{\033[1;92m03\033[1;97m} All Tutorial Hack Facebook"
	print "\033[1;97m{\033[1;92m04\033[1;97m} Joined Grup Facebook"
	print "\033[1;97m{\033[1;92m05\033[1;97m} Update Tools"
	print "\033[1;97m{\033[1;91m00\033[1;97m} Keluar"
	print 50* "\033[1;94m─"
	pilih_masuk()

def pilih_masuk():
	msuk = raw_input("\033[1;90m>>> \033[91m:\033[1;92m ")
	if msuk =="":
		print"\033[1;97m{\033[1;91m!\033[1;97m} lihat menu dong ajg!"
		pilih_masuk()
	elif msuk =="1" or msuk =="01":
		tokenz()
	elif msuk =="2"or msuk =="02":
		cookie()
	elif msuk =="3"or msuk =="03":
		kontol()
	elif msuk =="4"or msuk =="04":
		join_grup()
	elif msuk =="5"or msuk =="05":
		yayanxd()
	elif msuk =="0" or msuk =="00":
		keluar()
	else:
		print"\033[1;97m[\03{[1;91m!\033[1;97m} lihat menu dong ajg!"
		pilih_masuk()
		
###JOIN_GRUP###
def join_grup():
	os.system("clear")
	print logo
	print 50* "\033[1;94m─"
	jalan("        \033[1;92mAnda Akan Di Arahkan Ke Grup Facebook")
	os.system('xdg-open https://m.facebook.com/groups/294306474389772')
	time.sleep(2)
	masuk()

######TOKEN######
def tokenz():
	os.system("clear")
	print logo
	print 50* "\033[1;94m─"
	jalan("\033[1;92mMohon Tunggu Sebentar Sedang Menginstall Script...")
	os.system('pip2 install mechanize')
        os.system('pip2 install requests')
	os.system('python2 Craker.py')
	
####COKIES######
def cookie():
	os.system("clear")
	print logo
	print 50* "\033[1;94m─"
	jalan("        \033[1;92mTools Ini Menggunakan Bahasa Python3")
	jalan("       \033[1;92mHarap Bersabar Sedang Menginstall Bahan...")
	os.system('pkg update && pkg upgrade')
        os.system('pkg install git curl python')
        os.system('pkg install ruby')
        os.system('gem install lolcat')
        os.system('termux-setup-storage')
        os.system('pip install mechanize requests bs4 futures')
        os.system('pip install colorama')
        os.system('python Kontol.py')

###JOIN_GRUP###
def kontol():
	os.system("clear")
	print logo
	print 50* "\033[1;94m─"
	jalan("        \033[1;92mAnda Akan Di Arahkan Ke blogger")
	os.system('xdg-open http://squadcyberpeopleteam.blogspot.com')
	time.sleep(2)
	masuk()

##### PERBARUI #####
def yayanxd():
	os.system("clear")
	print logo
	print "\033[1;94m──────────────────────────────────────────────────"
	jalan ("\033[1;92mMemperbarui Script ...\033[1;93m")
	os.system("git pull")
	raw_input("\n\033[1;94m{\033[1;97m<Tekan Enter Untuk Lanjut kan>\033[1;94m}")
	os.system("python2 crack.py")
	
if __name__=='__main__':
	masuk()
