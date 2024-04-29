import telebot
from telebot import *
from kvsqlite.sync import Client
from a4a import *
from time import sleep
from keep_alive import  keep_alive
keep_alive()

i = Client('oao.hex')
k = 'oao'
get = i.get(k)

bot = telebot.TeleBot('6844093093:AAFHEXSt1teojra5muR30eQOPPQf-FD6zoQ')


jk = types.InlineKeyboardMarkup(row_width=3)
ss = types.InlineKeyboardButton(text='بدأ الصيد ✓',callback_data='ss')
ob = types.InlineKeyboardButton(text='ايقاف البوت',callback_data='ob')

#hh = types.InlineKeyboardMarkup(row_width=3)
sb = types.InlineKeyboardButton(text='تشغيل البوت',callback_data='sb')
jk.add(sb)
jk.add(ob)
jk.add(ss)
#hh.add(sb)

@bot.message_handler(func=lambda m:m.text in ['ستارت'])
def start(m):
	print(get)
	bot.send_message(m.chat.id,'مرحبا بك عزيزي المالك، هذه الازرار و استخدمهن يروحي ،',reply_markup=jk)
		
@bot.callback_query_handler(func=lambda c:True)
def cl(c):
	data =c.data
	ci = c.message.chat.id
	if data == 'ss':
		print('done')
		iu = bot.send_message(c.message.chat.id,text='تم بدأ الصيد')
		bot.register_next_step_handler(iu,sts)
		
	if data=='ob':
			i.set(k,False)
			bot.send_message(ci,text='تم ايقاف البوت ')
			print('stop')
	if data =='sb':
			i.set(k,True)
			print(f'f {get}')
			bot.send_message(ci,'تم تشغيل البوت ✓ ،')
	
@bot.message_handler(func=lambda m:False)
def sts(m):
			
			#asi.add(oob)
			ii = bot.send_message(m.chat.id,text='انجب؟')
			while True:
				rq = '0123456789'
				aa = 'qwertyuiopasdfghjklzxcvbnm'
				aaa = '0123456789qwertyuiopasdfghjklzxcvbnm'
				a = random.choice(aa)
				b = random.choice(aa)
				c = random.choice(aa)
				d = random.choice(aa)
				e = random.choice(aaa)
				f = random.choice(aaa)
				g = random.choice(rq)
				h = random.choice(rq)
				i = random.choice(rq)
				j = random.choice(rq)
				li = f'{a}{a}{b}{b}{c}'
				lii = f'{a}{b}{b}{c}{c}'
				liii = f'{a}{a}{b}{c}{c}'
				liiii = f'{a}{a}{b}{b}{c}'
				lu = f'{a}{a}{a}{c}{d}'
				luu = f'{a}{b}{c}{c}{c}'
				lpp = f'{a}.{f}.{e}' 
				lppp = f'{a}.{f}_{e}'
				lpppp = f'{a}_{f}_{e}'  
				loi = f'{a}_{f}.{e}'
				lis = [li,lii,liii,liiii,lu,luu,lpp,lppp,lpppp,loi]
				kkl = random.choice(lis)
				req = requests.post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',headers ={'Host':'www.instagram.com',
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
'user-agent':generate_user_agent(),
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
'cookie':'ig_nrcb=1'},data=f'email=aakmnnsjskksmsnsn%40gmail.com&username={kkl}&first_name=&opt_into_one_tap=false')
				if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in req.text:
					pass
					print('⛔ USER IS BAND : '+kkl)
				elif  '"errors": {"username":' in req.text or  '"code": "username_is_taken"' in req.text:
				     fail = f'''
				غير متاح {kkl} ❌
				'''
				#h = bot.send_message(m.chat.id,text='انجب؟')
				asi = types.InlineKeyboardMarkup(row_width=3)
				oob = types.InlineKeyboardButton(text=f'غير متاح : {kkl} ❌',callback_data='uub')
				asi.add(oob)
				sleep(2)
				bot.edit_message_reply_markup(chat_id=ii.chat.id, message_id=ii.message_id,reply_markup=asi)
				print('❌ USER IS UNVALID : '+kkl)
			else:
					print('✅ USER IS VALID : '+kkl)
					bot.send_message(m.chat.id,text=f'				تم صيد يوزر جديد : @{kkl} \n@j_tja | @AboMlakk ,',parse_mode='markdown')
			
			'''
	if data =='sb' and get==True:
			bot.send_message(ci,'تم تشغيل البوت ✓ ،')
			i.delete(k)
			i.set(k,True)
			print(f'f {get}')'''
			#@j_tja 
bot.infinity_polling()		
