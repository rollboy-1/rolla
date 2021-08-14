import telebot
import requests
from telebot import types
import random
import time

rhaby = int(1)
TOKEN = ("1893808867:AAFs2L7b_66CbDo0CSIytLiCu1USerEBbNU")
bot = telebot.TeleBot(TOKEN)
stop = True
@bot.message_handler(commands=['start'])
def send_welcome(message):
	mas = types.InlineKeyboardMarkup(row_width=2)
	v= types.InlineKeyboardButton("Developer ⸙",url='https://t.me/rolll1')
	mas.add(v)
	ru = message.from_user.first_name
	Ruk=bot.send_message(message.chat.id,f"""
-- -- -- -- - -- -- -- -- -- -- -- -- --
≈ welcome [{ru}](t.me/rolll3) ⸙
≈ Checker Telegram Username
≈ Coded By @rolll1
-- -- -- -- - -- -- -- -- -- -- -- -- --
""",parse_mode="Markdown",disable_web_page_preview='True',reply_markup=mas)
	bot.register_next_step_handler(Ruk,ple)
def ple(message):
	mar= types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	A = types.KeyboardButton(' Start ⸙ ')
	mar.add(A)
	bot.send_message(message.chat.id, "Choose from the buttons at the bottom",reply_markup=mar)
	
@bot.message_handler(func=lambda message: True)		
def send_welcome(message):
	global stop	
	if message.text =='Suspension Stop':
		stop = False			
	if message.text =='Suspension stop':
		stop = False
		mar= types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		A = types.KeyboardButton(' Start ⸙ ')
		mar.add(A)
		bot.send_message(message.chat.id, "Choose from the buttons at the bottom",reply_markup=mar)		
	if message.text =='Start ⸙':
		stop = True
		mas = types.InlineKeyboardMarkup(row_width=1)
		A = types.InlineKeyboardButton(" start ️", callback_data="F2")
		D = types.InlineKeyboardButton("Developer ⸙",url='https://t.me/DIBIBl')
		mar= types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		G = types.KeyboardButton('Suspension stop')
		mar.add(G)
		mas.add(A,D)
		bot.send_message(message.chat.id, "Choose from the buttons at the bottom",reply_markup=mar)
		bot.send_message(message.chat.id,'Click Run to start',reply_markup=mas)
@bot.callback_query_handler(func=lambda call:True )    
def sdd(call):
	
	@bot.message_handler(func=lambda message: True)		
	def send_welcome(message):
		if message.text =='Suspension stop':
			stop = False
	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Work is underway")
	global stop
	good=0
	bad=0
	kol =0
	N =0
	hh='4','5','6'
	t ='poiuytrewqasdfghjklmnbvcxz1234567890'
	tuks1 = 'poiuytrewqasdfghjklmnbvcxz1234567890'
	while stop == True:
		e = str("".join(random.choice(hh)for i in range(1)))
		
		rhaby2 = int(e)
		kol+=1
		N +=1
		rhaby1 = str("".join(random.choice(t)for i in range(2)))
		email =  str("".join(random.choice(tuks1)for i in range(1)))
		for password in range(rhaby):
			password = ''
			for item in range(rhaby2):
				rhaby3 = ''
			for item in range(rhaby2):
				rhaby3 += random.choice(rhaby1)
			user = (rhaby3+email)
			time.sleep(1)
			url = f"https://t.me/{user}"
			r = requests.get(url)
			if r.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
				good +=1
				tt=time.asctime()
				bot.send_message(call.message.chat.id,f'⌯  ʜɪ ѕɪʀ ɴᴇᴡ ғᴀᴄᴋᴇᴅ ⌯\n. — — — — —  — — — — — . \n⌯ ᴜѕᴇʀɴᴀᴍᴇ : @{user}\n⌯ {tt} \n. — — — — —  — — — — —\n• Tele : @rolll1 . @rolll3 .')
			else:
				bad+=1
			mas = types.InlineKeyboardMarkup(row_width=1)
			A = types.InlineKeyboardButton(f" {user}", callback_data="F1")
			B = types.InlineKeyboardButton(f" Done :{good}", callback_data="F2")
			e = types.InlineKeyboardButton(f" Bad :{bad}", callback_data="6y")
			o = types.InlineKeyboardButton(f" Entrance :{kol}", callback_data="gf")
			mas.add(A,B,e,o)
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Work is underway",reply_markup=mas)

try:
	bot.polling(none_stop=True)
except:
	bot.polling(none_stop=True)
	pass
