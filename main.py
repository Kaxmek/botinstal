import sys,os
os.system("pip install pyTelegramBotAPI")
os.system("pip install pyTelegramBotAPI==3.7.7")
os.system("pip install stdiomask")
os.system("pip install OneClick")
os.system("pip install user_agent")
os.system("pip install uuid")
os.system("pip install uuid4")
os.system("pip install token_hex")
os.system("pip install telebot")
os.system("pip install instaloader")
os.system("pip install requests")
os.system("pip install secrets")
os.system("pip install uid")
os.system("pip install types")
import requests 
import os
import telebot
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
csr = token_hex(8)*2
bot = telebot.TeleBot(5643156448:AAHiUgLVPNnREH2NKvVgLnVo5bmuzlOaH8w)
@bot.message_handler(commands=["start"])
def st(message):
    dev = types.InlineKeyboardButton(text="channel telegram", url="https://t.me/bsx_h2")
    key = types.InlineKeyboardMarkup()
    key.add(dev)
    ID = message.from_user.id
    bot.send_message(message.chat.id,"اهلا بك عزيزي في بوت اضهار معلومات حساب انستا من يوزر فقط\n———————×———————\nارسل يوزرك الان\nالمبرمج @PPGBB",reply_markup=key,reply_to_message_id=message.message_id)
@bot.message_handler(func=lambda m:True)
def start(message):
    bot.send_message(message.chat.id,"Wait please")
    ggg = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(ggg.context, message.text)
    head = {
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
      "Host": "i.instagram.com",
      "Connection": "Keep-Alive",
      "User-Agent": Hunter.Services(),
      "Cookie": "mid=YwvCRAABAAEsZcmT0OGJdPu3iLUs; csrftoken="+csr,
      "Cookie2": "$Version=1",
      "Accept-Language": "en-US",
      "X-IG-Capabilities": "AQ==",
      "Accept-Encoding": "gzip",}
    data= {"q":message.text,
   "device_id":f"android{uid}",
   "guid":uid,
   "_csrftoken":csr}
    kid=requests.post('https://i.instagram.com/api/v1/users/lookup/',headers=head,data=data).json()
    api = f'https://www.instagram.com/{message.text}/?__a=1&__d=dis'
    rr=requests.get(api).json()

    iddd = (profile.userid)
    nam = (profile.full_name)
    fol = (profile.followees)
    fols =(profile.followers)
    bio = (profile.mediacount)
    bayo = (profile.biography,profile.external_url)
    pc = (profile.profile_pic_url)
    re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")   
    ree = re.json()
    dat = ree['date']
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
    data=data= {"user_email":message.text,
   "device_id":f"android{iddd}",
   "guid":iddd,
   "_csrftoken":csr}
    restt=requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',data=data,headers=head)
    res=restt.json()
    ress=restt.text
    if 'obfuscated_email' in ress:
    	email=res['obfuscated_email']
    	bot.send_photo(message.chat.id,pc,caption=f"<strong>Name : » {nam}\nuser :  » {message.text}\nID : » {iddd}\ndate : » {dat}\nFollowing :  » {fol}\nFollowers :  » {fols}\npost : » {bio}\nBYO : » {bayo}\nRest : » {email}</strong>",parse_mode="html")
    if "graphql" not in nam:
        pass
bot.polling(True)
    
